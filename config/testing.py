from config.shared import Config
from config.dbconfig import read_db_config


class TestingConfig(Config):
    TESTING = True
    db_config = read_db_config()
    SECRET_KEY = 'test_key'
    SQLALCHEMY_DATABASE_URI = f'mysql://{db_config["user"]}:{db_config["password"]}' \
                              f'@{db_config["host"]}/{db_config["database"]}'


config = TestingConfig
