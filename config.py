import os

class DevelopmentConfig:
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
