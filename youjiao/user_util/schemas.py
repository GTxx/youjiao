from marshmallow import ValidationError, Schema, fields, validates_schema
from marshmallow.validate import Length, OneOf
from marshmallow.decorators import validates
from youjiao.user.models import User


class FavorSchema(Schema):
    user_id = fields.Integer(required=True)
    obj_id = fields.Integer(required=True)
    obj_type = fields.String(required=True)

    @validates('user_id')
    def validate_user_id_exist(self, data):
        if not User.query.get(data):
            raise ValidationError('user not found')

    @validates('obj_id')
    def validate_obj_id_exist(self, data):
        # TODO: validate if obj exist
        pass


class CommentSchema(Schema):
    id = fields.Integer()
    create_time = fields.DateTime()
    user_id = fields.Integer()
    comment_obj_id = fields.Integer()
    comment_obj_type = fields.String()
    content = fields.String()


class LeaveMessageSchema(Schema):
    user_id = fields.Integer()
    content = fields.String(validate=Length(min=1, max=1000), required=True)
