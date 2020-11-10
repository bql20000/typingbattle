import csv, logging

from mysql.connector import MySQLConnection, Error
from config.dbconfig import read_db_config


def insert_word(word_id, value, conn):
    query = f'INSERT INTO word VALUES(%s, %s)'
    cursor = conn.cursor()
    cursor.execute(query, (word_id, value))
    cursor.close()


try:
    conn = MySQLConnection(**read_db_config())
    if conn.is_connected():
        print('Connection established.')

    with open('main/data/english-word-list-total.csv', mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[0]:
                insert_word(row[0], row[1], conn)

    conn.commit()
    conn.close()
except Error as e:
    logging.exception(e)
