import sqlite3
from sqlite3 import Error

def db_connect(path):
    try:
        connection = sqlite3.connect(path)
        print('Connection to SQLite DB successful')
        return connection
    except Error as e:
        print(f'The error {e} occurred')
        print('Database connection not successful')
        return None

