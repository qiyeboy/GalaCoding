"""initial migration

Revision ID: 667330514dbe
Revises: None
Create Date: 2016-04-20 20:59:55.633000

"""

# revision identifiers, used by Alembic.
revision = '667330514dbe'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('system',
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('system')
    ### end Alembic commands ###
