# -*- coding: utf-8 -*-

from __future__ import absolute_import
from youjiao.extensions import db, redis_cli
from youjiao.utils.database import CRUDMixin
import sqlalchemy as sqla
from sqlalchemy import not_
from sqlalchemy.dialects.postgresql import ARRAY, JSON, ENUM
from youjiao.user_util.models import Comment
from flask import url_for
from youjiao.yj_media.models import Document


class Book(db.Model, CRUDMixin):
    id = sqla.Column(sqla.Integer, primary_key=True)
    name = db.Column(sqla.String(50))
    chief_editor = db.Column(sqla.String(16))
    executive_editor = db.Column(sqla.String(16))
    publisher = db.Column(sqla.String(16))

    book_size_list = [u'16开',]
    book_size_enum = sqla.Enum(*book_size_list, name='book_size')
    book_size = db.Column(book_size_enum)

    level_list = [u'幼小衔接班', u'小班', u'中班', u'大班']
    level_enum = sqla.Enum(*level_list, name='level')
    level = db.Column(level_enum)

    category_list = [u'幼教教材', u'幼教读物']
    category_enum = sqla.Enum(*category_list, name='book category')
    category = db.Column(category_enum)

    price = db.Column(sqla.Numeric(10, 2), default=30)
    publish = db.Column(sqla.Boolean, default=False)
    image_array = db.Column(ARRAY(sqla.String(255)))
    preview_array = db.Column(ARRAY(sqla.String(255)))

    coursewares = db.relationship('Courseware', backref='book')

    def __repr__(self):
        uni = u'<图书: {},{}>'.format(self.name, self.level)
        return uni.encode('utf-8')

    def __unicode__(self):
        uni = u'<图书: {},{}>'.format(self.name, self.level)
        return uni

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
            return 'http://7xn3in.com2.z0.glb.qiniucdn.com/logo-big.jpg'
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

    def add_user_visit_recent(self, user):
        key = user.book_visit_recent_key
        redis_cli.lpush(key, self.id)
        redis_cli.ltrim(key, 0, 8)


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
    cover_img_url = db.Column(sqla.String(200))

    level_list = Book.level_list
    level_enum = ENUM(*level_list, name='courseware level', create_type=False)
    level = sqla.Column(level_enum)

    def __repr__(self):
        uni = u'<课件: {}>'.format(self.name)
        return uni.encode('utf-8')

    def __unicode__(self):
        uni = u'<课件: {}>'.format(self.name)
        return uni
    
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
            Book.id == self.book_id, Courseware.id != self.id,
            Courseware.publish == True).all()

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
        if self.cover_img_url:
            return self.cover_img_url
        if self.book:
            return self.book.cover
        return 'http://7xn3in.com2.z0.glb.qiniucdn.com/logo-big.jpg'

    def add_user_visit_recent(self, user):
        key = user.courseware_visit_recent_key
        redis_cli.lpush(key, self.id)
        redis_cli.ltrim(key, 0, 8)
