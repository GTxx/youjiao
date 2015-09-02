# -*- coding: utf-8 -*-
from flask_restful import Resource, Api
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from marshmallow import ValidationError
from .models import User
from .utils import verify_password
user_api_bp = Blueprint('user_api_bp', __name__)
user_api = Api(user_api_bp)


class UserResource(Resource):
    pass



user_api.add_resource(UserResource, '/api/user')


from marshmallow import Schema, fields, validates_schema
from marshmallow.validate import Length

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
            raise ValidationError('password error')

    @validates_schema
    @check_fields_exist('password', 'password_confirm')
    def validate_password_and_confirm(self, data, password, password_confirm):
        if password != password_confirm:
            raise ValidationError('password != password_confirm')


# TODO: enable csrf when use session auth, disable csrf when token auth
@user_api_bp.route('/api/user/reset_password', methods=['POST'])
@login_required
def reset_password():
    # validate
    schema = ResetPasswordSchema()
    ResetPasswordSchema.validate
    # import ipdb; ipdb.set_trace()
    # TODO: supprot json and form input, or just support json
    # if request.content_type == 'application/json':
    #    get data from request.json
    # if request.content_type == 'form...'
    #   get data from form

    data, error = schema.load(request.form)
    # data, error = schema.load({'password': '1234'})
    if error:
        return jsonify(error), 400
    current_user.set_password(data['password'])
    # get data
    return jsonify(data)
