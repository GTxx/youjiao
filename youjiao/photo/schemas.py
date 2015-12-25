from marshmallow import Schema, fields
from .models import Photo, Album


class PhotoSchema(Schema):
    id = fields.Int(dump_only=True)
    create_time = fields.DateTime(dump_only=True)
    name = fields.String()
    qiniu_key = fields.String()
    album_id = fields.Int()

    url = fields.String(dump_only=True)


class PaginatePhotoSchema(Schema):
    results = fields.Nested(PhotoSchema, many=True)
    count = fields.Int()
    next = fields.Int()
    prev = fields.Int()


class AlbumSchema(Schema):
    id = fields.Int(dump_only=True)
    create_time = fields.DateTime(dump_only=True)
    name = fields.String()