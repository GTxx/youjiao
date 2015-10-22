# -*- coding: utf-8 -*-
from flask_admin.contrib import sqla
from wtforms.widgets import TextArea
from wtforms import TextAreaField
from flask_login import current_user
from flask_admin.actions import action
from flask import Markup, url_for, flash
from youjiao.teach_material.admin import JsonField
from .models import Activity, Page, OnlineCourse
from .permissions import content_edit_permission
from ..admin_utils import AuthEditorMixin


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] = 'ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class ActivityAdmin(AuthEditorMixin, sqla.ModelView):
    form_overrides = {
        'html': CKTextAreaField
    }
    create_template = 'ckeditor.html'
    edit_template = 'ckeditor.html'
    column_exclude_list = ('html', )
    column_searchable_list = ('title',)
    form_excluded_columns = ('create_time', 'update_time')
    form_choices = {
        'category': [
            ('policy', u'幼教政策'),
            ('news', u'幼教新闻'),
            ('events', u'幼教事件'),
            ('research', u'理论研究'),
            ('activity', u'实践活动'),
            ('researchevents', u'教研活动'),
            ('researchresult', u'教研成果')
        ],
    }

    @action('publish', 'Publish', u'确定要发布选择的资料吗?')
    def action_approve(self, ids):
        try:
            query = Activity.query.filter(Activity.id.in_(ids))

            count = 0
            for courseware in query.all():
                courseware.publish = True
                courseware.save()
                count += 1

            flash('Activity was successfully approved. {} users were successfully approved.'.format(count))
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise

            flash('Failed to approve users. {}'.format(str(ex)), 'error')

    def scaffold_list_columns(self):
        columns = super(ActivityAdmin, self).scaffold_list_columns()
        columns.append('preview')
        return columns

    def _preview_formatter(view, context, model, name):
        name = model.title if model.title else '活动'
        return Markup(
            "<a href='%s'>%s</a>" % (model.link, model.title))

    column_formatters = {
        'preview': _preview_formatter
    }


class PageAdmin(AuthEditorMixin, sqla.ModelView):
    form_overrides = {
        'html': CKTextAreaField
    }
    create_template = 'ckeditor.html'
    edit_template = 'ckeditor.html'
    column_list = ('title', 'create_time', 'update_time')
    column_searchable_list = ('title',)
    form_excluded_columns = ('create_time', 'update_time')

    def is_accessible(self):
        if not current_user.is_authenticated():
            return False
        if not content_edit_permission.can():
            return False
        return True


class OnlineCourseAdmin(AuthEditorMixin, sqla.ModelView):
    column_default_sort = 'id'
    form_excluded_columns = ('create_time', 'update_time')

    def scaffold_form(self):
        form_class = super(OnlineCourseAdmin, self).scaffold_form()
        form_class.content = JsonField('content')
        return form_class

    def scaffold_list_columns(self):
        columns = super(OnlineCourseAdmin, self).scaffold_list_columns()
        # import ipdb; ipdb.set_trace()
        columns.append('preview')
        return columns

    def _preview_formatter(view, context, model, name):
        name = model.category if model.category else '视频'
        return Markup(
            "<a href='%s'>%s</a>" % (model.link, model.name))

    column_formatters = {
        'preview': _preview_formatter
    }

    @action('publish', u'发布', u'确定要发布选择的资料吗?')
    def action_approve(self, ids):
        try:
            query = OnlineCourse.query.filter(OnlineCourse.id.in_(ids))

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


from ..extensions import admin, db
admin.add_view(ActivityAdmin(Activity, db.session, name=u'幼教动态'))
admin.add_view(PageAdmin(Page, db.session, name=u'静态页面'))
admin.add_view(OnlineCourseAdmin(OnlineCourse, db.session, name=u'幼教网课'))
