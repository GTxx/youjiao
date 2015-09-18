# -*- coding: utf-8 -*-
from flask_admin.contrib import sqla
from wtforms.widgets import TextArea
from wtforms import TextAreaField
from flask_login import current_user
from .permissions import content_edit_permission
from ..admin_utils import AuthMixin


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] = 'ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class ActivityAdmin(AuthMixin, sqla.ModelView):
    form_overrides = {
        'html': CKTextAreaField
    }
    create_template = 'ckeditor.html'
    edit_template = 'ckeditor.html'
    column_list = ('title', 'create_time', 'update_time', 'status', 'category')
    column_searchable_list = ('title',)
    form_excluded_columns = ('create_time', 'update_time')
    form_choices = {
        'category': [
            ('policy', u'幼教政策'),
            ('news', u'幼教新闻'),
            ('events', u'幼教事件'),
            ('research', u'理论研究'),
            ('activity', u'实践活动')
        ],
    }

    def is_accessible(self):
        if not current_user.is_authenticated():
            return False
        if not content_edit_permission.can():
            return False
        return True


class PageAdmin(AuthMixin, sqla.ModelView):
    form_overrides = {
        'html': CKTextAreaField
    }
    create_template = 'ckeditor.html'
    edit_template = 'ckeditor.html'
    column_list = ('title', 'create_time', 'update_time', 'status')
    column_searchable_list = ('title',)
    form_excluded_columns = ('create_time', 'update_time')
    form_choices = {
        'status': [
            (False, u'草稿'),
            (True, u'发布'),
        ]
    }

    def is_accessible(self):
        if not current_user.is_authenticated():
            return False
        if not content_edit_permission.can():
            return False
        return True


from ..extensions import admin, db
from .models import Activity, Page

admin.add_view(ActivityAdmin(Activity, db.session))
admin.add_view(PageAdmin(Page, db.session))
