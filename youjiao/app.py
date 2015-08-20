from __future__ import absolute_import

from flask_admin import Admin
from flask import Flask, render_template
from flask_security import Security, login_required

from .config import Config
from .content.models import Activity, Page
from .user.models import user_datastore,User
from .extensions import db

from .user.admin import UserAdmin
from .user.views import user_bp
from .content.admin import ActivityAdmin, PageAdmin
from .content.views import content_bp


# Flask views
@login_required
def index():
    return render_template('home/home.html')


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    security = Security(app, user_datastore)

    admin = Admin(app)
    admin.add_view(ActivityAdmin(Activity, db.session))
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(PageAdmin(Page, db.session))
    # import ipdb; ipdb.set_trace()
    app.register_blueprint(content_bp)
    app.register_blueprint(user_bp)
    app.add_url_rule('/', 'index', index)
    return app
