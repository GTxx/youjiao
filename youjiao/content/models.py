# -*- coding: utf-8 -*-
from __future__ import absolute_import

from datetime import datetime
import sqlalchemy as sqla
from sqlalchemy.dialects.postgresql import JSON
from youjiao.extensions import db, USER_TABLE_USER_ID
from youjiao.utils.database import CRUDMixin
from flask import url_for


class Activity(db.Model, CRUDMixin):
    id = db.Column(sqla.Integer, primary_key=True)
    create_time = db.Column(sqla.DateTime, default=datetime.utcnow)
    update_time = db.Column(sqla.DateTime, onupdate=datetime.utcnow)
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

    @classmethod
    def weekly_popular_top10(cls):
        return cls.query.limit(10).all()

    @property
    def link(self):
        return url_for('activity_content.activity_view', id=self.id)


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now)
    title = db.Column(db.String(255))
    html = db.Column(db.Text)
    status = db.Column(db.String(2), default='1')
    user_id = db.Column(db.Integer, db.ForeignKey(USER_TABLE_USER_ID))


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publish = db.Column(sqla.Boolean, default=False)
    create_time = db.Column(sqla.DateTime, default=datetime.utcnow)
    update_time = db.Column(sqla.DateTime, default=datetime.utcnow)
    name = db.Column(sqla.String(200))
    url = db.Column(sqla.String(200))
    category = db.Column(
        sqla.Enum(u'优秀课堂', u'优秀讲座', u'其他视频', u'产品使用培训', u'师资培训视频',
                  name='video_category'))
    content = db.Column(JSON)

    @classmethod
    def get_category(cls, category):
        return cls.query.filter_by(category=category)

    @property
    def link(self):
        return url_for('activity_content.video_detail', video_id=self.id)
