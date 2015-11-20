# -*- coding: utf-8 -*-

from __future__ import absolute_import
from youjiao.extensions import db
from youjiao.utils.database import CRUDMixin
import sqlalchemy as sqla
from sqlalchemy import not_
from sqlalchemy.dialects.postgresql import ARRAY, JSON
from youjiao.user_util.models import Comment
from flask import url_for
from youjiao.yj_media.models import Document


class Book(db.Model, CRUDMixin):
    id = sqla.Column(sqla.Integer, primary_key=True)
    name = db.Column(sqla.String(50))
    chief_editor = db.Column(sqla.String(16))
    executive_editor = db.Column(sqla.String(16))
    publisher = db.Column(sqla.String(16))
    book_size = db.Column(sqla.Enum(u'16开', name='book_size'))
    level = db.Column(sqla.Enum(u'幼小衔接班', u'小班', u'中班', u'大班', name='level'))
    category = db.Column(sqla.Enum(u'幼教教材', u'幼教读物', name='book_category'))
    price = db.Column(sqla.Numeric(10, 2), default=30)
    publish = db.Column(sqla.Boolean, default=False)
    image_array = db.Column(ARRAY(sqla.String(255)))
    preview_array = db.Column(ARRAY(sqla.String(255)))

    coursewares = db.relationship('Courseware', backref='book')

    @classmethod
    def read_book_top10(cls):
        return cls.query.filter(cls.category==u'幼教读物',
                                cls.publish==True).limit(10)

    @classmethod
    def teach_book_tol10(cls):
        return cls.query.filter(cls.category==u'幼教教材',
                                cls.publish==True).limit(10)

    @classmethod
    def top10(cls):
        return cls.query.filter(cls.publish==True, not_(cls.name.contains(u'家园'))).limit(10)

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

    @property
    def edit_link(self):
        redirect_url = url_for('book_view.book_detail', book_id=self.id)
        return '/admin/book/edit?url={}&id={}'.format(redirect_url, self.id)


class Courseware(db.Model, CRUDMixin):
    """
    content = [
        {'key': 'qinghuaci.mp4', 'name': '青花瓷i', 'type': 'video'}
        {'key': 'qinghuaci.mp3', 'name': '青花瓷i', 'type': 'audio'}
        {'key': 'qinghuaci.pdf', 'name': '青花瓷i', 'type': 'document'}
    ]
    """
    id = db.Column(sqla.Integer, primary_key=True)
    name = db.Column(sqla.String(200))
    book_id = db.Column(sqla.Integer, db.ForeignKey('book.id'))
    content = db.Column(JSON)
    publish = db.Column(sqla.Boolean, default=False)

    @classmethod
    def top10(cls):
        return cls.query.filter(cls.publish==True).limit(10)

    def comment(self):
        return Comment.query.filter_by(
            comment_obj_type='courseware').filter_by(comment_obj_id=self.id)

    @property
    def link(self):
        return url_for('book_view.courseware_detail', courseware_id=self.id)

    @property
    def related_courseware(self):
        return Courseware.query.join(Book).filter(
            Book.id==self.book_id, Courseware.id!=self.id,
            Courseware.publish==True).all()

    @property
    def edit_link(self):
        redirect_url = url_for('book_view.courseware_detail', courseware_id=self.id)
        return '/admin/courseware/edit?url={}&id={}'.format(redirect_url, self.id)

    def get_media_list(self, media_type):
        if not self.content:
            return []
        return [media for media in self.content if media.get('type')==media_type]

    @property
    def document_list(self):
        documents = self.get_media_list('document')
        res = []
        for document in documents:
            document_obj = Document.query.filter_by(qiniu_key=document.get('key').strip('.pdf')).first()
            img_list = document_obj.pdf_pic
            document.update({'img_list': img_list})
            res.append(document)
        return res

    @property
    def audio_list(self):
        return self.get_media_list('audio')

    @property
    def video_list(self):
        return self.get_media_list('video')

    @property
    def cover(self):
        if self.book:
            return self.book.cover
        return 'http://7xn3in.com2.z0.glb.qiniucdn.com/imgo.jpg'
