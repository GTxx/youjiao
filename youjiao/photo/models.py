from youjiao.extensions import db
import sqlalchemy as sqla
from datetime import datetime
from youjiao.utils.database import CRUDMixin
from flask import current_app
from youjiao.extensions import qiniu


class Photo(db.Model, CRUDMixin):
    id = sqla.Column(sqla.Integer, primary_key=True)
    create_time = sqla.Column(sqla.DateTime, default=datetime.utcnow)
    name = db.Column(sqla.String(50))
    qiniu_key = db.Column(sqla.String(200))
    album_id = db.Column(sqla.Integer, db.ForeignKey('album.id'))

    def __repr__(self):
        return u'<Photo: {}>'.format(self.name)

    @property
    def url(self):
        return u'{}/{}'.format(qiniu.PUBLIC_CDN_DOMAIN, self.qiniu_key)

    @property
    def thumbnail(self):
        return u'{}?imageView/2/w/150'.format(self.url)

    @property
    def with_watermark(self):
        return ''

    @property
    def with_watermark_thumbnail(self):
        return ''


class Album(db.Model, CRUDMixin):
    id = sqla.Column(sqla.Integer, primary_key=True)
    create_time = sqla.Column(sqla.DateTime, default=datetime.utcnow)
    name = sqla.Column(sqla.String(200))
    photos = db.relationship('Photo', backref='album')

    def __repr__(self):
        return u'<Album: {}>'.format(self.name)
