# -*- coding: utf-8 -*-

from youjiao.extensions import db
import sqlalchemy as sqla
from datetime import datetime


class Comment(db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    create_time = db.Column(sqla.DateTime, default=datetime.utcnow)
    user_id = db.Column(sqla.Integer, db.ForeignKey('user.id'))
    # 评论对象id
    comment_obj_id = db.Column(sqla.Integer)
    # 评论对象类型
    comment_obj_type = db.Column(sqla.Enum('book', name='comment_obj_type'))
    content = db.Column(sqla.String(140))


class Like(db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    create_time = db.Column(sqla.DateTime, default=datetime.utcnow)

    user_id = db.Column(sqla.Integer, db.ForeignKey('user.id'))
    # 评论对象id
    like_obj_id = db.Column(sqla.Integer, db.ForeignKey('book.id'))
    # 评论对象类型
    like_obj_type = db.Column(sqla.Enum('book', name='like_obj_type'))
