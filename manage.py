# coding: utf-8
from flask_script import Manager
from youjiao.extensions import db
from youjiao.app import create_app
from youjiao.user.models import User, Role

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
def dropdb():
    """Create database."""
    db.drop_all()

@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


@manager.command
def init_db():
    try:
        role = Role(name='editor', description='editor role')
        role.save()
        role = Role(name='admin', description='admin role')
        role.save()
    except Exception as e:
        print(e)


@manager.option('-n', '--name', dest='name', default='admin')
@manager.option('-p', '--password', dest='password', default='123456')
@manager.option('-e', '--email', dest='email', default='admin@1.com')
def create_admin(name, password, email):
    user = User.create_user(name, email, password)
    role = Role.query.filter_by(name='admin').first()
    if not role:
        role = Role('admin', 'admin role')
        role.save()
    user.roles.append(role)
    user.save()

@manager.command
def create_test_data():
    pass

if __name__ == "__main__":
    manager.run()
