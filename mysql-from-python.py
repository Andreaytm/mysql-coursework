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
        cursor.execute("UPDATE Friends SET age=%s WHERE name=%s;",
                        (23, 'Bob'))
        connection.commit()
finally:
    # Close the connection, regardless of whether the code above was successful
    connection.close()