from flask_principal import Permission, RoleNeed

content_edit_permission = Permission(RoleNeed('editor'))

content_preview_permission = Permission(RoleNeed('editor'))
