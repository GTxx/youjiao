# -*- coding: utf-8 -*-

from youjiao.extensions import db
from youjiao.utils.database import CRUDMixin
import sqlalchemy as sqla
from sqlalchemy.dialects.postgresql import JSON
from flask import current_app
from qiniu import PersistentFop, op_save, BucketManager
from urlparse import urljoin
from youjiao.flask_qiniu import get_private_url


class MediaMixin(object):
    name = db.Column(sqla.String(200))
    qiniu_key = db.Column(sqla.String(200), unique=True)
    # 处理结果
    media_process = db.Column(JSON) # 不能用process和meta，因为wtform 有这两个属性
    # 媒体资源的元信息
    media_meta = db.Column(JSON)


class Video(CRUDMixin, MediaMixin, db.Model):
    QINIU_CALLBACK_ROUTE = '/qiniu_video_callback'
    id = sqla.Column(sqla.Integer, primary_key=True)

    def convert_mp4(self):
        src_bucket_name = current_app.qiniu.PRIVATE_BUCKET_NAME
        dest_bucket_name = src_bucket_name
        pipeline = current_app.qiniu.PIPELINE
        QINIU_VIDEO_CALLBACK_URL = urljoin(
                current_app.qiniu.CALLBACK_URL, self.QINIU_CALLBACK_ROUTE)
        pfop = PersistentFop(current_app.qiniu.qiniu_auth,
                             src_bucket_name, pipeline,
                             QINIU_VIDEO_CALLBACK_URL)
        saved_key = self.qiniu_key + '.mp4'
        # import ipdb; ipdb.set_trace()
        op = op_save('avthumb/mp4', dest_bucket_name, saved_key.encode('utf-8'))
        ret, info = pfop.execute(self.qiniu_key, [op, ], force=1)
        if info.status_code != 200:
            raise Exception(u'error {}'.format(info))

    @classmethod
    def batch_convert_mp4(cls, ids):
        if len(ids) == 0:
            return 0
        query = cls.query.filter(Video.id.in_(ids))
        for video in query.all():
            video.convert_mp4()
        return query.count()


class Audio(CRUDMixin, MediaMixin, db.Model):

    QINIU_AUDIO_CALLBACK_ROUTE = '/qiniu_audio_callback'

    id = sqla.Column(sqla.Integer, primary_key=True)

    def convert_mp3(self):
        src_bucket_name = current_app.qiniu.PRIVATE_BUCKET_NAME
        dest_bucket_name = src_bucket_name
        QINIU_AUDIO_CALLBACK_URL = urljoin(
            current_app.qiniu.CALLBACK_URL, self.QINIU_AUDIO_CALLBACK_ROUTE)
        pfop = PersistentFop(current_app.qiniu.qiniu_auth, src_bucket_name,
                             notify_url=QINIU_AUDIO_CALLBACK_URL)
        saved_key = self.qiniu_key + '.mp3'
        op = op_save('avthumb/mp3', dest_bucket_name, saved_key.encode('utf-8'))
        ret, info = pfop.execute(self.qiniu_key, [op], force=1)
        if info.status_code != 200:
            raise Exception('error {}'.format(info))
        return True

    @classmethod
    def batch_convert_mp3(cls, ids):
        if len(ids) == 0:
            return 0
        query = cls.query.filter(Audio.id.in_(ids))
        for audio in query.all():
            audio.convert_mp3()
        return query.count()

    @property
    def qiniu_meta(self):
        bucket = BucketManager(current_app.qiniu.qiniu_auth)
        ret, info = bucket.stat(current_app.qiniu.PRIVATE_BUCKET_NAME, self.qiniu_key.encode('utf-8'))
        return info

class Document(CRUDMixin, MediaMixin, db.Model):
    QINIU_DOCUMENT_CALLBACK_ROUTE = '/qiniu_document_convert_pdf_callback'
    id = sqla.Column(sqla.Integer, primary_key=True)

    @property
    def pdf_pic(self):
        if self.media_process and self.media_process.get('pdf'):
            pdf_info = self.media_process.get('pdf')
            page_num = pdf_info.get('page_num')
            key = pdf_info.get('key')
            return [u'{}?odconv/jpg/page/{}/'.format(key, i) for i in range(1, page_num+1)]
        return []

    @property
    def file(self):
        return get_private_url(self.qiniu_key)

    @property
    def pdf_file(self):
        if self.media_process and self.media_process.get('pdf'):
            pdf_info = self.media_process.get('pdf')
            page_num = pdf_info.get('page_num')
            key = pdf_info.get('key')
            return get_private_url(key)
        return []

    def convert_pdf(self):
        src_bucket_name = current_app.qiniu.PRIVATE_BUCKET_NAME
        dest_bucket_name = src_bucket_name
        QINIU_DOCUMENT_CALLBACK_URL = urljoin(
            current_app.qiniu.CALLBACK_URL, self.QINIU_DOCUMENT_CALLBACK_ROUTE)
        pfop = PersistentFop(current_app.qiniu.qiniu_auth, src_bucket_name,
                             notify_url=QINIU_DOCUMENT_CALLBACK_URL)
        saved_key = self.qiniu_key + '.pdf'
        op = op_save('yifangyun_preview', dest_bucket_name, saved_key.encode('utf-8'))
        ret, info = pfop.execute(self.qiniu_key, [op, ], force=1)
        if info.status_code != 200:
            raise Exception('error {}'.format(info))

    @classmethod
    def batch_conver_pdf(cls, ids):
        if len(ids) == 0:
            return 0
        query = cls.query.filter(Document.id.in_(ids))
        for document in query.all():
            document.convert_pdf()
        return query.count()
