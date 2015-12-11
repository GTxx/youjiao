# -*- coding: utf-8 -*-
from youjiao.extensions import db
from youjiao.utils.database import CRUDMixin, CreateUpdateTimeMixin
import sqlalchemy as sqla
from flask import url_for
from sqlalchemy.dialects.postgresql import JSON


class OnlineCourse(CRUDMixin, CreateUpdateTimeMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publish = db.Column(sqla.Boolean, default=False)
    name = db.Column(sqla.String(200))
    url = db.Column(sqla.String(200))
    category = db.Column(
        sqla.Enum(u'优秀课堂', u'优秀讲座', u'其他视频', u'产品使用培训', u'师资培训视频',
                  name='online_course_category'))
    content = db.Column(JSON)

    @classmethod
    def get_category(cls, category):
        return cls.query.filter_by(category=category, publish=True)

    @property
    def link(self):
        return url_for('online_course.video_detail', video_id=self.id)

    @property
    def cover(self):
        return 'http://7xn3in.com2.z0.glb.qiniucdn.com/logo-big.jpg'
