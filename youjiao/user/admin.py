from flask_admin.contrib import sqla


class UserAdmin(sqla.ModelView):
    column_list = ('name', 'email', 'last_login', 'is_admin')
    column_searchable_list = ('name', 'email')
    form_excluded_columns = ('create_time', 'last_login')
