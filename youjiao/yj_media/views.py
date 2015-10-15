# -*- coding: utf-8 -*-
from flask import Blueprint, request, url_for, current_app
from werkzeug.local import LocalProxy
from urlparse import urljoin
from .models import Video, Audio, Document

media_bp = Blueprint('media_bp', __name__)

QINIU_CALLBACK_ROUTE = '/qiniu_video_callback'

QINIU_VIDEO_CALLBACK_URL = LocalProxy(lambda: _get_qiniu_video_callback_url())

def _get_qiniu_video_callback_url():
    return urljoin(current_app.qiniu.CALLBACK_URL, QINIU_CALLBACK_ROUTE)

# TODO: verify it's from qiniu
@media_bp.route(QINIU_CALLBACK_ROUTE, methods=['POST'])
def qiniu_video_callback():
    print('get qiniu callback')
    # import ipdb; ipdb.set_trace()
    # {u'code': 0, u'hash': u'lo3bH-tnSkWCEF8ERjEqj1DkzhaC', u'returnOld': 0,
    #  u'cmd': u'avthumb/mp4|saveas/eW91amlhby12aWRlbzox5bmy57KJ5Yqg5bel54Wu54af6L-H56iLLm1wZy5tcDQ=', u'key': u'1\u5e72\u7c89\u52a0\u5de5\u716e\u719f\u8fc7\u7a0b.mpg.mp4', u'desc': u'The fop was completed successfully'}
    for item in request.json['items']:
        qiniu_key = item['key'][:-4]
        video = Video.query.filter_by(qiniu_key=qiniu_key).first()
        if video:
            video.json = {'private': {'qiniu_key': item['key'], 'status': 'done'}}
            video.save()
    return 'abc'
