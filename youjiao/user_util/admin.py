# -*- coding: utf-8 -*-
from flask_login import current_user
from flask_admin.contrib import sqla
from youjiao.user.permissions import admin_permission
from ..extensions import admin, db
from .models import LeaveMessage


class LeaveMessageAdmin(sqla.ModelView):

    column_labels = dict(user=u'用户', create_time=u'创建时间', content=u'留言')
    def is_accessible(self):
        if not current_user.is_authenticated:
            return False
        if not admin_permission.can():
            return False
        return True


admin.add_view(LeaveMessageAdmin(LeaveMessage, db.session, category=u'用户管理',
                                 name=u'用户留言'))
