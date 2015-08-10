class BaseConfig(object):
    # Create dummy secrey key so we can use sessions
    SECRET_KEY = '123456790'

    # Create in-memory database
    DATABASE_FILE = 'sample_db.sqlite'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
    SQLALCHEMY_ECHO = True

try:
    from .local_config import LocalConfig

    class Config(LocalConfig, BaseConfig):
        pass


except Exception as e:
    class Config(BaseConfig):
        pass
