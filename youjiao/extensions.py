from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_admin import Admin
from flask_restful import Api
from flask_redis import FlaskRedis

db = SQLAlchemy()

limiter = Limiter()

admin = Admin(template_mode='bootstrap3')

redis_cli = FlaskRedis(strict=True)
