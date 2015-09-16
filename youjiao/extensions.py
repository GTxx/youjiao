from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_admin import Admin
from flask_restful import Api

db = SQLAlchemy()

limiter = Limiter()

admin = Admin(template_mode='bootstrap3')
