from qiniu import Auth

class FlaskQiniu(object):
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        ak = app.config.get('QINIU_AK')
        sk = app.config.get('QINIU_SK')
        self.qiniu_auth = Auth(ak, sk)
        app.qiniu = self
