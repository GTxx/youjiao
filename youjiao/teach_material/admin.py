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
    column_filters = ('level', 'category', 'name')
    column_searchable_list = ('name', 'executive_editor', 'chief_editor')
    column_labels = dict(name=u'图书名', chief_editor=u'主编', executive_editor=u'责任编辑', publisher=u'出版社',
                         book_size=u'图书大小', level=u'等级', category=u'分类', price=u'价格',
                         publish=u'是否发布', preview=u'内容', coursewares=u'关联课件', image_array=u'图书封面',
                         preview_array=u'预览图片')
    column_display_pk = True

    def scaffold_list_columns(self):
        columns = super(BookAdmin, self).scaffold_list_columns()
        # import ipdb; ipdb.set_trace()
        columns.append('preview')
        return columns

    @action('approve', u'发布', u'确定要发布所选择的图书吗?')
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

    @action('recommend', u'加入首页教材推荐', u'把图书加入到首页推荐吗?')
    def add_home_recommend(self, ids):
        from youjiao.content.models import ContentList
        try:
            query = Book.query.filter(Book.id.in_(ids))
            ContentList.add_obj_to_position(query, ContentList.HOME_BOOK)
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise
            flash(u'操作失败. {}'.format(str(ex)), 'error')


class CoursewareAdmin(AuthEditorMixin, sqla.ModelView):
    create_template = 'json_editor.html'
    edit_template = 'json_editor.html'
    column_exclude_list = ('content',)
    column_default_sort = 'id'
    column_searchable_list = ('name',)
    column_display_pk = True

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

    def _book(view, context, model, name):
        if model.book:
            return model.book.name
        else:
            return ''

    column_formatters = {
        'preview': _preview_formatter,
        'book': _book,
    }

    column_exclude_list = ['content']

    column_labels = dict(name=u'课件名', book=u'所属图书', publish=u'是否发布',
                         preview=u'内容', cover_img_url=u'课件封面', level=u'班级')

    @action('publish', u'发布', u'确定要发布选择的资料吗?')
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

    @action('recommend', u'加入首页课件推荐', u'把课件加入到首页推荐吗?')
    def add_home_courseware(self, ids):
        from youjiao.content.models import ContentList
        try:
            query = Courseware.query.filter(Courseware.id.in_(ids))
            ContentList.add_obj_to_position(query, ContentList.HOME_COURSEWARE)
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise
            flash(u'操作失败. {}'.format(str(ex)), 'error')


admin.add_view(BookAdmin(Book, db.session, name=u'教材'))
admin.add_view(CoursewareAdmin(Courseware, db.session, name=u'课件'))
