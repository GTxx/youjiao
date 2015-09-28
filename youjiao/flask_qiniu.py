from qiniu import Auth
from werkzeug.local import LocalProxy

QINIU_CONFIG = LocalProxy(lambda: _get_qiniu_config())

class FlaskQiniu(object):
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        ak = app.config.get('QINIU_AK')
        sk = app.config.get('QINIU_SK')
        self.qiniu_auth = Auth(ak, sk)
        app.qiniu = self


def _get_qiniu_config():
    # TODO: get qiniu config from app
    return
