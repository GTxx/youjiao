from qiniu import Auth


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
