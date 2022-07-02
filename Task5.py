import sys
import dbconnection_postgres
import dbconnection_SQLite
from sqlite3 import Error
try:
    if sys.argv[1] == 'sqlite':
        db_path = './data/transactions.db'
        db_connection = dbconnection_SQLite.db_connect(db_path)
    elif sys.argv[1] == "postgres":
        db_connection = dbconnection_postgres.db_connect()
    else:
        print("Please specify the database name in the argument as 'sqlite' or 'postgres'")
        exit()

    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM "Devices";')
    print('Following is the query result: ', cursor.fetchall())

except Error as e:
    print(e)

finally:
    db_connection.close()