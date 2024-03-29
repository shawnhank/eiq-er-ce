"""empty message

Revision ID: f7a19a90adfd
Revises: 47386cd00c1e
Create Date: 2019-11-19 12:22:36.090021

"""

# revision identifiers, used by Alembic.
revision = "f7a19a90adfd"
down_revision = "47386cd00c1e"

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql



def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.add_column("default_query", sa.Column("arch", sa.String(), nullable=True))
    op.add_column("default_filters", sa.Column("arch", sa.String(), nullable=True))
    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_column("default_query", "arch")
    op.drop_column("default_filters", "arch")

    # ### end Alembic commands ###
