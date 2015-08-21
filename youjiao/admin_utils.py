from flask_login import current_user
from flask import redirect, url_for, request


class AuthMixin(object):
    # add auth in admin view
    def is_accessible(self):
        return current_user.is_authenticated()

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('security.login', next=request.url))
