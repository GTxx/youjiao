# -*- coding: utf-8 -*-
from flask_admin.contrib import sqla
from flask_admin.actions import action
from flask import Markup, flash
from youjiao.teach_material.admin import JsonField
from youjiao.utils.admin import _json_format_field
from .models import OnlineCourse
from ..admin_utils import AuthEditorMixin


class OnlineCourseAdmin(AuthEditorMixin, sqla.ModelView):
    column_default_sort = 'id'
    form_excluded_columns = ('create_time', 'update_time')

    create_template = 'onlinecourse/onlinecourse_admin_json_create.html'
    edit_template = 'onlinecourse/onlinecourse_admin_json_editor.html'

    can_view_details = True
    details_template = 'json_detail.html'

    def scaffold_form(self):
        form_class = super(OnlineCourseAdmin, self).scaffold_form()
        form_class.content = JsonField('content')
        return form_class

    def scaffold_list_columns(self):
        columns = super(OnlineCourseAdmin, self).scaffold_list_columns()
        columns.append('preview')
        return columns

    def _preview_formatter(view, context, model, name):
        name = model.category if model.category else '视频'
        return Markup(
            "<a href='%s'>%s</a>" % (model.link, model.name))

    column_formatters = {
        'preview': _preview_formatter,
        'content': _json_format_field('content')
    }

    column_labels = dict(create_time=u'创建时间', update_time=u'更新时间', title=u'标题', name=u'名称',
                         url=u'地址', content=u'内容', category=u'类型', publish=u'是否发布', preview=u'预览')

    @action('publish', u'发布', u'确定要发布选择的网课吗?')
    def action_approve(self, ids):
        try:
            query = OnlineCourse.query.filter(OnlineCourse.id.in_(ids))

            count = 0
            for onlinecourse in query.all():
                onlinecourse.publish = True
                onlinecourse.save()
                count += 1

            flash(u'发布了{}个网课.'.format(count))
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise

            flash(u'发布网课失败. {}'.format(str(ex)), 'error')


from ..extensions import admin, db


admin.add_view(OnlineCourseAdmin(OnlineCourse, db.session, name=u'幼教网课'))
