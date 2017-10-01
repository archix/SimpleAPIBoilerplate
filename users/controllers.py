from flasgger import swag_from
from flask import Blueprint, request, Response, abort, json, g

from users import consts
from users.exceptions import UserException
from users.models import User
from utils.decorators import transactional, verify_token
from utils.docs.add_user import add_user_specs
from utils.docs.get_profile import get_profile_specs
from utils.docs.get_users import get_users_specs
from utils.docs.login_register import login_specs, confirm_register_specs, register_specs
from utils.docs.update import update_specs, update_another_specs

user = Blueprint('user', __name__)


@user.route('/register/', methods=['POST'])
@swag_from(register_specs)
def register():
    data = request.get_json(force=True)
    try:
        new_user, token = User.register(data)
    except UserException as e:
        abort(e.status_code, e.msg)
    return Response(json.dumps({'user': new_user.to_dict(show=['details']), 'token': token}),
                    status=201, mimetype='application/json')


@user.route('/register/confirm/', methods=['POST'])
@swag_from(confirm_register_specs)
@transactional
def register_confirmation():
    data = request.get_json(force=True)
    token = data.get('token')
    if not token:
        abort(400, 'No token provided.')
    try:
        result = User.register_confirm(token)
        return Response(json.dumps(result), status=200, mimetype='application/json')
    except UserException as e:
        abort(e.status_code, e.msg)


@user.route('/login/', methods=['POST'])
@swag_from(login_specs)
def login():
    data = request.get_json(force=True)
    try:
        result = User.login(data)
    except UserException as e:
        abort(e.status_code, e.msg)
    return Response(json.dumps(result), status=200, mimetype='application/json')


@user.route('/me/', methods=['GET', 'PUT'])
@verify_token
@transactional
@swag_from(get_profile_specs, methods=['GET'])
@swag_from(update_specs, methods=['PUT'])
def user_profile():
    logged_user = g.user
    if request.method == 'PUT':
        try:
            json_data = request.get_json(force=True)
            logged_user.update(json_data)
        except UserException as e:
            abort(e.status_code, e.msg)
    return Response(json.dumps(logged_user.to_dict(show=['details'])), status=200, mimetype='application/json')


@user.route('/dashboard/users/', methods=['GET'])
@swag_from(get_users_specs)
@verify_token
def dashboard_users():
    lim = int(request.args.get('limit', 10))
    off = int(request.args.get('offset', 0))
    result = User.get_users(off, lim)
    return Response(json.dumps([u.to_dict() for u in result]), status=200, mimetype='application/json')


@user.route('/dashboard/users/', methods=['POST'])
@swag_from(add_user_specs)
@verify_token(roles_required=[consts.ROLE_ADMIN])
def dashboard_users_add():
    data = request.get_json(force=True)
    token = None
    try:
        if data['role_id'] == consts.ROLE_MANAGER:
            new_user, token = User.create_manager(data)
        elif data['role_id'] == consts.ROLE_ADMIN:
            data['active'] = True
            new_user = User.create_admin(data)
        else:
            data['active'] = True
            new_user = User.create_user(data, consts.ROLE_USER)
    except UserException as e:
        abort(e.status_code, e.msg)
    result = {'user': new_user.to_dict(show=['details'])}
    if token:
        result['token'] = token
    return Response(json.dumps({'user': new_user.to_dict(show=['details']), 'token': token}),
                    status=201, mimetype='application/json')


@user.route('/dashboard/users/<user_id>/', methods=['PUT'])
@swag_from(update_another_specs)
@verify_token(roles_required=[consts.ROLE_ADMIN, consts.ROLE_MANAGER])
@transactional
def dashboard_users_update(user_id):
    json_data = request.get_json(force=True)
    update_user = User.query.get(user_id)
    if not user:
        abort(404, 'User does not exist')
    try:
        update_user.update(json_data)
    except UserException as e:
        abort(e.status_code, e.msg)
    return Response(json.dumps(update_user.to_dict(show=['details'])), status=200, mimetype='application/json')
