# -*- coding: utf-8 -*-
from .models import Video, Audio, Document
import json
from urlparse import urljoin
from flask import flash, current_app, url_for
from flask_admin.consts import ICON_TYPE_GLYPH
from flask_admin.contrib import sqla
from flask_admin.actions import action
from qiniu import Auth, PersistentFop, op_save
from youjiao.extensions import admin, db
from .views import QINIU_CALLBACK_ROUTE, QINIU_DOCUMENT_CALLBACK_ROUTE
from ..admin_utils import AuthMixin
from youjiao.utils.admin import JsonField


class VideoAdmin(AuthMixin, sqla.ModelView):

    def is_accessible(self):
        if not super(VideoAdmin, self).is_accessible():
            return False
        return True

    def scaffold_list_columns(self):
        columns = super(VideoAdmin, self).scaffold_list_columns()
        # import ipdb; ipdb.set_trace()
        columns.append(u'预处理')
        return columns

    def _preview_formatter(view, context, model, name):
        if model.media_process:
            return json.dumps(model.media_process, ensure_ascii=False)
        return ''

    def scaffold_form(self):
        form_class = super(VideoAdmin, self).scaffold_form()
        form_class.media_meta = JsonField('media_meta')
        form_class.media_process = JsonField('media_process')
        return form_class

    column_formatters = {
        u'预处理': _preview_formatter
    }
    column_exclude_list = ['media_process']

    @action('convert', u'转mp4', 'Are you sure you want to convert this video?')
    def action_approve(self, ids):
        try:
            query = Video.query.filter(Video.id.in_(ids))
            count = 0
            src_bucket_name = current_app.qiniu.PRIVATE_BUCKET_NAME
            dest_bucket_name = src_bucket_name
            pipeline = current_app.qiniu.PIPELINE
            QINIU_VIDEO_CALLBACK_URL = urljoin(
                    current_app.qiniu.CALLBACK_URL, QINIU_CALLBACK_ROUTE)
            pfop = PersistentFop(current_app.qiniu.qiniu_auth,
                                 src_bucket_name, pipeline,
                                 QINIU_VIDEO_CALLBACK_URL)
            ops = []
            for video in query.all():
                saved_key = video.qiniu_key + '.mp4'
                # import ipdb; ipdb.set_trace()
                op = op_save('avthumb/mp4', dest_bucket_name, saved_key.encode('utf-8'))
                ops.append(op)
            ret, info = pfop.execute(video.qiniu_key, ops, force=1)
            if info.status_code != 200:
                raise Exception(u'error {}'.format(info))
            flash(u'{} users were successfully approved.'.format(count))
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise

            flash(u'Failed to approve users. {}'.format(str(ex)), 'error')


class DocumentAdmin(AuthMixin, sqla.ModelView):

    def is_accessible(self):
        if not super(DocumentAdmin, self).is_accessible():
            return False
        return True

    def scaffold_list_columns(self):
        columns = super(DocumentAdmin, self).scaffold_list_columns()
        # import ipdb; ipdb.set_trace()
        columns.append(u'预处理')
        return columns

    def _preview_formatter(view, context, model, name):
        if model.media_process:
            return json.dumps(model.media_process, ensure_ascii=False)
        return ''

    column_formatters = {
        u'预处理': _preview_formatter
    }
    column_exclude_list = ['media_process']

    @action('convert', u'转pdf', u'文档会转换成pdf并存储在私有空间，确定要转换吗?')
    def action_approve(self, ids):
        try:
            query = Document.query.filter(Video.id.in_(ids))
            count = 0
            src_bucket_name = current_app.qiniu.PRIVATE_BUCKET_NAME
            dest_bucket_name = src_bucket_name
            QINIU_DOCUMENT_CALLBACK_URL = urljoin(
                    current_app.qiniu.CALLBACK_URL, QINIU_DOCUMENT_CALLBACK_ROUTE)
            pfop = PersistentFop(current_app.qiniu.qiniu_auth, src_bucket_name,
                                 notify_url=QINIU_DOCUMENT_CALLBACK_URL)
            ops = []
            for document in query.all():
                saved_key = document.qiniu_key + '.pdf'
                op = op_save('yifangyun_preview', dest_bucket_name, saved_key.encode('utf-8'))
                ops.append(op)
            ret, info = pfop.execute(document.qiniu_key, ops, force=1)
            if info.status_code != 200:
                raise Exception('error {}'.format(info))
            flash('{} users were successfully approved.'.format(count))
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise

            flash('Failed to approve users. {}'.format(str(ex)), 'error')


class AudioAdmin(AuthMixin, sqla.ModelView):

    def is_accessible(self):
        if not super(AudioAdmin, self).is_accessible():
            import ipdb; ipdb.set_trace()
            return False
        return True

    def scaffold_list_columns(self):
        columns = super(AudioAdmin, self).scaffold_list_columns()
        # import ipdb; ipdb.set_trace()
        columns.append(u'预处理')
        return columns

    def _preview_formatter(view, context, model, name):
        if model.media_process:
            return json.dumps(model.media_process, indent=2, ensure_ascii=False)
        return ''

    column_formatters = {
        u'预处理': _preview_formatter
    }
    column_exclude_list = ['media_process']


admin.add_view(VideoAdmin(Video, db.session, name=u'视频', category=u'资源管理',
                          menu_icon_type=ICON_TYPE_GLYPH,
                          menu_icon_value='glyphicon-hd-video'))


admin.add_view(DocumentAdmin(Document, db.session, name=u'文档', category=u'资源管理',
                          menu_icon_type=ICON_TYPE_GLYPH,
                          menu_icon_value='glyphicon-file'))


admin.add_view(AudioAdmin(Audio, db.session, name=u'音频', category=u'资源管理',
                          menu_icon_type=ICON_TYPE_GLYPH,
                          menu_icon_value='glyphicon-headphones'))
