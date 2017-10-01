import datetime

import jwt
from flask import current_app, g
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import backref

from extensions import db
from users import consts
from users.exceptions import UserBadRequestException, UserUnauthorized
from utils.email_providers.factory import EmailProviderFactory
from utils.models.meta import Model
from utils.password import hash_password


class Base(Model):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now)

    read_only_fields = ['id', 'created_at', 'updated_at']


class User(Base):
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    active = db.Column(db.Boolean, default=False)
    role_id = db.Column(db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', backref=db.backref('users', lazy='dynamic'))
    details = db.relationship('UserDetails', uselist=False, backref=backref("user", uselist=False))

    default_fields = ['first_name', 'last_name', 'email', 'role', 'active']
    hidden_fields = ['password']
    read_only_fields = Base.read_only_fields + ['user_details_id']

    def __str__(self):
        return '{}: User - {}'.format(self.id, self.full_name)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @classmethod
    def create_admin(cls, json_data):
        admin = cls.create_user(json_data, consts.ROLE_ADMIN)
        return admin

    @classmethod
    def create_manager(cls, json_data):
        """
        Creates inactive manager and sends invitation mail
        :param json_data:
        :return:
        """
        manager = cls.create_user(json_data, consts.ROLE_MANAGER)
        token = manager.generate_token(expiration=30).decode()
        # send email
        email_provider = EmailProviderFactory.get_email_provider(current_app.config['EMAIL_PROVIDER'])
        email_provider.send_email(
            current_app.config['EMAIL_FROM'],
            current_app.config['EMAIL_FROM_NAME'],
            'API - You\'re invited',
            'Please confirm invitation by clicking following link {}?token={}'.format(
                current_app.config['FRONTEND_URL'],
                token
            ),
            [{'Email': manager.email}]
        )
        return manager, token

    @classmethod
    def create_user(cls, json_data, role_id):
        json_data['role_id'] = role_id
        user = cls.from_dict(json_data)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError as e:
            raise UserBadRequestException(e.orig.pgerror)
        return user

    @classmethod
    def from_dict(cls, json_data):
        obj = cls()
        obj.first_name = json_data.get('first_name')
        obj.last_name = json_data.get('last_name')
        obj.email = json_data.get('email')
        obj.password = hash_password(json_data.get('password'))
        obj.role_id = json_data.get('role_id')
        obj.active = json_data.get('active')
        return obj

    def generate_token(self, expiration=None):
        expiration = expiration if expiration else 60
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration),
            'iat': datetime.datetime.utcnow(),
            '_id': self.id
        }
        return jwt.encode(
            payload,
            current_app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )

    @classmethod
    def get_users(cls, offset, limit):
        """
        Used for /dashboard/users
        :return: list of users for Admin and Manager, but only logged in user if User
        """
        if g.user.role.id == consts.ROLE_USER:
            return [g.user]
        else:
            return cls.query.order_by('id').offset(offset).limit(limit)

    @classmethod
    def login(cls, data):
        email = data.get('email')
        password = data.get('password')
        if not (email and password):
            raise UserBadRequestException('email and password required')

        password = hash_password(password)
        user = cls.query.filter_by(email=email, password=password).first()
        if not user:
            raise UserUnauthorized('Invalid Credentials')

        if not user.active:
            raise UserUnauthorized('Inactive')

        return {'token': user.generate_token().decode()}

    @classmethod
    def register(cls, data):
        user = cls.create_user(data, consts.ROLE_USER)
        token = user.generate_token(expiration=30).decode()
        # send email
        email_provider = EmailProviderFactory.get_email_provider(current_app.config['EMAIL_PROVIDER'])
        email_provider.send_email(
            current_app.config['EMAIL_FROM'],
            current_app.config['EMAIL_FROM_NAME'],
            'API - Confirm registration',
            'Please confirm registration by clicking following link {}?token={}'.format(
                current_app.config['FRONTEND_URL'],
                token
            ),
            [{'Email': user.email}]
        )
        return user, token

    @classmethod
    def register_confirm(cls, token):
        """
        Activates user
        :param token: token sent to user email
        :return: login token so user can access app
        """
        try:
            payload = jwt.decode(token, current_app.config.get('SECRET_KEY'))
            confirmed_user = cls.query.get(payload['_id'])
            confirmed_user.active = True
            return {'token': confirmed_user.generate_token().decode()}
        except jwt.ExpiredSignatureError:
            raise UserUnauthorized('Token expired,')
        except jwt.InvalidTokenError:
            raise UserUnauthorized('Invalid Token.')

    def update(self, data):
        for key, value in data.items():
            if key in self.read_only_fields:
                raise UserBadRequestException(msg='Can not update read only fields. {}'.format(self.read_only_fields))
            if key == 'details':
                if self.details:
                    self.details.update(data[key])
                else:
                    ud = UserDetails.from_dict(data[key])
                    ud.user_id = self.id
                    db.session.add(ud)
                continue
            elif key == 'role':
                raise UserBadRequestException(msg='Can not update role in this call.')

            setattr(self, key, value)


class UserDetails(Base):
    address = db.Column(db.String(200))
    phone_number = db.Column(db.String(50))
    postal_code = db.Column(db.String(10))
    date_of_birth = db.Column(db.DateTime)
    gender = db.Column(db.String(20))
    avatar = db.Column(db.String)

    user_id = db.Column(db.ForeignKey('user.id'))

    default_fields = ['address', 'phone_number', 'postal_code', 'date_of_birth', 'gender', 'avatar']

    @classmethod
    def from_dict(cls, json_data):
        obj = cls()
        obj.address = json_data.get('address')
        obj.phone_number = json_data.get('phone_number')
        obj.postal_code = json_data.get('postal_code')
        obj.date_of_birth = json_data.get('date_of_birth')
        obj.gender = json_data.get('gender')
        obj.avatar = json_data.get('avatar')
        obj.user_id = json_data.get('user_id')
        return obj

    def update(self, data):
        for key, value in data.items():
            # read only is not allowed. I'll let it fail silently atm
            if key in self.read_only_fields or key in self.__mapper__.relationships.keys():
                continue
            setattr(self, key, value)


class Role(Base):
    name = db.Column(db.String(15))

    default_fields = ['name']
