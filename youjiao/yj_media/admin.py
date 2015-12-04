# -*- coding: utf-8 -*-
from .models import Video, Audio, Document
import json
from urlparse import urljoin
from flask import flash, current_app, url_for, Markup
from flask_admin.consts import ICON_TYPE_GLYPH
from flask_admin.contrib import sqla
from flask_admin.actions import action
from qiniu import Auth, PersistentFop, op_save
from youjiao.extensions import admin, db
from .views import (QINIU_CALLBACK_ROUTE, QINIU_DOCUMENT_CALLBACK_ROUTE,
                    )
from ..admin_utils import AuthEditorMixin
from youjiao.utils.admin import JsonField, _json_format_field


class VideoAdmin(AuthEditorMixin, sqla.ModelView):

    def is_accessible(self):
        if not super(VideoAdmin, self).is_accessible():
            return False
        return True

    def scaffold_list_columns(self):
        columns = super(VideoAdmin, self).scaffold_list_columns()
        # import ipdb; ipdb.set_trace()
        columns.append(u'mp4')
        return columns

    def _mp4(view, context, model, name):
        if model.media_process:
            return model.media_process['mp4']['key']
        return ''

    column_formatters = {
        u'mp4': _mp4,
        'media_process': _json_format_field('media_process'),
        'media_meta': _json_format_field('media_meta')
    }
    column_list = ['name', 'qiniu_key', 'mp4']
    column_searchable_list = ('name',)
    can_view_details = True
    details_template = 'json_detail.html'
    column_labels = dict(name=u'名字', qiniu_key=u'qiniuKey')

    @action('convert', u'转mp4', 'Are you sure you want to convert this video?')
    def action_convert_mp4(self, ids):
        try:
            count = Video.batch_convert_mp4(ids)
            flash(u'{} video begin to convert.'.format(count))
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise

            flash(u'Failed to convert video. {}'.format(str(ex)), 'error')

    # @action('cut', u'视频切割', u'视频将切割成3min,确定吗')
    # def video_cut(self, ids):
    #     try:
    #         count = Video.batch_video_cut(ids)
    #         flash(u'{} video begin to cut.'.format(count))
    #     except Exception as ex:
    #         if not self.handle_view_exception(ex):
    #             raise
    #
    #         flash(u'Failed to cut video. {}'.format(str(ex)), 'error')

class DocumentAdmin(AuthEditorMixin, sqla.ModelView):

    can_view_details = True
    def is_accessible(self):
        if not super(DocumentAdmin, self).is_accessible():
            return False
        return True

    def scaffold_list_columns(self):
        columns = super(DocumentAdmin, self).scaffold_list_columns()
        # import ipdb; ipdb.set_trace()
        columns.append(u'pdf')
        return columns

    def _pdf(view, context, model, name):
        if model.media_process:
            return model.media_process['pdf']['key']
        return ''

    column_formatters = {
        u'pdf': _pdf,
        'media_process': _json_format_field('media_process'),
        'media_meta': _json_format_field('media_meta')
    }
    column_list = ['name', 'qiniu_key', 'pdf']
    column_searchable_list = ('name',)
    can_view_details = True
    details_template = 'json_detail.html'

    column_labels = dict(name=u'名字', qiniu_key=u'qiniuKey')

    @action('convert', u'转pdf', u'文档会转换成pdf并存储在私有空间，确定要转换吗?')
    def action_convert_pdf(self, ids):
        try:
            count = Document.batch_conver_pdf(ids)
            flash('{} users were successfully approved.'.format(count))
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise

            flash('Failed to approve users. {}'.format(str(ex)), 'error')


class AudioAdmin(AuthEditorMixin, sqla.ModelView):

    column_searchable_list = ('name',)
    can_view_details = True
    details_template = 'json_detail.html'

    def scaffold_list_columns(self):
        columns = super(AudioAdmin, self).scaffold_list_columns()
        # import ipdb; ipdb.set_trace()
        columns.append(u'mp3')
        return columns

    def _mp3(view, context, model, name):
        if model.media_process:
            return model.media_process['mp3']['key']
        return ''

    column_formatters = {
        u'mp3': _mp3,
        'media_process': _json_format_field('media_process'),
        'media_meta': _json_format_field('media_process')
    }
    column_list = ['name', 'qiniu_key', 'mp3']

    column_labels = dict(name=u'名字', qiniu_key=u'qiniuKey')

    @action('convert', u'转mp3', u'文件会转换并另存为mp3,确定吗?')
    def action_convert(self, ids):
        try:
            count = Audio.batch_convert_mp3(ids)
            flash('{} audio begin to convert.'.format(count))
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise
            flash('Failed to convert mp3. {}'.format(str(ex)), 'error')


admin.add_view(VideoAdmin(Video, db.session, name=u'视频', category=u'资源管理',
                          menu_icon_type=ICON_TYPE_GLYPH,
                          menu_icon_value='glyphicon-hd-video'))


admin.add_view(DocumentAdmin(Document, db.session, name=u'文档', category=u'资源管理',
                          menu_icon_type=ICON_TYPE_GLYPH,
                          menu_icon_value='glyphicon-file'))


admin.add_view(AudioAdmin(Audio, db.session, name=u'音频', category=u'资源管理',
                          menu_icon_type=ICON_TYPE_GLYPH,
                          menu_icon_value='glyphicon-headphones'))
