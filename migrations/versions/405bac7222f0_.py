# -*- coding: utf-8 -*-
"""empty message

Revision ID: 405bac7222f0
Revises: None
Create Date: 2015-09-29 15:25:49.942116

"""

# revision identifiers, used by Alembic.
revision = '405bac7222f0'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('album',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('chief_editor', sa.String(length=16), nullable=True),
    sa.Column('executive_editor', sa.String(length=16), nullable=True),
    sa.Column('publisher', sa.String(length=16), nullable=True),
    sa.Column('book_size', sa.Enum(u'16\u5f00', name='book_size'), nullable=True),
    sa.Column('level', sa.Enum(u'\u5e7c\u5c0f\u8854\u63a5\u73ed', u'\u5c0f\u73ed', u'\u4e2d\u73ed', u'\u5927\u73ed', name='level'), nullable=True),
    sa.Column('category', sa.Enum(u'\u5e7c\u6559\u6559\u6750', u'\u5e7c\u6559\u8bfb\u7269', name='book_category'), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('publish', sa.Boolean(), nullable=True),
    sa.Column('image_array', postgresql.ARRAY(sa.String(length=255)), nullable=True),
    sa.Column('preview_array', postgresql.ARRAY(sa.String(length=255)), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('video',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('publish', sa.Boolean(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('category', sa.Enum(u'\u4f18\u79c0\u8bfe\u5802', u'\u4f18\u79c0\u8bb2\u5ea7', u'\u5176\u4ed6\u89c6\u9891', u'\u4ea7\u54c1\u4f7f\u7528\u57f9\u8bad', u'\u5e08\u8d44\u57f9\u8bad\u89c6\u9891', name='video_category'), nullable=True),
    sa.Column('content', postgresql.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('youjiao_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.Column('phone_number', sa.String(length=16), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('origin', sa.String(length=255), nullable=True),
    sa.Column('html', sa.Text(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('category', sa.Enum('policy', 'news', 'events', 'research', 'activity', 'achievement', name='category'), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['youjiao_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comment_obj_id', sa.Integer(), nullable=True),
    sa.Column('comment_obj_type', sa.Enum('book', 'courseware', name='comment_obj_type'), nullable=True),
    sa.Column('content', sa.String(length=140), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['youjiao_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('courseware',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('content', postgresql.JSON(), nullable=True),
    sa.Column('publish', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('obj_id', sa.Integer(), nullable=True),
    # 这里其实是后加的，但是直接写一个迁移文件太麻烦，我放弃了。
    # 因为没有alembic的migrate，我直接在数据库做的alter type。
    # 这个地方只作为第一次migrate用。
    sa.Column('obj_type', sa.Enum('book', 'courseware', 'onlinecourse', name='like_obj_type'), nullable=True),
    sa.ForeignKeyConstraint(['obj_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['youjiao_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'obj_id', 'obj_type', name='_user_favor_obj')
    )
    op.create_table('page',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('html', sa.Text(), nullable=True),
    sa.Column('status', sa.String(length=2), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['youjiao_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('photo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('qiniu_key', sa.String(length=200), nullable=True),
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['album.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['youjiao_user.id'], ),
    sa.UniqueConstraint('user_id', 'role_id')
    )
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('nickname', sa.String(length=16), nullable=True),
    sa.Column('work_place_name', sa.String(length=255), nullable=True),
    sa.Column('avatar_qiniu_key', sa.String(length=200), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('gender', sa.Enum('male', 'female', name='gender'), nullable=True),
    sa.Column('career', sa.String(length=16), nullable=True),
    sa.Column('province', sa.String(length=16), nullable=True),
    sa.Column('city', sa.String(length=16), nullable=True),
    sa.Column('district', sa.String(length=16), nullable=True),
    sa.Column('street', sa.String(length=16), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['youjiao_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nickname')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    op.drop_table('roles_users')
    op.drop_table('photo')
    op.drop_table('page')
    op.drop_table('favor')
    op.drop_table('courseware')
    op.drop_table('comment')
    op.drop_table('activity')
    op.drop_table('youjiao_user')
    op.drop_table('video')
    op.drop_table('role')
    op.drop_table('book')
    op.drop_table('album')
    ### end Alembic commands ###
