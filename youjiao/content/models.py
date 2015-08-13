from __future__ import absolute_import

from datetime import datetime
from youjiao.extensions import db


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now)
    title = db.Column(db.String(255))
    html = db.Column(db.Text)
    status = db.Column(db.String(2), default='1')
    category = db.Column(db.String(200), default='policy')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now)
    title = db.Column(db.String(255))
    html = db.Column(db.Text)
    status = db.Column(db.String(2), default='1')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
