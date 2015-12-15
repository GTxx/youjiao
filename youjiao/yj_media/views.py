# -*- coding: utf-8 -*-
import requests
from flask import Blueprint, request, url_for, current_app
from werkzeug.local import LocalProxy
from urlparse import urljoin
from .models import Video, Audio, Document
import copy


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
    print(request.json)
    for item in request.json['items']:
        qiniu_key = item['key'][:-4]
        video = Video.query.filter_by(qiniu_key=qiniu_key).first()
        if video:
            if video.media_process:
                new_media_process = copy.copy(video.media_process)
            else:
                new_media_process = {}
            new_media_process.update({
                'mp4': {'key': item['key'],
                        'bucket': current_app.qiniu.PRIVATE_BUCKET_NAME,
                        'bucket_attr': 'private'}})
            video.media_process = new_media_process
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


@media_bp.route(Video.QINIU_CUT_VIDEO_CALLBACK, methods=['POST'])
def qiniu_cut_video_callback():
    '''
    {
    u'pipeline': u'1380451545.youjiaoavprocess',
    u'code': 0,
    u'items': [
        {
            u'code': 0,
            u'hash': u'lnVxhkoDzrKRTkIwjMqDbnz_xH8Y',
            u'returnOld': 0,
            u'cmd': u'avthumb/mp4/t/180|saveas/eW91amlhby12aWRlbzrliqjnianov4flhqzlkIjmiJAud212Lm1wNC5zaG9ydC5tcDQ=',
            u'key': u'\u52a8\u7269\u8fc7\u51ac\u5408\u6210.wmv.mp4.short.mp4',
            u'desc': u'Thefopwascompletedsuccessfully'
        }
    ],
    u'reqid': u'WTEAAJb6aEjqfh4U',
    u'inputBucket': u'youjiao-video',
    u'inputKey': u'\u52a8\u7269\u8fc7\u51ac\u5408\u6210.wmv.mp4',
    u'id': u'z0.566935fa7823de6ae317ee9e',
    u'desc': u'Thefopwascompletedsuccessfully'
    }
    '''
    inputKey = request.json['inputKey']
    video = Video.query.filter_by(qiniu_key=inputKey).first()
    if not video:
        return 'ok'
    if video.media_process:
        new_media_process = copy.copy(video.media_process)
    else:
        new_media_process = {}
    for item in request.json['items']:
        new_media_process.update({
            'short mp4': {'key': item['key'],
                          'bucket': current_app.qiniu.PRIVATE_BUCKET_NAME,
                          'bucket_attr': 'private'}})
        print(new_media_process)
        video.media_process = new_media_process
        video.save()
    return 'ok'