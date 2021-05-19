from config.shared import Config


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'test_key'


config = TestingConfig
