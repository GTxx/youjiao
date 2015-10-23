# -*- coding: utf-8 -*-
from flask_admin.contrib import sqla
from flask_admin import expose, expose_plugview
from flask_admin.actions import action
from wtforms.widgets import TextArea
from wtforms import TextAreaField
from flask_admin.form import ImageUploadField, ImageUploadInput
from flask_login import current_user
from .permissions import photo_edit_permission, album_edit_permission
from ..admin_utils import AuthEditorMixin
from wtforms.widgets import TextArea
from youjiao.extensions import qiniu
from flask import Markup, url_for, flash, current_app
from uuid import uuid4
from ..extensions import admin, db, qiniu
from .models import Photo, Album
import json


class AlbumAdmin(AuthEditorMixin, sqla.ModelView):

    column_filters = ('name', )
    list_template = 'yj_admin/album.list.html'

    def _preview_formatter(view, context, model, name):
        img_content = ''.join(
            ["<img src={} />".format(photo.thumbnail)
             for photo in model.photos]
        )
        url_content = ''.join(
            ["<p>{}</p>".format(photo.url)
             for photo in model.photos]
        )

        return Markup(img_content+url_content)

    column_formatters = {
        'preview': _preview_formatter
    }

    def scaffold_list_columns(self):
        columns = super(AlbumAdmin, self).scaffold_list_columns()
        columns.append('preview')
        return columns

    @expose('/photo_preview/<id>', methods=('GET', ))
    def photo_preview(self, id):
        album = Album.query.get(id)
        return self.render('yj_admin/photo_preview.html', data=album.photos)


class QiniuImageUploadInput(ImageUploadInput):

    def get_url(self, field):
        return '{}/{}?imageView/2/w/100'.format(qiniu.PUBLIC_CDN_DOMAIN, field.data)


class QiniuImageUploadField(ImageUploadField):

    widget = QiniuImageUploadInput()

    def _save_file(self, data, filename):
        from qiniu import put_data
        data.seek(0)
        bucket_name = current_app.qiniu.PUBLIC_BUCKET_NAME
        # TODO: 上传开启水印转换
        up_token = qiniu.qiniu_auth.upload_token(
            bucket_name, filename,
            policy={})
        res = put_data(up_token=up_token, key=filename, data=data.read())
        return filename

    def generate_name(self, obj, file_data):
        name = super(QiniuImageUploadField, self).generate_name(obj, file_data)
        return unicode(uuid4()) + '/' + name


class PhotoAdmin(AuthEditorMixin, sqla.ModelView):

    column_default_sort = 'id'

    list_template = 'yj_admin/photo.list.html'

    column_filters = ('album_id', )

    # overide qiniu_key field
    form_extra_fields = {
        'qiniu_key': QiniuImageUploadField('Image')
    }
    #
    def scaffold_list_columns(self):
        columns = super(PhotoAdmin, self).scaffold_list_columns()
        # import ipdb; ipdb.set_trace()
        columns.append('preview')
        return columns

    def _preview_formatter(view, context, model, name):
        return Markup("<img src={} /><p>{}</p>".format(model.thumbnail, model.url))

    column_formatters = {
        'preview': _preview_formatter
    }

from flask_admin.consts import ICON_TYPE_GLYPH
admin.add_view(PhotoAdmin(Photo, db.session, name=u'图片', category=u'资源管理',
                          menu_icon_type=ICON_TYPE_GLYPH, menu_icon_value='glyphicon-picture'))
admin.add_view(AlbumAdmin(Album, db.session, name=u'相册', category=u'资源管理',
                          menu_icon_type=ICON_TYPE_GLYPH, menu_icon_value='glyphicon-folder-open'))
