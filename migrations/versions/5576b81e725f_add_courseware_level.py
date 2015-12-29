# -*- coding: utf-8 -*-
"""add courseware level

Revision ID: 5576b81e725f
Revises: 23fc76e750a0
Create Date: 2015-12-29 10:10:53.643077

"""

# revision identifiers, used by Alembic.
revision = '5576b81e725f'
down_revision = '23fc76e750a0'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###

    # enum is added manually
    conn = op.get_bind()
    enum = postgresql.ENUM(u"幼小衔接班", u"小班", u"中班", u"大班", name='courseware level')
    enum.create(op.get_bind(), checkfirst=True)

    op.add_column('courseware', sa.Column('level', postgresql.ENUM(u'\u5e7c\u5c0f\u8854\u63a5\u73ed', u'\u5c0f\u73ed', u'\u4e2d\u73ed', u'\u5927\u73ed', name='courseware level'), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('courseware', 'level')
    postgresql.ENUM(name="courseware level").drop(op.get_bind(), checkfirst=False)
    ### end Alembic commands ###
