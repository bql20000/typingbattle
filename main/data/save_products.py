"""
Save products information into database to save API calls .
Product information includes: price, rating, url, thumbnail, title, currency
"""


import json
import logging

from mysql.connector import MySQLConnection, Error
from config.dbconfig import read_db_config


n_data_files = 2
product_id = 0


def insert_product(product_id, title, thumbnail, rating, total_reviews, url, currency, price, conn):
    query = f'INSERT INTO product VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
    cursor = conn.cursor()
    cursor.execute(query, (product_id, title, thumbnail, rating, total_reviews, url, currency, price))
    cursor.close()


try:
    import os
    conn = MySQLConnection(**read_db_config(filename='../../config/config.ini'))
    if conn.is_connected():
        print('Connection established.')

    for i in range(n_data_files):
        with open(f'./products/amazon-products-{i}.json') as json_file:
            data = json.load(json_file)
            products = data['products']
            for item in products:
                title = str(item['title'])
                thumbnail = item['thumbnail']
                rating = float(item['reviews']['rating'])
                url = item['url']
                price = float(item['price']['current_price'])
                currency = item['price']['currency']
                total_reviews = item['reviews']['total_reviews']
                product_id += 1
                insert_product(product_id, title, thumbnail, rating, total_reviews, url, currency, price, conn)

    conn.commit()
    conn.close()
except Error as e:
    logging.exception(e)
