# -*- coding: utf-8 -*-
from flask_principal import Permission, RoleNeed

book_edit_permission = Permission(RoleNeed('editor'))
courseware_edit_permission = Permission(RoleNeed('editor'))

# book还没发布时， 对/book/<id> 页面预览权限
book_preview_permission = Permission(RoleNeed('editor'))
# courseware还没发布时， 对/courseware/<id> 页面预览权限
courseware_preview_permission = Permission(RoleNeed('editor'))
