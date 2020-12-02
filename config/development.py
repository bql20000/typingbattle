from config.shared import Config


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'dev_key'


config = DevelopmentConfig
