from config.default import DefaultConfig
from config.dbconfig import read_db_config


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    db_config = read_db_config()
    SQLALCHEMY_DATABASE_URI = f'mysql://{db_config["user"]}:{db_config["password"]}' \
                              f'@{db_config["host"]}/{db_config["database"]}'


config = DevelopmentConfig
