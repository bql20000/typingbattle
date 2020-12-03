import os
from configparser import ConfigParser


def read_db_config(filename='config/config.ini'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read configuration file
    parser = ConfigParser()
    parser.read(filename)
    env = os.getenv("ENVIRONMENT", "development")
    section = f'mysql-{env}'

    # print(parser.sections())

    # read configuration from mysql section
    if parser.has_section(section):
        items = parser.items(section)
        return {item[0]: item[1] for item in items}
    else:
        raise Exception(f'{section} not found in {filename}.')
