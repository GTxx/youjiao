from flask_principal import Permission, RoleNeed

admin_permission = Permission(RoleNeed('admin'))
editor_permission = Permission(RoleNeed('editor'))