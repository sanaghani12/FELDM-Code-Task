from dbconnection_SQLite import db_connect
from sqlite3 import Error
try:
    db_path = './data/transactions.db'
    db_connection = db_connect(db_path)

    cursor = db_connection.cursor()
    cursor.execute('''SELECT max(s_rev),visitor_id 
                      FROM (select sum(revenue) as s_rev,visitor_id from transactions 
                      GROUP BY visitor_id)''')
    revenue, visitor_id = cursor.fetchone()
    print('Following is the id for the Visitor with the highest revenue: ', visitor_id )
    print('The revenue for the above visitor is: ', revenue )

except Error as e:
    print(e)

finally:
    db_connection.close()


