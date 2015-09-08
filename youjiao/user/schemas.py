# -*- coding: utf-8 -*-
from marshmallow import ValidationError, Schema, fields, validates_schema
from marshmallow.validate import Length, OneOf
from flask_login import current_user
from .utils import verify_password


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


def check_fields_exist(*fields):
    '''检查需要用到的field是否存在'''
    def decorator(validate_fn):
        def wrap(self, data):
            # import ipdb; ipdb.set_trace()
            field_value_list = []
            for field in fields:
                field_value = data.get(field)
                if not data.get(field):
                    # 如果这个field在之前就被过滤掉了，就跳过该validate_fn
                    return
                field_value_list.append(field_value)
            return validate_fn(self, data, *field_value_list)
        return wrap
    return decorator


class ResetPasswordSchema(Schema):
    password = fields.String(required=True, validate=Length(6, 30))
    password_confirm = fields.String(required=True, validate=Length(6, 30))
    old_password = fields.String(required=True, validate=Length(6, 30))

    @validates_schema
    @check_fields_exist('old_password')
    def validate_oldpassword(self, data, old_password):
        # TODO: if all fields is valid,  then execute this validate func
        if not verify_password(old_password, current_user.password):
            raise ValidationError(u'原始密码错误')

    @validates_schema
    @check_fields_exist('password', 'password_confirm')
    def validate_password_and_confirm(self, data, password, password_confirm):
        if password != password_confirm:
            raise ValidationError(u'两次输入的密码不一致')
