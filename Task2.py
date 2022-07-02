from dbconnection_SQLite import db_connect
from sqlite3 import Error
try:
    db_path = './data/transactions.db'
    db_connection = db_connect(db_path)

    cursor = db_connection.cursor()
    cursor.execute('''SELECT max(R),DATE(datetime)
                      FROM (select datetime, sum(revenue) as R FROM transactions T,devices D 
                      ON T.device_type = D.id 
                      WHERE device_name = 'Mobile Phone'
                      GROUP BY datetime)''')
    revenue, date = cursor.fetchone()
    print('Following is the date with highest revenue for users who ordered via mobile phone: ', date )
    print('The revenue for that date is : ', revenue )

except Error as e:
    print(e)

finally:
    db_connection.close()
