"""empty message

Revision ID: 1d40fae6192f
Revises: 3be18890cd19
Create Date: 2017-09-30 14:35:48.833466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d40fae6192f'
down_revision = '3be18890cd19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_user_details_id_fkey', 'user', type_='foreignkey')
    op.drop_column('user', 'user_details_id')
    op.add_column('user_details', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user_details', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_details', type_='foreignkey')
    op.drop_column('user_details', 'user_id')
    op.add_column('user', sa.Column('user_details_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('user_user_details_id_fkey', 'user', 'user_details', ['user_details_id'], ['id'])
    # ### end Alembic commands ###
