class BaseConfig(object):
    # Create dummy secrey key so we can use sessions
    SECRET_KEY = '123456790'

    # DEBUG
    DEBUG = True

    # Create in-memory database
    SQLALCHEMY_DATABASE_URI = 'postgresql://youjiao_db_admin:123@localhost/youjiao_db'
    SQLALCHEMY_ECHO = True

    # for user register and login security
    PASSWORD_HASH = "pbkdf2_sha512"
    PASSWORD_SALT = "W0dRBgO0Ukobw8NweLAXvqug2ZTh97HZIEMFcEsWhf7lt68"

    # flask_wtf
    WTF_CSRF_CHECK_DEFAULT = False

    # flask_babel
    BABEL_DEFAULT_LOCALE = 'zh_CN'

    # flask_redis
    REDIS_URL = 'redis://localhost:6379/0'

    # flask_qiniu
    QINIU_AK = 'ak'
    QINIU_SK = 'sk'
    QINIU_PIPELINE = 'pipeline'
    QINIU_CALLBACK_URL = 'call back url'
    QINIU_PUBLIC_BUCKET_NAME = 'public bucket name'
    QINIU_PUBLIC_CDN_DOMAIN = 'public domain name'

    QINIU_PRIVATE_BUCKET_NAME = 'private bucket name'
    QINIU_PRIVATE_CDN_DOMAIN = 'private domain name'




try:
    from youjiao.config.local_config import LocalConfig

    class Config(LocalConfig, BaseConfig):
        pass


except Exception as e:
    print(e)
    class Config(BaseConfig):
        pass
