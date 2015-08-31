from flask_login import current_user
from flask_admin.contrib import sqla
from flask_principal import Permission, RoleNeed
from ..admin_utils import AuthMixin
from .permissions import admin_permission


class UserAdmin(sqla.ModelView):
    column_list = ('name', 'email', 'last_login', 'is_admin')
    column_searchable_list = ('name', 'email')
    form_excluded_columns = ('create_time', 'last_login')

    def is_accessible(self):
        if not current_user.is_authenticated():
            return False
        if not admin_permission.can():
            return False
        return True
