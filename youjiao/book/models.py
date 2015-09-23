# -*- coding: utf-8 -*-

from __future__ import absolute_import
from youjiao.extensions import db
from youjiao.utils.database import CRUDMixin
import sqlalchemy as sqla
from sqlalchemy.dialects.postgresql import ARRAY
from youjiao.user_util.models import Comment
from flask import url_for


class Book(db.Model, CRUDMixin):
    id = sqla.Column(sqla.Integer, primary_key=True)
    name = db.Column(sqla.String(50))
    chief_editor = db.Column(sqla.String(16))
    executive_editor = db.Column(sqla.String(16))
    publisher = db.Column(sqla.String(16))
    book_size = db.Column(sqla.Enum(u'16开', name='book_size'))
    level = db.Column(sqla.Enum(u'小班', u'中班', u'大班', name='level'))
    category = db.Column(sqla.Enum(u'幼教教材', u'幼教读物', name='book_category'))
    price = db.Column(sqla.Numeric(10, 2), default=30)
    publish = db.Column(sqla.Boolean, default=False)
    image_array = db.Column(ARRAY(sqla.String(255)))
    preview_array = db.Column(ARRAY(sqla.String(255)))

    @classmethod
    def read_book_top10(cls):
        return cls.query.filter_by(category=u'幼教读物').limit(10)

    @classmethod
    def teach_book_tol10(cls):
        return cls.query.filter_by(category=u'幼教教材').limit(10)

    @classmethod
    def top10(cls):
        return cls.query.limit(10)

    @property
    def cover(self):
        if len(self.image_array) == 0:
            return 'http://7xj2zj.com2.z0.glb.qiniucdn.com/1.jpg'
        else:
            return self.image_array[0]

    @property
    def link(self):
        return url_for('book_view.book_detail', book_id=self.id)

    def comment(self, page=0):
        return Comment.query.filter_by(comment_obj_type='book').filter_by(comment_obj_id=self.id)


