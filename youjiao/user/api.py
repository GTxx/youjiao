# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, abort
from flask_login import login_required, current_user

from .schemas import UserSchema, UserProfileSchema, ResetPasswordSchema
user_api_bp = Blueprint('user_api_bp', __name__)


# TODO: enable csrf when use session auth, disable csrf when token auth
@user_api_bp.route('/api/user/reset_password', methods=['POST'])
@login_required
def reset_password():
    # validate
    schema = ResetPasswordSchema()
    # import ipdb; ipdb.set_trace()
    # TODO: supprot json and form input, or just support json
    # if request.content_type == 'application/json':
    #    get data from request.json
    # if request.content_type == 'form...'
    #   get data from form

    data, error = schema.load(request.get_json())
    # data, error = schema.load({'password': '1234'})
    if error:
        return jsonify(error), 400
    current_user.set_password(data['password'])
    # get data
    return jsonify(data)


@user_api_bp.route('/api/user_info')
@login_required
def get_user_info():
    # get own info
    res = UserSchema().dump(current_user)
    return jsonify(res.data)
