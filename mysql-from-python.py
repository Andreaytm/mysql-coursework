import os
import datetime
import pymysql 

# Get username from Cloud9 workspace 
# (modify this variable if running on another environement)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host = 'localhost',
                            user = username, 
                            password = '',
                            db = 'Chinook')
try:
    with connection.cursor() as cursor:
        rows = [('Julie', 35, "1980-04-22 22:02:30"),
                ('Katy', 44, "1972-03-27 10:11:11"),
                ('Leanne', 87, "1938-11-15 05:03:17")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the code above was successful
    connection.close()