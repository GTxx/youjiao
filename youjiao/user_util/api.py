from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from .schemas import FavorSchema
from .models import Favor


user_util_api_bp = Blueprint('user_util_api_bp', __name__)

@user_util_api_bp.route('/api/favor', methods=['POST'])
@login_required
def favor():
    # validate
    schema = FavorSchema()
    # import ipdb; ipdb.set_trace()
    # TODO: supprot json and form input, or just support json
    # if request.content_type == 'application/json':
    #    get data from request.json
    # if request.content_type == 'form...'
    #   get data from form

    # import ipdb; ipdb.set_trace()
    json_data = request.get_json()
    json_data.update({'user_id': current_user.id})
    data, error = schema.load(request.get_json())

    # data, error = schema.load({'password': '1234'})
    if error:
        return jsonify(error), 400
    from sqlalchemy import exists, and_
    from youjiao.extensions import db
    obj_id = data.get('obj_id')
    obj_type = data.get('obj_type')
    ret = db.session.query(exists().where(
        and_(Favor.obj_id==obj_id,
             Favor.obj_type==obj_type,
             Favor.user_id==current_user.id))).scalar()
    if not ret:
        favor = Favor(**data)
        favor.save()
    return jsonify(data), 201

