from config.shared import Config


class ProductionConfig(Config):
    SECRET_KEY = '96656add40140f5eb0124545c05d217368bb6412124bc67f9b44b8321086fc0b'


config = ProductionConfig
