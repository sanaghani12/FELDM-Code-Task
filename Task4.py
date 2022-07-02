from dbconnection_SQLite import db_connect
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup
from datetime import datetime
import csv


def readxmldata():
    with open('./data/eurofxref-hist-90d.xml', 'r') as f:
        data = f.read()
    XML_data = BeautifulSoup(data, "xml")
    return XML_data


def get_date_list_from_XML(XML_data):
    time_values = []
    xml_elements = XML_data.find('Cube').contents
    for x in xml_elements:
        try:
            time_values.append(datetime.strptime(x.get('time'), '%Y-%m-%d'))
        except AttributeError:  # For strings that do not contain time attribute.
            continue
        except Error as e:
            print(e)
    return time_values


def get_date_for_currency_conversion(date_list, date_value_in_db):
    return min(date_list, key=lambda x: abs(x - datetime.strptime(date_value_in_db, '%Y-%m-%d %H:%M:%S')))


def get_rate_for_currency_conversion(closest_date_in_xml, currency):
    b_name = XML_data.find('Cube', {'time': closest_date_in_xml.date()}).find('Cube', {'currency': currency})
    return b_name.get('rate')


try:
    db_path = './data/transactions.db'
    db_connection = db_connect(db_path)
    db_connection.row_factory = sqlite3.Row

    cursor1 = db_connection.cursor()
    cursor2 = db_connection.cursor()
    cursor1.execute("SELECT id, datetime,revenue FROM transactions")

    XML_data = readxmldata()

    # extract complete list of dates from XML data
    date_list = get_date_list_from_XML(XML_data)

    while True:
        row = cursor1.fetchone()
        if row:
            date_value_in_db = row['datetime']
            closest_date_in_xml = get_date_for_currency_conversion(date_list, date_value_in_db)
            conversion_rate = get_rate_for_currency_conversion(closest_date_in_xml, 'USD')

            print("DB date time: ", row['datetime'], "Closest date in XML: ", closest_date_in_xml, "conversion_rate: ",
                  conversion_rate)
            cursor2.execute('''UPDATE transactions
                             SET revenue = revenue/?
                             WHERE
                             id=?''', (conversion_rate, row['id']))

        else:
            break

except Error as e:
    print(e)

finally:
    db_connection.commit()
    db_connection.close()
