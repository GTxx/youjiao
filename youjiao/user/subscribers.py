from datetime import datetime
from flask import current_app
from flask_login import user_logged_in


def record_user_login_time(sender, user):
    user.last_login = datetime.utcnow()
    user.save()


def connect(app):
    # connect sender and subscriber here.
    # In case sender is app, call this function after app is created.
    user_logged_in.connect(record_user_login_time, sender=app)