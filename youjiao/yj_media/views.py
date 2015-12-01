# -*- coding: utf-8 -*-
import requests
from flask import Blueprint, request, url_for, current_app
from werkzeug.local import LocalProxy
from urlparse import urljoin
from .models import Video, Audio, Document

media_bp = Blueprint('media_bp', __name__)

QINIU_CALLBACK_ROUTE = '/qiniu_video_callback'
QINIU_DOCUMENT_CALLBACK_ROUTE = '/qiniu_document_callback'

QINIU_VIDEO_CALLBACK_URL = LocalProxy(lambda: _get_qiniu_video_callback_url())

def _get_qiniu_video_callback_url():
    return urljoin(current_app.qiniu.CALLBACK_URL, QINIU_CALLBACK_ROUTE)

# TODO: verify it's from qiniu
@media_bp.route(Video.QINIU_CALLBACK_ROUTE, methods=['POST'])
def qiniu_video_callback():
    print('get qiniu callback')
    # import ipdb; ipdb.set_trace()
    for item in request.json['items']:
        qiniu_key = item['key'][:-4]
        video = Video.query.filter_by(qiniu_key=qiniu_key).first()
        if video:
            video.media_process = {'mp4': {'key': item['key'],
                                  'bucket': current_app.qiniu.PRIVATE_BUCKET_NAME,
                                  'bucket_attr': 'private'}}
            video.save()
    return 'abc'

# TODO: verify it's from qiniu
@media_bp.route(Document.QINIU_DOCUMENT_CALLBACK_ROUTE, methods=['POST'])
def qiniu_document_callback():
    print('get qiniu document callback')
    # import ipdb; ipdb.set_trace()
    for item in request.json['items']:
        qiniu_key = item['key'][:-4]
        document = Document.query.filter_by(qiniu_key=qiniu_key).first()
        if document:
            from .utils import get_private_url
            url = get_private_url((item['key']+u'?odconv/jpg/info').encode('utf-8'))
            response = requests.get(url)
            document.media_process = {'pdf': {'key': item['key'],
                                     'bucket': current_app.qiniu.PRIVATE_BUCKET_NAME,
                                     'bucket_attr': 'private',
                                     'page_num': response.json().get('page_num')}}
            document.save()
    return 'abc'

@media_bp.route(Audio.QINIU_AUDIO_CALLBACK_ROUTE, methods=['POST'])
def qiniu_audio_callback():
    for item in request.json['items']:
        qiniu_key = item['key'][:-4]
        audio = Audio.query.filter_by(qiniu_key=qiniu_key).first()
        if audio:
            audio.media_process = {'mp3': {'key': item['key'],
                                  'bucket': current_app.qiniu.PRIVATE_BUCKET_NAME,
                                  'bucket_attr': 'private'}}
            audio.save()
    return 'abc'