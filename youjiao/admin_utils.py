from flask_login import current_user
from flask import redirect, url_for, request
from flask_admin import AdminIndexView, expose
from flask_principal import Permission, RoleNeed


class AuthEditorMixin(object):
    # add auth in admin view
    def is_accessible(self):
        edit_permission = Permission(RoleNeed('editor'))
        if not current_user.is_authenticated:
            return False
        if not edit_permission.can():
            return False
        return True
