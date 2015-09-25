# -*- coding: utf-8 -*-
from flask_admin.contrib import sqla
from flask_admin.actions import action
from wtforms.widgets import TextArea
from wtforms import TextAreaField
from flask_login import current_user
from .permissions import photo_edit_permission, album_edit_permission
from ..admin_utils import AuthMixin
from wtforms.widgets import TextArea
from flask import Markup, url_for, flash, current_app
from uuid import uuid4
from ..extensions import admin, db, qiniu
from .models import Photo, Album
import json



class AlbumAdmin(AuthMixin, sqla.ModelView):

    column_filters = ('name', )

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
    # column_exclude_list = ('image_array', 'preview_array')

    def is_accessible(self):
        if not current_user.is_authenticated():
            return False
        # if not album_edit_permission.can():
        #     return False
        return True

    def scaffold_list_columns(self):
        columns = super(AlbumAdmin, self).scaffold_list_columns()
        # import ipdb; ipdb.set_trace()
        columns.append('preview')
        return columns

    # @action('approve', 'Approve', 'Are you sure you want to approve selected users?')
    # def action_approve(self, ids):
    #     try:
    #         query = Book.query.filter(Book.id.in_(ids))
    #
    #         count = 0
    #         for book in query.all():
    #             book.publish = True
    #             book.save()
    #             count += 1
    #
    #         flash('User was successfully approved. {} users were successfully approved.'.format(count))
    #     except Exception as ex:
    #         if not self.handle_view_exception(ex):
    #             raise
    #
    #         flash('Failed to approve users. {}'.format(str(ex)), 'error')


# class JsonField(TextAreaField):
#     widget = TextArea()
#
#     def _value(self):
#         if self.data:
#             return json.dumps(self.data)
#         else:
#             return u''
#
#     def process_formdata(self, valuelist):
#         if valuelist:
#             try:
#                 import ipdb; ipdb.set_trace()
#                 self.data = json.loads(valuelist[0].replace('\r\n', ''))
#             except Exception as e:
#                 raise ValueError(str(e))
#         else:
#             self.data = {}


from flask_admin.form import ImageUploadField, ImageUploadInput
from wtforms import Form

class QiniuImageUploadInput(ImageUploadInput):

    def get_url(self, field):
        qiniu_domain = current_app.config.get('QINIU_CDN_DOMAIN')
        return '{}/{}?imageView/2/w/100'.format(qiniu_domain, field.data)


class QiniuImageUploadField(ImageUploadField):

    widget = QiniuImageUploadInput()

    def _save_file(self, data, filename):
        from qiniu import put_data
        data.seek(0)
        bucket_name = current_app.config.get('QINIU_BUCKET_NAME')
        up_token = qiniu.qiniu_auth.upload_token(bucket_name, filename)
        res = put_data(up_token=up_token, key=filename, data=data.read())
        return filename

    def generate_name(self, obj, file_data):
        name = super(QiniuImageUploadField, self).generate_name(obj, file_data)
        return unicode(uuid4()) + '/' + name


class PhotoAdmin(AuthMixin, sqla.ModelView):

    column_default_sort = 'id'

    def is_accessible(self):
        if not current_user.is_authenticated():
            return False
        if not photo_edit_permission.can():
            return False
        return True

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


admin.add_view(PhotoAdmin(Photo, db.session))
admin.add_view(AlbumAdmin(Album, db.session))
