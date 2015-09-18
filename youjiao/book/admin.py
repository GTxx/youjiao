# -*- coding: utf-8 -*-
from flask_admin.contrib import sqla
from wtforms.widgets import TextArea
from wtforms import TextAreaField
from flask_login import current_user
from .permissions import book_edit_permission
from ..admin_utils import AuthMixin


class BookAdmin(AuthMixin, sqla.ModelView):

    def is_accessible(self):
        if not current_user.is_authenticated():
            return False
        # if not book_edit_permission.can():
            # return False
        return True


from ..extensions import admin, db
from .models import Book

admin.add_view(BookAdmin(Book, db.session))
