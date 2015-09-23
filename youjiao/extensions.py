from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_admin import Admin
from flask_restful import Api
from flask_redis import FlaskRedis

db = SQLAlchemy()
USER_TABLE_NAME = 'youjiao_user' # table name 'user' is used in postgresql
USER_TABLE_USER_ID = '{}.id'.format(USER_TABLE_NAME)

limiter = Limiter()

admin = Admin(template_mode='bootstrap3')

redis_cli = FlaskRedis(strict=True)
