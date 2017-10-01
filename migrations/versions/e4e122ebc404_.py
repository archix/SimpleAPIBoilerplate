"""empty message

Revision ID: e4e122ebc404
Revises: 
Create Date: 2017-09-29 16:40:36.760549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4e122ebc404'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('user_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('phone_number', sa.String(length=50), nullable=True),
    sa.Column('postal_code', sa.String(length=10), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=True),
    sa.Column('gender', sa.String(length=20), nullable=True),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    role_table = sa.sql.table('role',
                              sa.sql.column('id', sa.Integer),
                              sa.sql.column('name', sa.String)
                              )
    user_table = sa.sql.table('user',
                              sa.sql.column('id', sa.Integer),
                              sa.sql.column('email', sa.String),
                              sa.sql.column('password', sa.String),
                              sa.sql.column('role_id', sa.ForeignKey)
                              )
    op.bulk_insert(role_table,
                   [
                       {'id': 1, 'name': 'Admin'},
                       {'id': 2, 'name': 'Manager'},
                       {'id': 3, 'name': 'User'},
                   ]
                   )
    op.bulk_insert(user_table,
                   [
                       {'id': 1,
                        'email': 'admin@maildrop.cc',
                        'password': '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',
                        'role_id': 1}
                   ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_details')
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###
