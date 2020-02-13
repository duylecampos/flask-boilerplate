import os


class Config:
    DEBUG = True
    ENVIRONMENT = "develop"
    APP_NAME = os.environ.get("APP_NAME", "Flask-Boilerplate")
    SECRET_KEY = os.environ.get("SECRET_KEY", "NOT_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
