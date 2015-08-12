# -*- coding: utf-8 -*-
from __future__ import absolute_import
from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import filters, ModelView
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from wtforms import TextAreaField
from wtforms.widgets import TextArea
from config import Config


# Create application
app = Flask(__name__)

app.config.from_object(Config)
from models import db
from models.activity import Activity
from models.user import User
from models.page import Page

db.init_app(app)


# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'


@app.route('/activity/<id>')
def activity_view(id):
    obj = Activity.query.get(id)
    return render_template('activity/activity.html', activity=obj)


#
# @app.route('/activity')
# def activity_list():
#     query = Activity.query.all()
#     return render_template('activity_list.html', activity_list=query)


@app.route('/category/<category>/')
def category(category):
    posts = Activity.query.filter_by(category=category).filter_by(status=2).all()
    return render_template('activity/home.html', activity_list=posts)


@app.route('/account/login/')
def login():
    return render_template('account/login.html')


@app.route('/account/register/')
def register():
    return render_template('account/register.html')


@app.route('/index/')
def home():
    return render_template('home/home.html')


@app.route('/school/')
def school():
    return render_template('school/school.html')


@app.route('/school/lectures/')
def school_sub():
    return render_template('school/home.html')


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += 'ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class ActivityAdmin(sqla.ModelView):
    form_overrides = {
        'html': CKTextAreaField
    }
    create_template = 'ckeditor.html'
    edit_template = 'ckeditor.html'
    column_list = ('title', 'create_time', 'update_time', 'status', 'category')
    column_searchable_list = ('title',)
    form_excluded_columns = ('create_time', 'update_time')
    form_choices = {
        'category': [
            ('policy', u'幼教政策'),
            ('news', u'幼教新闻'),
        ],
        'status': [
            ('1', u'草稿'),
            ('2', u'发布'),
        ]
    }


class UserAdmin(sqla.ModelView):
    column_list = ('name', 'email', 'last_login', 'is_admin')
    column_searchable_list = ('name', 'email')
    form_excluded_columns = ('create_time', 'last_login')


class PageAdmin(sqla.ModelView):
    form_overrides = {
        'html': CKTextAreaField
    }
    create_template = 'ckeditor.html'
    edit_template = 'ckeditor.html'
    column_list = ('title', 'create_time', 'update_time', 'status')
    column_searchable_list = ('title',)
    form_excluded_columns = ('create_time', 'update_time')
    form_choices = {
        'status': [
            ('1', u'草稿'),
            ('2', u'发布'),
        ]
    }


admin = Admin(app)
admin.add_view(ActivityAdmin(Activity, db.session))
admin.add_view(UserAdmin(User, db.session))
admin.add_view(PageAdmin(Page, db.session))
