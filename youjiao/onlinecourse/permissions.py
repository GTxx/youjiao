
from flask_principal import Permission, RoleNeed

onlinecourse_preview_permission = Permission(RoleNeed('editor'))
