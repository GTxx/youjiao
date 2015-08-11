from __future__ import absolute_import
from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import filters
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from wtforms import TextAreaField
from wtforms.widgets import TextArea
from config import Config
from flask_security import Security, login_required
from flask_login import login_required
from models.user import user_datastore


# Create application
app = Flask(__name__)

app.config.from_object(Config)
from models import db
from models.activity import Activity
from models.user import User

db.init_app(app)
security = Security(app, user_datastore)


# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'


@app.route('/activity/<id>')
@login_required
def activity_view(id):
    obj = Activity.query.get(id)
    return render_template('activity.html', activity=obj)


@app.route('/activity')
def activity_list():
    query = Activity.query.all()
    return render_template('activity_list.html', activity_list=query)


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
    column_list = ('title', 'create_time', 'update_time', )
    column_searchable_list = ('title', )
    form_excluded_columns = ('create_time', 'update_time')

class UserAdmin(sqla.ModelView):
    column_list = ('name', 'email', 'last_login', 'is_admin')
    column_searchable_list = ('name', 'email')
    form_excluded_columns = ('create_time', 'last_login')

admin = Admin(app)
admin.add_view(ActivityAdmin(Activity, db.session))
admin.add_view(UserAdmin(User, db.session))
