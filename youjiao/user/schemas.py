from marshmallow import Schema, fields
from marshmallow.validate import Length, OneOf


class UserSchema(Schema):
    # TODO: complete schema condition
    id = fields.Integer()
    name = fields.String(required=True, validate=Length(5, 30))
    email = fields.Email()
    phone_number = fields.String()


class UserProfileSchema(Schema):
    work_place_name = fields.String(validate=Length(0, 30))
    # avatar_qiniu_key = db.Column(sqla.String(200), default='default_avatar.png')
    birthday = fields.Date()
    gender = fields.String(validate=OneOf('male', 'female'))
    career = fields.String(validate=Length(1, 16))
    province = fields.String(validate=Length(1, 16))
    city = fields.String(validate=Length(1, 16))
    district = fields.String(validate=Length(1, 16))
    street = fields.String(validate=Length(1, 16))
