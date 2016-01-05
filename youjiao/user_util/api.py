from flask import Blueprint, request, jsonify
from flask.views import MethodView
from flask_login import login_required, current_user
from .schemas import FavorSchema
from .models import Favor, LeaveMessage
from youjiao.user.utils import auth_required


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


class LeaveMessageView(MethodView):
    decorators = [auth_required()]

    def post(self):
        from .schemas import LeaveMessageSchema
        data = request.get_json()
        data.update({'user_id': current_user.id})
        result = LeaveMessageSchema().load(data)
        if result.errors:
            return jsonify(result.errors), 400
        lm = LeaveMessage(**result.data)
        lm.save()
        return jsonify(result.data), 201


user_util_api_bp.add_url_rule('/api/leavemessage/', view_func=LeaveMessageView.as_view('leavemessage_view'))
