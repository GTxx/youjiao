from flask_login import current_user
from flask_admin.contrib import sqla
from flask_principal import Permission, RoleNeed
from ..admin_utils import AuthMixin
from .permissions import admin_permission
from .models import User, Role


class UserAdmin(sqla.ModelView):
    column_list = ('name', 'email', 'last_login', 'create_time')
    column_searchable_list = ('name', 'email')
    form_excluded_columns = ('create_time', 'last_login', 'password', 'profile')

    # deactivate user if not want user to login
    can_delete = False

    create_modal = True
    edit_modal = True

    def create_model(self, form):
        user = super(UserAdmin, self).create_model(form)
        user.set_password(user.password)
        return user

    def is_accessible(self):
        if not current_user.is_authenticated():
            return False
        if not admin_permission.can():
            return False
        return True


class RoleAdmin(sqla.ModelView):
    column_list = ('name', 'description')
    column_searchable_list = ('name', 'description')

    create_modal = True
    edit_modal = True

    def is_accessible(self):
        if not current_user.is_authenticated():
            return False
        if not admin_permission.can():
            return False
        return True


from ..extensions import admin, db

admin.add_view(UserAdmin(User, db.session))
admin.add_view(RoleAdmin(Role, db.session))
