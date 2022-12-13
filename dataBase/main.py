from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error

app = FastAPI()

try:
    connection = mysql.connector.connect(host='localhost:3305',
                                         database='dog_db',
                                         user='root',
                                         password='1542')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
