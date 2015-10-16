# -*- coding: utf-8 -*-

from youjiao.extensions import db
from youjiao.utils.database import CRUDMixin
import sqlalchemy as sqla
from sqlalchemy.dialects.postgresql import JSON


class MediaMixin(object):
    name = db.Column(sqla.String(200))
    qiniu_key = db.Column(sqla.String(200), unique=True)
    # 处理结果
    media_process = db.Column(JSON) # 不能用process和meta，因为wtform 有这两个属性
    # 媒体资源的元信息
    media_meta = db.Column(JSON)


class Video(CRUDMixin, MediaMixin, db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)


class Audio(CRUDMixin, MediaMixin, db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)


class Document(CRUDMixin, MediaMixin, db.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
