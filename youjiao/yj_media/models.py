# -*- coding: utf-8 -*-

from youjiao.extensions import db
import sqlalchemy as sqla
from sqlalchemy.dialects.postgresql import JSON


class Video(db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    qiniu_key = db.Column(sqla.String(200), unique=True)
    json = db.Column(JSON)


class Audio(db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    qiniu_key = db.Column(sqla.String(200), unique=True)
    json = db.Column(JSON)


class Document(db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    qiniu_key = db.Column(sqla.String(200), unique=True)
    json = db.Column(JSON)
