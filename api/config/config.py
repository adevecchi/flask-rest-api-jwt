class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'JWT-SECRET-KEY'
    SECRET_KEY = 'SECRET-KEY'
    SECURITY_PASSWORD_SALT = 'SECURITY-PASSWORD-SALT'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<your_username>:<your_password>@localhost:3306/luizalabs'
    SQLALCHEMY_ECHO = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:devecchi@localhost:3306/dev_luizalabs'
    SQLALCHEMY_ECHO = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<your_username>:<your_password>@localhost:3306/test_luizalabs'
    SQLALCHEMY_ECHO = False