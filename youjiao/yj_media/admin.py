# -*- coding: utf-8 -*-
from .models import Video, Audio, Document
import urllib
from flask import flash, current_app, url_for
from flask_admin.contrib import sqla
from flask_admin.actions import action
from qiniu import Auth, PersistentFop, op_save
from youjiao.extensions import admin, db
from ..admin_utils import AuthMixin


class VideoAdmin(AuthMixin, sqla.ModelView):

    def is_accessible(self):
        if not super(VideoAdmin, self).is_accessible():
            import ipdb; ipdb.set_trace()
            return False
        return True

    @action('convert', u'转码', 'Are you sure you want to convert this video?')
    def action_approve(self, ids):
        try:
            query = Video.query.filter(Video.id.in_(ids))
            count = 0
            src_bucket_name = current_app.qiniu.PRIVATE_BUCKET_NAME
            dest_bucket_name = src_bucket_name
            pipeline = current_app.qiniu.PIPELINE
            for video in query.all():
                saved_key = video.qiniu_key + '.mp4'
                # TODO: add callback
                pfop = PersistentFop(current_app.qiniu.qiniu_auth,
                                     src_bucket_name, pipeline,
                                     url_for('video_qiniu_callback'))
                op = op_save('avthumb/mp4', dest_bucket_name, saved_key.encode('utf-8'))
                ops = []
                ops.append(op)
                ret, info = pfop.execute(video.qiniu_key, ops, 1)
                if info.status_code != 200:
                    raise Exception('error {}'.format(info))
            flash('{} users were successfully approved.'.format(count))
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise

            flash('Failed to approve users. {}'.format(str(ex)), 'error')


admin.add_view(VideoAdmin(Video, db.session, name=u'视频'))
