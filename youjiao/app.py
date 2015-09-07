from __future__ import absolute_import

from flask_admin import Admin
from flask import Flask, render_template, session
from flask_security import Security, login_required
from flask_wtf import CsrfProtect
from flask_babel import Babel
from flask_login import LoginManager
from flask_principal import Principal, identity_loaded

from .config import Config
from .content.models import Activity, Page
from .user.models import User
from .user.utils import load_user
from .extensions import db

from .user.admin import UserAdmin
from .user.utils import _on_identity_loaded
from .user.views import user_bp
from .content.admin import ActivityAdmin, PageAdmin
from .content.views import content_bp


# Flask views
def index():
    return render_template('home/home.html', current_page='home')


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    # security = Security(app, user_datastore)
    # flask_login
    login_manager = LoginManager(app)
    login_manager.user_loader(load_user)

    # flask_principal
    Principal(app)
    identity_loaded.connect_via(app)(_on_identity_loaded)
    # flask csrf
    CsrfProtect(app)
    # flask_babel
    Babel(app)

    # flask_admin
    admin = Admin(app, template_mode='bootstrap3')
    admin.add_view(ActivityAdmin(Activity, db.session))
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(PageAdmin(Page, db.session))
    # import ipdb; ipdb.set_trace()
    # register blueprint
    app.register_blueprint(content_bp)
    app.register_blueprint(user_bp)

    app.add_url_rule('/', 'index', index)
    return app
