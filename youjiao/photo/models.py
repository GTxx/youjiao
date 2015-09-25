from youjiao.extensions import db
import sqlalchemy as sqla
from datetime import datetime
from youjiao.utils.database import CRUDMixin


class Photo(db.Model, CRUDMixin):
    id = sqla.Column(sqla.Integer, primary_key=True)
    create_time = sqla.Column(sqla.DateTime, default=datetime.utcnow)
    name = db.Column(sqla.String(50))
    qiniu_key = db.Column(sqla.String(200))
    album_id = db.Column(sqla.Integer, db.ForeignKey('album.id'))


class Album(db.Model, CRUDMixin):
    id = sqla.Column(sqla.Integer, primary_key=True)
    create_time = sqla.Column(sqla.DateTime, default=datetime.utcnow)
    name = sqla.Column(sqla.String(200))
    photos = db.relationship('Photo', backref='album')
