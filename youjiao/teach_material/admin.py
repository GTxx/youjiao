# -*- coding: utf-8 -*-
from flask_admin.contrib import sqla
from flask_admin.actions import action
from wtforms.widgets import TextArea
from wtforms import TextAreaField
from flask_login import current_user
from .permissions import book_edit_permission, courseware_edit_permission
from ..admin_utils import AuthMixin
from wtforms.widgets import TextArea
from flask import Markup, url_for, flash
from ..extensions import admin, db
from .models import Book, Courseware
import json



class BookAdmin(AuthMixin, sqla.ModelView):

    def _preview_formatter(view, context, model, name):
        return Markup(
            "<a href='%s'>%s</a>" % (
                url_for('book_view.book_detail', book_id=model.id),
                model.name
            )
        ) if model.name else "book"

    column_formatters = {
        'preview': _preview_formatter
    }
    column_exclude_list = ('image_array', 'preview_array')

    def is_accessible(self):
        if not current_user.is_authenticated():
            return False
        if not book_edit_permission.can():
            return False
        return True


    def scaffold_list_columns(self):
        columns = super(BookAdmin, self).scaffold_list_columns()
        # import ipdb; ipdb.set_trace()
        columns.append('preview')
        return columns

    @action('approve', 'Approve', 'Are you sure you want to approve selected users?')
    def action_approve(self, ids):
        try:
            query = Book.query.filter(Book.id.in_(ids))

            count = 0
            for book in query.all():
                book.publish = True
                book.save()
                count += 1

            flash('User was successfully approved. {} users were successfully approved.'.format(count))
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise

            flash('Failed to approve users. {}'.format(str(ex)), 'error')


class JsonField(TextAreaField):
    widget = TextArea()

    def _value(self):
        if self.data:
            return json.dumps(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            try:
                # import ipdb; ipdb.set_trace()
                self.data = json.loads(valuelist[0].replace('\r\n', ''))
            except Exception as e:
                raise ValueError(str(e))
        else:
            self.data = {}


class CoursewareAdmin(AuthMixin, sqla.ModelView):

    column_default_sort = 'id'

    def is_accessible(self):
        if not current_user.is_authenticated():
            return False
        if not courseware_edit_permission.can():
            return False
        return True

    def scaffold_form(self):
        form_class = super(CoursewareAdmin, self).scaffold_form()
        form_class.content = JsonField('content')
        return form_class

    def scaffold_list_columns(self):
        columns = super(CoursewareAdmin, self).scaffold_list_columns()
        # import ipdb; ipdb.set_trace()
        columns.append('preview')
        return columns

    def _preview_formatter(view, context, model, name):
        name = model.name if model.name else 'courseware'
        return Markup(
            "<a href='%s'>%s</a>" % (
                url_for('book_view.courseware_detail', courseware_id=model.id),
                name
            ))


    column_formatters = {
        'preview': _preview_formatter
    }

    @action('approve', 'Approve', 'Are you sure you want to approve selected users?')
    def action_approve(self, ids):
        try:
            query = Courseware.query.filter(Courseware.id.in_(ids))

            count = 0
            for courseware in query.all():
                courseware.publish = True
                courseware.save()
                count += 1

            flash('User was successfully approved. {} users were successfully approved.'.format(count))
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise

            flash('Failed to approve users. {}'.format(str(ex)), 'error')


admin.add_view(BookAdmin(Book, db.session))
admin.add_view(CoursewareAdmin(Courseware, db.session))
