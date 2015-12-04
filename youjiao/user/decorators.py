from flask_login import current_user
from flask import redirect
from functools import wraps


def anonymous_user_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect('/')
        return f(*args, **kwargs)
    return wrapper