from __future__ import absolute_import

from flask_admin import Admin
from flask import Flask
from flask_security import Security

from .config import Config
from .activity.models import Activity
from .user.models import user_datastore,User
from .extensions import db

from .user.admin import UserAdmin
from .activity.admin import ActivityAdmin


# # Flask views
# @app.route('/')
# def index():
#     return '<a href="/admin/">Click me to get to Admin!</a>'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    security = Security(app, user_datastore)

    admin = Admin(app)
    admin.add_view(ActivityAdmin(Activity, db.session))
    admin.add_view(UserAdmin(User, db.session))
    return app


