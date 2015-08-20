# coding: utf-8
from flask_script import Manager
from youjiao.extensions import db
from youjiao.app import create_app

# Used by app debug & livereload
PORT = 5000

app = create_app()
manager = Manager(app)


@manager.option('-p', '--port', dest='port', default=5000)
def run(port):
    """Run app."""
    app.run(port=int(port), debug=True)


@manager.command
def createdb():
    """Create database."""
    db.create_all()


@manager.command
def dropdb():
    """Create database."""
    db.drop_all()


if __name__ == "__main__":
    manager.run()
