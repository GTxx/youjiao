from __future__ import absolute_import

from datetime import datetime
import sqlalchemy as sqla
from youjiao.extensions import db
from youjiao.utils.database import CRUDMixin


class Activity(db.Model, CRUDMixin):
    id = db.Column(sqla.Integer, primary_key=True)
    create_time = db.Column(sqla.DateTime, default=datetime.now)
    update_time = db.Column(sqla.DateTime, onupdate=datetime.now)
    title = db.Column(db.String(255))
    html = db.Column(db.Text)
    status = db.Column(sqla.Boolean, default=False)
    category = db.Column(
        sqla.Enum('policy', 'news', 'events', 'research', 'activity',
                  'achievement', name='category'),
        default='policy')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

    @classmethod
    def weekly_popular_top10(cls):
        return cls.query.limit(10).all()


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now)
    title = db.Column(db.String(255))
    html = db.Column(db.Text)
    status = db.Column(db.String(2), default='1')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
