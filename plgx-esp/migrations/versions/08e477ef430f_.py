"""empty message

Revision ID: 08e477ef430f
Revises: 8eb52199a52c
Create Date: 2021-07-06 10:29:21.567229

"""

# revision identifiers, used by Alembic.
revision = '08e477ef430f'
down_revision = '8eb52199a52c'

from alembic import op
import sqlalchemy as sa
import polylogyx.db.database
from sqlalchemy.dialects import postgresql


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.add_column('rule', sa.Column('platform', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rule', 'platform')

    # ### end Alembic commands ###