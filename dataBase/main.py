from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error

app = FastAPI()


mydb = mysql.connector.connect(
    host="localhost",
    user="myusername",
    password="mypassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
