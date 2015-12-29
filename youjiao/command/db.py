from youjiao.extensions import manager
import os
from flask import current_app

@manager.command
def db_shell():
    os.system('pgcli {}'.format(current_app.config['SQLALCHEMY_DATABASE_URI']))
