from config.default import DefaultConfig
from config.dbconfig import read_db_config


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    db_config = read_db_config()
    SECRET_KEY = '495DE9B3D0D6BB7480F90D0B373EA4438F76798DCE81337449434D78460C046A'
    SQLALCHEMY_DATABASE_URI = f'mysql://{db_config["user"]}:{db_config["password"]}' \
                              f'@{db_config["host"]}/{db_config["database"]}'


config = DevelopmentConfig
