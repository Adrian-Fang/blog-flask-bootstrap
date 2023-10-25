import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    # SECRET_KEY = "development"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "development"
    # SQLALCHEMY_DATABASE_URI = "sqlite:///flaskr.sqlite3"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URI"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


class StagingConfig(Config):
    TESTING = True
    DEBUG = True


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
