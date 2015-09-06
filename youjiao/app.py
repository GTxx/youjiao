from __future__ import absolute_import

from flask_admin import Admin
from flask import Flask, render_template
from flask_wtf import CsrfProtect
from flask_babel import Babel
from flask_login import LoginManager
from flask_principal import Principal, identity_loaded
from flask_debugtoolbar import DebugToolbarExtension


from .config import Config
from .content.models import Activity, Page
from .user.models import User
from .user.utils import load_user
from .extensions import db, limiter, admin
from .utils.csrf import check_csrf

from .user.admin import UserAdmin
from .user.utils import _on_identity_loaded
from .user.views import user_bp
from .user.api import user_api_bp
from .content.admin import ActivityAdmin, PageAdmin
from .content.views import content_bp


# Flask views
def index():
    return render_template('home/home.html', current_page='home')


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.debug = True

    # flask_sqlalchemy
    db.init_app(app)

    # flask_debug
    DebugToolbarExtension(app)

    # flask_login
    login_manager = LoginManager(app)
    login_manager.user_loader(load_user)

    # flask_principal
    Principal(app)
    identity_loaded.connect_via(app)(_on_identity_loaded)

    # flask_wtf csrf
    csrf = CsrfProtect()
    csrf.init_app(app)
    app.before_request(check_csrf(csrf))

    # flask_babel
    Babel(app)

    # flask_limiter
    limiter.init_app(app)

    # flask_admin
    admin.init_app(app)

    # register blueprint
    app.register_blueprint(content_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(user_api_bp)

    # register home page
    app.add_url_rule('/', 'index', index)

    return app
