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
        rows = [(27, 'Bob'),
                (33, 'Jim'),
                (25, 'Fred')]
        cursor.executemany("UPDATE Friends SET age=%s WHERE name=%s;", rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the code above was successful
    connection.close()