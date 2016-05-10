"""empty message

Revision ID: 07d57a9a0cd7
Revises: e2e08634f5c0
Create Date: 2016-05-10 18:58:50.570000

"""

# revision identifiers, used by Alembic.
revision = '07d57a9a0cd7'
down_revision = 'e2e08634f5c0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('tags_txt', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'tags_txt')
    ### end Alembic commands ###
