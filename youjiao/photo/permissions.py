from flask_principal import Permission, RoleNeed

photo_edit_permission = Permission(RoleNeed('editor'))

album_edit_permission = Permission(RoleNeed('editor'))
