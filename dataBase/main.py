from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error

app = FastAPI()


# import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='1542', host='127.0.0.1', database='dog_db'
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)

#Closing the connection
conn.close()


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password=1542,
#   database="dog_db"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# try:
#     connection = mysql.connector.connect(host='localhost:3305',
#                                          database='dog_db',
#                                          user='root',
#                                          password='1542')
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)

# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")
