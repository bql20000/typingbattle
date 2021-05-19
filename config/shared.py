from config.dbconfig import read_db_config


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SEND_FILE_MAX_AGE_DEFAULT = 0
    JWT_EXPIRATION_PERIOD = 24 * 3600
    db_config = read_db_config()
    SQLALCHEMY_DATABASE_URI = f'mysql://{db_config["user"]}:{db_config["password"]}' \
                              f'@{db_config["host"]}/{db_config["database"]}'
    BLACKLISTED_TOKENS = []
    DEBUG = False
    TESTING = False

    LOGGING_FILE = ''
    LOGGING_LEVEL = 10  # DEBUG
