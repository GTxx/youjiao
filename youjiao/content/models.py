# -*- coding: utf-8 -*-
from __future__ import absolute_import
from datetime import datetime
import collections
import sqlalchemy as sqla
from sqlalchemy import String, Unicode
from sqlalchemy.dialects.postgresql import JSON, ARRAY
from youjiao.extensions import db, USER_TABLE_USER_ID
from youjiao.utils.database import CRUDMixin, CreateUpdateTimeMixin
from flask import url_for


class Activity(CRUDMixin, CreateUpdateTimeMixin, db.Model):
    id = db.Column(sqla.Integer, primary_key=True)
    # create_time = db.Column(sqla.DateTime, default=datetime.utcnow)
    # update_time = db.Column(sqla.DateTime, onupdate=datetime.utcnow)
    title = db.Column(db.String(255))
    origin = db.Column(db.String(255), default='')
    html = db.Column(db.Text)
    # status = db.Column(sqla.Boolean, default=False)
    publish = db.Column(sqla.Boolean, default=False)
    category = db.Column(
        sqla.Enum('policy', 'news', 'events', 'research', 'activity',
                  'achievement', name='category'),
        default='policy')
    user_id = db.Column(db.Integer, db.ForeignKey(USER_TABLE_USER_ID))
    user = db.relationship('User')

    @classmethod
    def weekly_popular_top10(cls):
        return cls.query.limit(10).all()

    @property
    def link(self):
        return url_for('activity_content.activity_view', id=self.id)

    @property
    def edit_link(self):
        redirect_url = url_for('activity_content.activity_view', id=self.id)
        return '/admin/activity/edit?url={}&id={}'.format(redirect_url, self.id)


class Page(CRUDMixin, CreateUpdateTimeMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # create_time = db.Column(db.DateTime, default=datetime.now)
    # update_time = db.Column(db.DateTime, onupdate=datetime.now)
    title = db.Column(db.String(255))
    html = db.Column(db.Text)
    status = db.Column(db.String(2), default='1')
    user_id = db.Column(db.Integer, db.ForeignKey(USER_TABLE_USER_ID))

    @property
    def edit_link(self):
        redirect_url = url_for('activity_content.pages', page_title=self.title)
        return '/admin/page/edit?url={}&id={}'.format(redirect_url, self.id)


class Slider(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(sqla.String(200))
    image_list = db.Column(JSON)

    @classmethod
    def home_slider(cls):
        slider = cls.query.filter_by(name=u'主页').first()
        if slider:
            return slider.image_list
        else:
            return [
                {'image': "http://7xj2zj.com2.z0.glb.qiniucdn.com/11.jpg",
                 'link': '/book/1'},
                {'image': "http://7xj2zj.com2.z0.glb.qiniucdn.com/12.jpg",
                 'link': '/book/2'},
                {'image': "http://7xj2zj.com2.z0.glb.qiniucdn.com/13.jpg",
                 'link': '/book/3'},
                {'image': "http://7xj2zj.com2.z0.glb.qiniucdn.com/14.jpg",
                 'link': '/book/4'},
                {'image': "http://7xj2zj.com2.z0.glb.qiniucdn.com/15.jpg",
                 'link': '/book/5'},
            ]

    @classmethod
    def book_slider(cls):
        slider = cls.query.filter_by(name=u'教材').first()
        if slider:
            return slider.image_list
        else:
            return [
                {'image': "http://7xn3in.com2.z0.glb.qiniucdn.com/banner1.jpg",
                 'link': '/book/1'},
                {'image': "http://7xn3in.com2.z0.glb.qiniucdn.com/banner2.jpg",
                 'link': '/book/1'},
                {'image': "http://7xn3in.com2.z0.glb.qiniucdn.com/banner3.jpg",
                 'link': '/book/1'},
                {'image': "http://7xn3in.com2.z0.glb.qiniucdn.com/banner4.jpg",
                 'link': '/book/1'},
                {'image': "http://7xn3in.com2.z0.glb.qiniucdn.com/banner5.jpg",
                 'link': '/book/1'},
            ]

    @classmethod
    def courseware_slider(cls):
        slider = cls.query.filter_by(name=u'课件').first()
        if slider:
            return slider.image_list
        else:
            return [
                {
                    "image": "http://7xn3in.com2.z0.glb.qiniucdn.com/e7a9887b-2a77-4e52-85c9-0e914880f795/anner1.jpg",
                    "link": "#"},
                {
                    "image": "http://7xn3in.com2.z0.glb.qiniucdn.com/f3603d5f-dbab-407c-baa0-6702fd4d708f/anner2.jpg",
                    "link": "#"},
                {
                    "image": "http://7xn3in.com2.z0.glb.qiniucdn.com/e9fb3150-4b19-48e4-adcb-35eea39bd818/banner3.jpg",
                    "link": "#"},
                {
                    "image": "http://7xn3in.com2.z0.glb.qiniucdn.com/2ba3c115-9203-4f1e-8885-15093041a53d/banner4.jpg",
                    "link": "#"},
                {
                    "image": "http://7xn3in.com2.z0.glb.qiniucdn.com/52bc0da0-6bcc-49f8-a6ee-cb978376e7e3/banner5.jpg",
                    "link": "#"}
            ]


class ContentList(CRUDMixin, CreateUpdateTimeMixin, db.Model):
    ''' 页面出现一些对象, 要求有name这个字段,  保存成一个array(list)放在json中'''
    id = db.Column(sqla.Integer, primary_key=True)
    position = db.Column(sqla.String(200))
    content = db.Column(JSON)

    BOOK = u'幼教教材'
    COURSEWARE = u'幼教课件'
    ONLINECOURSE = u'幼教网课'

    # position enum
    HOME_BOOK = u'首页 教材推荐'
    HOME_COURSEWARE = u'首页 课件推荐'
    HOME_RECOMMEND = u'首页推荐'

    from youjiao.teach_material.models import Book, Courseware
    from youjiao.onlinecourse.models import OnlineCourse
    name_model = {
        BOOK: Book, COURSEWARE: Courseware, ONLINECOURSE: OnlineCourse
    }
    model_name = {v: k for k, v in name_model.items()}

    @staticmethod
    def obj_to_dict(obj):
        obj_dict_list = [
            {'id': obj.id, 'name': obj.__repr__(), 'model_name': name}
            for name, model in ContentList.name_model.items()
            if isinstance(obj, model)]
        if len(obj_dict_list) == 0:
            raise Exception('can not handle obj: {}'.format(obj))
        else:
            return obj_dict_list[0]

    @staticmethod
    def dict_to_obj(dct):
        obj_model = ContentList.name_model[dct['model_name']]
        obj_id = dct['id']
        return obj_model.query.get(obj_id)

    @classmethod
    def add_obj_to_position(cls, obj_list, position_name):
        if position_name not in [cls.HOME_BOOK, cls.HOME_COURSEWARE,
                                 cls.HOME_RECOMMEND]:
            raise Exception('{} is invalid'.format(position_name))
        contentlist = cls.query.filter(cls.position==position_name).first()
        if not contentlist:
            contentlist = cls(position=position_name, content=[])
            contentlist.save()

        if not isinstance(obj_list, collections.Iterable):
            obj_list = [obj_list, ]
        added_content = [cls.obj_to_dict(obj) for obj in obj_list]
        contentlist.content = contentlist.content + added_content
        contentlist.save()
        return contentlist

    @property
    def ids(self):
        return [i.get('id') for i in self.content]

    @property
    def obj_list(self):
        return [self.dict_to_obj(i) for i in self.content]
