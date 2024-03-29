"""empty message

Revision ID: 91fda2055a1c
Revises: 351aa45dc518
Create Date: 2024-01-22 09:58:05.366119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91fda2055a1c'
down_revision = '351aa45dc518'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('show', schema=None) as batch_op:
        batch_op.drop_column('venue_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('show', schema=None) as batch_op:
        batch_op.add_column(sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
