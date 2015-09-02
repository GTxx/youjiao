from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_restful import Api

db = SQLAlchemy()

limiter = Limiter()
