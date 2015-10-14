# -*- coding: utf-8 -*-
from flask import Blueprint, request, url_for
from .models import Video, Audio, Document

media_bp = Blueprint('media_bp', __name__)

QINIU_CALLBACK_ROUTE = '/qiniu_video_callback'


@media_bp.route(QINIU_CALLBACK_ROUTE)
def qiniu_video_callback():
    import ipdb; ipdb.set_trace()
    return 'abc'
