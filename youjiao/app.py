# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask_admin import Admin
from flask import Flask, render_template
from flask_wtf import CsrfProtect
from flask_babelex import Babel
from flask_login import LoginManager
from flask_principal import Principal, identity_loaded
from flask_debugtoolbar import DebugToolbarExtension

# from .config import Config
from . import config as youjiao_config
from .user.utils import load_user
from .user.subscribers import connect as user_connect
from .extensions import db, limiter, admin, redis_cli, flask_qiniu, jwt
from .utils.csrf import check_csrf

# user
from .user.models import User
from .user.admin import UserAdmin
from .user.utils import _on_identity_loaded
from .user.views import user_bp
from .user.api import user_api_bp

# content
from .content.admin import ActivityAdmin
from .content.models import Activity, Slider, ContentList
from .content.views import content_bp

# book
from .teach_material.admin import BookAdmin
from .teach_material.models import Book, Courseware
from .teach_material.views import book_bp
from .teach_material.api import book_api_bp

# user util
from .user_util.models import Favor
from .user_util.api import user_util_api_bp

# photo
from .photo.models import Photo, Album
from .photo.admin import AlbumAdmin

# yj_media
from .yj_media.admin import VideoAdmin
from .yj_media.models import Video, Audio, Document
from .yj_media.views import media_bp

# online course
from .onlinecourse.models import OnlineCourse
from .onlinecourse.views import online_course_bp
from .onlinecourse.admin import OnlineCourseAdmin

import os
import json


# Flask views
def index():
    # import ipdb; ipdb.set_trace()
    book_content_list = ContentList.query.filter(
        ContentList.position==ContentList.HOME_BOOK).first()
    if book_content_list:
        book_list = book_content_list.obj_list
    else:
        book_list = Book.top10()

    courseware_content_list = ContentList.query.filter(
        ContentList.position==ContentList.HOME_COURSEWARE).first()
    if courseware_content_list:
        courseware_list = courseware_content_list.obj_list
    else:
        courseware_list = Courseware.top10()

    onlinecourse_content_list = ContentList.query.filter(
        ContentList.position==u'首页视频').first()
    if onlinecourse_content_list:
        onlinecourse_list = onlinecourse_content_list.obj_list
    else:
        onlinecourse_list = OnlineCourse.top10()
    return render_template('home/home.html', current_page='home',
                           Book=Book, Courseware=Courseware,
                           slider=Slider.home_slider(),
                           book_list=book_list, courseware_list=courseware_list,
                           onlinecourse_list=onlinecourse_list)


def create_app():
    app = Flask(__name__)
    app.config.from_object(youjiao_config)

    # flask_sqlalchemy
    # import ipdb; ipdb.set_trace()
    db.init_app(app)

    # flask_redis
    redis_cli.init_app(app)



    # flask_debug
    if app.config.get('DEBUG'):
        DebugToolbarExtension(app)

    # flask_login
    login_manager = LoginManager(app)
    login_manager.user_loader(load_user)
    login_manager.login_view = 'user_view.login'

    # flask_jwt
    jwt.init_app(app)

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

    # flask_qiniu
    flask_qiniu.init_app(app)

    # flask_admin
    admin.init_app(app)

    # register blueprint
    app.register_blueprint(content_bp)

    app.register_blueprint(user_bp)

    app.register_blueprint(user_api_bp)

    # import ipdb; ipdb.set_trace()
    app.register_blueprint(book_bp)
    app.register_blueprint(book_api_bp)
    app.register_blueprint(user_util_api_bp)
    app.register_blueprint(media_bp)
    app.register_blueprint(online_course_bp)

    # register subscriber
    user_connect(app)

    # register home page
    app.add_url_rule('/', 'index', index)

    with open(os.path.join(os.getcwd(), 'youjiao/static/assets.json.py'), 'r') as assets:
        app.assets = json.load(assets)

    return app
