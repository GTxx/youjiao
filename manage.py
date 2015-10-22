# coding: utf-8
from flask_script import Manager
from flask_migrate import MigrateCommand
from flask import url_for
from youjiao.extensions import db, qiniu
from youjiao.app import create_app
from youjiao.user.models import User, Role, UserProfile
import os, json
import urlparse

# Used by app debug & livereload
PORT = 5000

app = create_app()
manager = Manager(app)


@manager.option('-p', '--port', dest='port', default=5000)
def run(port):
    """Run app."""
    app.run(host='0.0.0.0', port=int(port))


@manager.command
def createdb():
    # -*- coding: utf-8 -*-
    """Create database."""
    db.create_all()


@manager.command
def init_db():
    try:
        role = Role(name='editor', description='editor role')
        role.save()
        role = Role(name='admin', description='admin role')
        role.save()
        create_admin('admin', '111111', 'admin@1.com')
        create_editor('editor1', '111111', 'editor1@1.com')
        create_editor('editor2', '111111', 'editor2@1.com')
        create_common_user('wangbin', '111111', 'wangbin@1.com')
        create_common_user('xx', '111111', 'xx@1.com')
        create_common_user('jiyu', '111111', 'jiyu@1.com')
        create_common_user('quwenyu', '111111', 'quwenyu@1.com')
        from youjiao.test_data import book_list, activity_list
        from youjiao.teach_material.models import Book
        from youjiao.content.models import Activity
        for book in book_list:
            b = Book(**book._asdict())
            b.save()
        for activity in activity_list:
            a = Activity(**activity._asdict())
            a.save()
    except Exception as e:
        print(e)


@manager.command
def drop_table():
    """Create database."""
    db.drop_all()


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


@manager.command
def create_qiniu_conf():
    static_dir = os.path.join(os.getcwd(), 'youjiao/static/build')
    dest = "qiniu:access_key={}&secret_key={}&bucket={}&key_prefix={}".format(
        qiniu.AK, qiniu.SK, qiniu.PUBLIC_BUCKET_NAME, qiniu.STATIC_CDN_PREFIX)
    config = {"src": static_dir, "dest": dest, "debug_level": 1}
    with open('qiniu.json', 'w') as f:
        f.write(json.dumps(config))


@manager.option('-n', '--name', dest='name', default='admin')
@manager.option('-p', '--password', dest='password', default='123456')
@manager.option('-e', '--email', dest='email', default='admin@1.com')
def create_admin(name, password, email):
    user = User.create_user(name, email, password)
    profile = UserProfile()
    profile.save()
    user.profile = profile
    user.save()
    role = Role.query.filter_by(name='admin').first()
    if not role:
        role = Role()
        role.name = 'admin'
        role.description = 'admin role'
        role.save()
    user.roles.append(role)
    role = Role.query.filter_by(name='editor').first()
    if not role:
        role = Role()
        role.name = 'editor'
        role.description = 'editor role'
        role.save()
    user.roles.append(role)
    user.save()


def create_editor(name, password, email):
    user = User.create_user(name, email, password)
    profile = UserProfile()
    profile.save()
    user.profile = profile
    role = Role.query.filter_by(name='editor').first()
    if not role:
        role = Role('editor', 'editor role')
        role.save()
    user.roles.append(role)
    user.save()


def create_common_user(name, password, email):
    user = User.create_user(name, email, password)
    profile = UserProfile()
    profile.save()
    user.profile = profile
    user.save()


@app.template_filter('asset')
def asset_filter(file_string):
    try:
        if app.debug == True:
            static_path = '/static/build'
        else:
            static_path = urlparse.urljoin(qiniu.PUBLIC_CDN_DOMAIN, qiniu.STATIC_CDN_PREFIX)
        filename = '.'.join(file_string.split('.')[:-1])
        filetype = file_string.split('.').pop()
        file_resolve_name = app.assets[filename][filetype]
        file_path = os.path.join(static_path, filetype + '/' + file_resolve_name)
        return file_path
    except Exception as e:
        return ''


@app.template_filter('vendor_asset')
def vendor_asset_filter(file_string):
    static_path = 'build'
    file_path = os.path.join(static_path, file_string)
    try:
        if app.debug == True:
            return url_for('static', filename=file_path)
        else:
            relative_path = os.path.join(qiniu.STATIC_CDN_PREFIX, file_string)
            res = urlparse.urljoin(qiniu.PUBLIC_CDN_DOMAIN, relative_path)
            return res
    except Exception as e:
        return ''


manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
