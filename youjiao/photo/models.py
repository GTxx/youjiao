from youjiao.extensions import db
import sqlalchemy as sqla
from datetime import datetime
from youjiao.utils.database import CRUDMixin
from flask import current_app


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
        qiniu_cdn = current_app.config.get('QINIU_CDN_DOMAIN')
        return u'{}/{}'.format(qiniu_cdn, self.qiniu_key)

    @property
    def thumbnail(self):
        return u'{}?imageView/2/w/150'.format(self.url)


class Album(db.Model, CRUDMixin):
    id = sqla.Column(sqla.Integer, primary_key=True)
    create_time = sqla.Column(sqla.DateTime, default=datetime.utcnow)
    name = sqla.Column(sqla.String(200))
    photos = db.relationship('Photo', backref='album')

    def __repr__(self):
        return u'<Album: {}>'.format(self.name)
