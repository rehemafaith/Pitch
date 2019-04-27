"""Initial Migration

Revision ID: 30c9f4fb38fe
Revises: 295b454f59ca
Create Date: 2019-04-24 22:01:32.297923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30c9f4fb38fe'
down_revision = '295b454f59ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
