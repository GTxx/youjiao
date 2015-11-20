from qiniu import Auth
from flask import current_app
from urlparse import urljoin
import urllib


class FlaskQiniu(object):
    def __init__(self, app=None):
        self._state = {}
        if app:
            self.init_app(app)

    def init_app(self, app):
        for key, value in app.config.items():
            if key.startswith('QINIU'):
                self._state[key] = value
        self.qiniu_auth = Auth(self.AK, self.SK)
        app.qiniu = self

    def __getattr__(self, item):
        name = 'QINIU_' + item
        return self._state[name]


def get_private_url(key):
    if not key:
        return ''
    q = current_app.qiniu.qiniu_auth
    PRIVATE_DOMAIN = current_app.qiniu.PRIVATE_CDN_DOMAIN
    url = urljoin(PRIVATE_DOMAIN, key)
    res = q.private_download_url(url.encode('utf-8'), expires=3600)
    return res.decode('utf-8')
