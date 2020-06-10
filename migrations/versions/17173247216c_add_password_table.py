"""Add password table

Revision ID: 17173247216c
Revises: 242bda1d9405
Create Date: 2020-06-09 11:20:48.875161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17173247216c'
down_revision = '242bda1d9405'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###