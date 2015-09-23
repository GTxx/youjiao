class BaseConfig(object):
    # Create dummy secrey key so we can use sessions
    SECRET_KEY = '123456790'

    # DEBUG
    DEBUG = True

    # Create in-memory database
    SQLALCHEMY_DATABASE_URI = 'postgresql://youjiao_db_admin:123@localhost/youjiao_db'
    SQLALCHEMY_ECHO = True

    # for user register and login security
    # SECURITY_REGISTERABLE = False # overide flask_security register with custom register
    PASSWORD_HASH = "pbkdf2_sha512"
    PASSWORD_SALT = "W0dRBgO0Ukobw8NweLAXvqug2ZTh97HZIEMFcEsWhf7lt68"
    # SECURITY_CONFIRMABLE = False  # disable email confirm
    # SECURITY_SEND_REGISTER_EMAIL = False  # disable email confirm

    # flask_wtf
    WTF_CSRF_CHECK_DEFAULT = False

    # flask_babel
    BABEL_DEFAULT_LOCALE = 'zh'

    # flask_redis
    REDIS_URL = 'redis://localhost:6379/0'

try:
    from youjiao.config.local_config import LocalConfig

    class Config(LocalConfig, BaseConfig):
        pass


except Exception as e:
    print(e)
    class Config(BaseConfig):
        pass
