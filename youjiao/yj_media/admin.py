# -*- coding: utf-8 -*-
from .models import Video, Audio, Document
import urllib
import json
from urlparse import urljoin
from flask import flash, current_app, url_for
from flask_admin.contrib import sqla
from flask_admin.actions import action
from qiniu import Auth, PersistentFop, op_save
from youjiao.extensions import admin, db
from .views import QINIU_CALLBACK_ROUTE
from ..admin_utils import AuthMixin


class VideoAdmin(AuthMixin, sqla.ModelView):

    def is_accessible(self):
        if not super(VideoAdmin, self).is_accessible():
            import ipdb; ipdb.set_trace()
            return False
        return True

    def scaffold_list_columns(self):
        columns = super(VideoAdmin, self).scaffold_list_columns()
        # import ipdb; ipdb.set_trace()
        columns.append('preview')
        return columns

    def _preview_formatter(view, context, model, name):
        if model.json:
            return json.dumps(model.json, ensure_ascii=False)
        return ''

    column_formatters = {
        'preview': _preview_formatter
    }
    column_exclude_list = ['json']

    @action('convert', u'转码私密', 'Are you sure you want to convert this video?')
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
                raise Exception('error {}'.format(info))
            flash('{} users were successfully approved.'.format(count))
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise

            flash('Failed to approve users. {}'.format(str(ex)), 'error')


admin.add_view(VideoAdmin(Video, db.session, name=u'视频'))
