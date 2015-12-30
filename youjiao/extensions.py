# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_admin import Admin
from flask_script import Manager
from youjiao.yj_admin.views import YJHomeView
from flask_redis import FlaskRedis
from .flask_qiniu import FlaskQiniu

db = SQLAlchemy()
USER_TABLE_NAME = 'youjiao_user' # table name 'user' is used in postgresql
USER_TABLE_USER_ID = '{}.id'.format(USER_TABLE_NAME)

limiter = Limiter()

admin = Admin(index_view=YJHomeView(name=u'数据面板'), name=u'幼教后台', template_mode='bootstrap3')

redis_cli = FlaskRedis(strict=True)

flask_qiniu = FlaskQiniu()

manager = Manager()
