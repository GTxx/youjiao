from flask_principal import Permission, RoleNeed

book_edit_permission = Permission(RoleNeed('editor'))