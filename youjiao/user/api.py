# -*- coding: utf-8 -*-
from flask_restful import Resource, Api
from flask import Blueprint, request, jsonify, abort
from flask_login import login_required, current_user

from .models import User, UserProfile
from .schemas import UserSchema, UserProfileSchema, ResetPasswordSchema
user_api_bp = Blueprint('user_api_bp', __name__)
user_api = Api(user_api_bp)


class UserResource(Resource):
    # TODO: check permission first

    def get(self, user_id):
        import ipdb; ipdb.set_trace()
        # TODO: replce it with permission check
        # if current_user.id != user_id:
        #     abort(403)
        user = User.query.get(user_id)
        res = UserSchema().dump(user)
        return res.data

    def patch(self, user_id):
        # partial update
        schema = UserSchema()
        user = User.query.get(user_id)
        # get data from request
        data = request.get_json()
        complete_data = data.copy()
        for field_name in schema.fields.keys():
            if not data.has_key(field_name) and getattr(user, field_name):
                complete_data[field_name] = getattr(user, field_name)
        res = schema.load(complete_data)
        # update user
        if res.errors:
            return res.errors, 400
        user.query.update(data)
        user.save()
        return schema.dump(user).data



class UserProfileResource(Resource):
    def get(self, profile_id):
        user_profile = UserProfile.query.get(profile_id)
        res = UserProfileSchema().dump(user_profile)
        return res.data

    def patch(self, profile_id):
        schema = UserProfileSchema()
        user_profile = UserProfile.query.get(profile_id)
        data = request.get_json()
        complete_data = data.copy()
        for field_name in schema.fields.keys():
            field_value = getattr(user_profile, field_name)
            if not data.has_key(field_name) and field_value:
                complete_data[field_name] = field_value
        res = schema.load(complete_data)
        # update user
        if res.errors:
            return res.errors, 400
        import ipdb; ipdb.set_trace()
        user_profile.query.update(res.data)
        user_profile.save()
        return schema.dump(user_profile).data


user_api.add_resource(UserResource, '/api/user/<int:user_id>')
user_api.add_resource(UserProfileResource, '/api/user_profile/<int:profile_id>')


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



