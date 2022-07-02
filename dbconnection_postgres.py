import psycopg2
from config import config

def db_connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connection to PostgreSQL database successful')
        conn = psycopg2.connect(**params)
        return conn

    except (Exception, psycopg2.DatabaseError) as e:
        print(f'The error {e} occurred')
        print('Database connection not successful')
        return None


