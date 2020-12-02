from config.shared import Config
from config.dbconfig import read_db_config


class ProductionConfig(Config):
    db_config = read_db_config()
    SECRET_KEY = '96656add40140f5eb0124545c05d217368bb6412124bc67f9b44b8321086fc0b'
    SQLALCHEMY_DATABASE_URI = f'mysql://{db_config["user"]}:{db_config["password"]}' \
                              f'@{db_config["host"]}/{db_config["database"]}'


config = ProductionConfig
