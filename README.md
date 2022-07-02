# FELD M - TECH TASKS

Author: Sana Ghani

### Prerequisites:
* Please check requirements.txt for python library dependencies. 
* To install, run `pip install -r requirements.txt`.
* For Task 5, Postgres database should be installed. 

### Task 1
#### Write a Python script to find out which visitor created the most revenue. 
#### Note: A simple print of the result to the console is sufficient.

To execute the task, run `python3 Task1.py`. 

Screenshot of the result:
![image](https://user-images.githubusercontent.com/91886253/176982544-e817c6de-1140-4acd-8dc0-7599a8f181ae.png)

### Task 2
#### Write a Python script to find out on which day most revenue for users who ordered via a mobile phone was created.
#### Note: a simple print of the result to the console is sufficient.

To execute the task, run `python3 Task2.py`. 

Screenshot of the result:
![image](https://user-images.githubusercontent.com/91886253/176982416-a50ca5a0-710d-4e09-8565-b294c6894f77.png)

### Task 3

#### Write a Python script that combines the contents of Devices and Transactions and store it as a single flat file including the column names.

To execute the task, run `python3 Task3.py`.

The output of the task is saved as a csv file inside the data folder as "devices_and_transactions.csv".

### Task 4
#### As stated in the SQL comments the created revenue is currently stored in USD.
#### Update the data stored in the database to have the created revenue in EUR.
#### You can use the following resource to fetch the currency conversion rates:
#### https://transfer.feld-m.de/fbsharing/Bzu2Zj3y

For this task, I have used the library "BeautifulSoup" to parse the XML file in Python.

* First, I extracted the dates for which conversion rates are available in the XML file and stored these dates in a list.
* For each row in the 'Transactions' table, we find the nearest date for which conversion rate is available (using the list in previous step).
* Then we use that date's conversion rate to update the revenue in EUR in the database.

* To execute this task, run `python3 Task4.py`. 
* Below screenshot shows the values of the 'datetime' column in DB, the nearest date in XML, and the conversion rate for updating the 'revenue' in the database.
![image](https://user-images.githubusercontent.com/91886253/176983847-a14583c4-1bac-4514-adef-e46e3c3431b5.png)
* The database is updated with the revenue in currency 'EUR' according to the conversion rates in the provided XML.

### Task 5

#### Imagine you have to add support for other DBMS, how would you address this request?
#### Write a Python script that exemplarily uses PostgreSQL.
#### 

* For this task, we have used PostgreSQL database.
* SQL file is created for database migration from sqlite to Postgres. You can find the DBMigrationScriptForPostgres.sql file in the data folder.
* To import the DBMigrationScriptForPostgres.sql, following command can be used in psql: 
  ```
  \i '<path_to_sql_file>/DBMigrationScriptForPostgres.sql'
  ```
* The credentials for the postgres database have to be included in the "database.ini" file.
* The code is designed to support both "sqlite" and "postgres" database (using command line arguments).
* To execute the task with postgres data, run `python3 Task5.py postgres`.

Screenshot of the result:
![image](https://user-images.githubusercontent.com/91886253/176983190-962d6abe-7aa0-425d-8d9e-f5ab19280363.png)

* To execute the task with sqlite data, run `python3 Task5.py sqlite`.

Screenshot of the result:
![image](https://user-images.githubusercontent.com/91886253/176983257-abdc9fec-7b42-4dbe-9320-5875e149e4c1.png)

