# -*- coding: utf-8 -*-

from youjiao.extensions import db, USER_TABLE_USER_ID
from youjiao.utils.database import CRUDMixin
import sqlalchemy as sqla
from sqlalchemy import UniqueConstraint
from datetime import datetime


class Comment(CRUDMixin, db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    create_time = db.Column(sqla.DateTime, default=datetime.utcnow)
    user_id = db.Column(sqla.Integer, db.ForeignKey(USER_TABLE_USER_ID))
    # 评论对象id
    comment_obj_id = db.Column(sqla.Integer)
    # 评论对象类型
    comment_obj_type = db.Column(sqla.Enum('book', 'courseware', name='comment_obj_type'))
    content = db.Column(sqla.String(140))


class Favor(CRUDMixin, db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    create_time = db.Column(sqla.DateTime, default=datetime.utcnow)

    user_id = db.Column(sqla.Integer, db.ForeignKey(USER_TABLE_USER_ID))
    # 喜爱对象id
    obj_id = db.Column(sqla.Integer, db.ForeignKey('book.id'))
    # 喜爱对象类型
    obj_type = db.Column(sqla.Enum('book', name='like_obj_type'))

    __table_args__ = (
        UniqueConstraint('user_id', 'obj_id', 'obj_type',
                         name='_user_favor_obj'),)

    @property
    def favor_model(self):
        from youjiao.teach_material.models import Book
        if self.obj_type == 'book':
            return Book
        else:
            return None

    @property
    def real_obj(self):
        model = self.favor_model
        return model.query.get(self.obj_id)
