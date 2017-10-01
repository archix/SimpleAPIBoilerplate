import os


class Config:
    DEBUG = True

    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "secret"

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))

    # ***** ROUTES PREFIX ******
    APPLICATION_ROOT = '/api'

    # ********** DATABASE ***********************
    DB_USER = 'admin'
    DB_PASSWORD = 'admin'
    DB_HOST = 'localhost'
    DB_NAME = 'test_api'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

    # ********** UPLOAD *************************
    IMAGE_ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif']
    IMAGE_UPLOAD_FOLDER = '/images'

    # ********** TESTING ************************
    TESTING = False
    # Used in testing. When this is true and client submits a solutions,

    # ********** JWT ****************************
    SECRET_KEY = '\::b)yV-."#!Finn-6SD-9(dE>O+-S8I,):6}@kfUw;0v\h:4EZU0;1cOv)zag&'

    # ********** EMAIL ****************
    EMAIL_PROVIDER = 'mailjet'
    EMAIL_FROM = 'notheardis66@teleworm.us'
    EMAIL_FROM_NAME = 'Mailer Api'

    # ********** MAILJET ************************
    MAILJET_PUBLIC_KEY = '288c7a7e15eaf87e9808f26bc8d5dba0'
    MAILJET_SECRET_KEY = '67ff5f53864a84c73be3c1b39a56a83c'

    # ********** FRONTEND ***********************
    FRONTEND_URL = 'http://some-url.com/confimation'


class LocalConfig(Config):
    """ Umbrella config for all local runs, vagrant runs and unit testing runs """
    pass


class ProductionConfig(Config):
    """ Config used in production environment """
    DEBUG = False


config = {
    'local': LocalConfig,
    'production': ProductionConfig
}

SELECTED_CONFIG = os.getenv('API_ENV', 'local')

