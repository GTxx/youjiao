"""empty message

Revision ID: 39ded2bff92b
Revises: 1f62cf8270a4
Create Date: 2015-10-13 16:56:15.644892

"""

# revision identifiers, used by Alembic.
revision = '39ded2bff92b'
down_revision = '1f62cf8270a4'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('qiniu_key', sa.String(length=200), nullable=True),
    sa.Column('json', postgresql.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('qiniu_key')
    )
    op.create_table('document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('qiniu_key', sa.String(length=200), nullable=True),
    sa.Column('json', postgresql.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('qiniu_key')
    )
    op.create_table('online_course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('publish', sa.Boolean(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('category', sa.Enum(u'\u4f18\u79c0\u8bfe\u5802', u'\u4f18\u79c0\u8bb2\u5ea7', u'\u5176\u4ed6\u89c6\u9891', u'\u4ea7\u54c1\u4f7f\u7528\u57f9\u8bad', u'\u5e08\u8d44\u57f9\u8bad\u89c6\u9891', name='online_course_category'), nullable=True),
    sa.Column('content', postgresql.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'video', sa.Column('json', postgresql.JSON(), nullable=True))
    op.add_column(u'video', sa.Column('qiniu_key', sa.String(length=200), nullable=True))
    op.create_unique_constraint(None, 'video', ['qiniu_key'])
    op.drop_column(u'video', 'category')
    op.drop_column(u'video', 'update_time')
    op.drop_column(u'video', 'name')
    op.drop_column(u'video', 'url')
    op.drop_column(u'video', 'publish')
    op.drop_column(u'video', 'content')
    op.drop_column(u'video', 'create_time')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'video', sa.Column('create_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column(u'video', sa.Column('content', postgresql.JSON(), autoincrement=False, nullable=True))
    op.add_column(u'video', sa.Column('publish', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(u'video', sa.Column('url', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.add_column(u'video', sa.Column('name', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.add_column(u'video', sa.Column('update_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column(u'video', sa.Column('category', postgresql.ENUM(u'\u4f18\u79c0\u8bfe\u5802', u'\u4f18\u79c0\u8bb2\u5ea7', u'\u5176\u4ed6\u89c6\u9891', u'\u4ea7\u54c1\u4f7f\u7528\u57f9\u8bad', u'\u5e08\u8d44\u57f9\u8bad\u89c6\u9891', name='video_category'), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'video', type_='unique')
    op.drop_column(u'video', 'qiniu_key')
    op.drop_column(u'video', 'json')
    op.drop_table('online_course')
    op.drop_table('document')
    op.drop_table('audio')
    ### end Alembic commands ###
