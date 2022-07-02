from dbconnection_SQLite import db_connect
from sqlite3 import Error
import csv

try:
    db_path = './data/transactions.db'
    db_connection = db_connect(db_path)

    cursor = db_connection.cursor()
    cursor.execute('''SELECT T.*, D.device_name FROM transactions T, devices D
                      ON T.device_type = D.id''')
    with open("./data/devices_and_transactions.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)

except Error as e:
    print(e)

finally:
    db_connection.close()
