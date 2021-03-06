"""
This module saves 18 measurement units in units.txt
to the database. In production, this file will have no effects on
the application's behaviors.
"""

import logging

from mysql.connector import MySQLConnection, Error
from config.dbconfig import read_db_config


def insert_word(word_id, value, conn):
    query = 'INSERT INTO unit VALUES(%s, %s)'
    cursor = conn.cursor()
    cursor.execute(query, (word_id, value))
    cursor.close()


try:
    conn = MySQLConnection(**read_db_config(filename='config/config.ini'))

    print('Saving unit system to database ... ', end='')
    file = open('data/units.txt', 'r')
    for i, row in enumerate(file, 1):
        insert_word(i, row[:-1], conn)

    conn.commit()
    conn.close()
    print('FINISH!')
except Error as e:
    logging.exception(e)
