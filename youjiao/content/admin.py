# -*- coding: utf-8 -*-
from flask_admin.contrib import sqla
from wtforms.widgets import TextArea
from wtforms import TextAreaField


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += 'ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class ActivityAdmin(sqla.ModelView):
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
        ],
        'status': [
            ('1', u'草稿'),
            ('2', u'发布'),
        ]
    }


class PageAdmin(sqla.ModelView):
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
            ('1', u'草稿'),
            ('2', u'发布'),
        ]
    }
