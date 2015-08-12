# coding: utf-8
from flask_script import Manager

from youjiao.extensions import db
from youjiao.app import create_app

# Used by app debug & livereload
PORT = 5000

app = create_app()
manager = Manager(app)


@manager.command
def run():
    """Run app."""
    app.run(port=PORT, debug=True)


@manager.command
def createdb():
    """Create database."""
    db.create_all()


if __name__ == "__main__":
    manager.run()