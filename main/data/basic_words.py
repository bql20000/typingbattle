"""
This module saves 500 english words in common-english-words.csv
to the database. In production, this file will have no effects on
the application's behaviors.
"""

import csv
import logging

from mysql.connector import MySQLConnection, Error
from config.dbconfig import read_db_config


def insert_word(word_id, value, conn):
    return
    query = f'INSERT INTO word VALUES(%s, %s)'
    cursor = conn.cursor()
    cursor.execute(query, (word_id, value))
    cursor.close()


try:
    import os
    print(os.curdir)
    conn = MySQLConnection(**read_db_config())
    if conn.is_connected():
        print('Connection established.')

    with open('main/data/common-english-words.csv', mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[0]:
                insert_word(row[0], row[1], conn)

    conn.commit()
    conn.close()
except Error as e:
    logging.exception(e)
