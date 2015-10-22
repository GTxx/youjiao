# -*- coding: utf-8 -*-
from flask_admin.contrib import sqla
from flask_admin.actions import action
from wtforms.widgets import TextArea
from wtforms import TextAreaField
from flask_login import current_user
from .permissions import book_edit_permission, courseware_edit_permission
from ..admin_utils import AuthEditorMixin
from wtforms.widgets import TextArea
from flask import Markup, url_for, flash
from ..extensions import admin, db
from .models import Book, Courseware
from youjiao.utils.admin import JsonField
import json


class BookAdmin(AuthEditorMixin, sqla.ModelView):

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


class CoursewareAdmin(AuthEditorMixin, sqla.ModelView):

    column_default_sort = 'id'

    def scaffold_form(self):
        form_class = super(CoursewareAdmin, self).scaffold_form()
        form_class.content = JsonField('content')
        return form_class

    def scaffold_list_columns(self):
        columns = super(CoursewareAdmin, self).scaffold_list_columns()
        # import ipdb; ipdb.set_trace()
        columns.append('preview')
        columns.append(u'内容')
        return columns

    def _preview_formatter(view, context, model, name):
        name = model.name if model.name else 'courseware'
        return Markup(
            "<a href='%s'>%s</a>" % (
                url_for('book_view.courseware_detail', courseware_id=model.id),
                name
            ))

    def _content_formatter(view, context, model, name):
        if model.content:
            return json.dumps(model.content, ensure_ascii=False)
        return ''

    column_formatters = {
        'preview': _preview_formatter,
        u'内容': _content_formatter
    }

    column_exclude_list = ['content']

    @action('publish', 'Publish', u'确定要发布选择的资料吗?')
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


admin.add_view(BookAdmin(Book, db.session, name=u'教材'))
admin.add_view(CoursewareAdmin(Courseware, db.session, name=u'课件'))
