# -*- coding: utf-8 -*-
from flask_login import current_user
from flask_admin.contrib import sqla
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

    column_labels = dict(email=u'邮箱地址', last_login=u'上次登陆时间', name=u'用户名', create_time=u'创建时间')

    def create_model(self, form):
        user = super(UserAdmin, self).create_model(form)
        user.set_password(user.password)
        return user

    def is_accessible(self):
        if not current_user.is_authenticated:
            return False
        if not admin_permission.can():
            return False
        return True


class RoleAdmin(sqla.ModelView):
    column_list = ('name', 'description')
    column_searchable_list = ('name', 'description')

    create_modal = True
    edit_modal = True

    column_labels = dict(name=u'用户名', description=u'用户身份')

    def is_accessible(self):
        if not current_user.is_authenticated:
            return False
        if not admin_permission.can():
            return False
        return True


from ..extensions import admin, db
from flask_admin.consts import ICON_TYPE_GLYPH


admin.add_view(UserAdmin(User, db.session, category=u'用户管理', name=u'用户',
                         menu_icon_type=ICON_TYPE_GLYPH,
                         menu_icon_value='glyphicon-user'))
admin.add_view(RoleAdmin(Role, db.session, category=u'用户管理', name=u'身份',
                         menu_icon_type=ICON_TYPE_GLYPH,
                         menu_icon_value='glyphicon-education'))
