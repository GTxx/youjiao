from flask_principal import Permission, RoleNeed

content_edit_permission = Permission(RoleNeed('editor'))
