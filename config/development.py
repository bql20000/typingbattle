from config.shared import Config
from config.dbconfig import read_db_config


class DevelopmentConfig(Config):
    DEBUG = True
    db_config = read_db_config()
    SECRET_KEY = 'dev_key'
    SQLALCHEMY_DATABASE_URI = f'mysql://{db_config["user"]}:{db_config["password"]}' \
                              f'@{db_config["host"]}/{db_config["database"]}'


config = DevelopmentConfig
