# coding: utf-8
from flask_script import Manager
from models import db
from app import app

# Used by app debug & livereload
PORT = 5000

manager = Manager(app)


@manager.command
def run():
    """Run app."""
    app.run(port=PORT)


@manager.command
def createdb():
    """Create database."""
    db.create_all()


if __name__ == "__main__":
    manager.run()