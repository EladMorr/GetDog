import mysql.connector
from fastapi import FastAPI
import json
from pydantic import BaseModel
import pandas as pd
from models import *

app = FastAPI()


def conn():
    try:
        cnx = mysql.connector.connect(
            user='root', password='2705', host='mysql')
        cursor = cnx.cursor()
        return cursor, cnx
    except Exception as e:
        return "Failed to create connection Error: {0}".format(e)


def createDB():
    cursor, cnx = conn()
    cursor.execute("CREATE DATABASE dogs")
    cnx = mysql.connector.connect(
        user='root', password='2705', host='mysql', database='dogs')
    cursor = cnx.cursor()
    cursor.execute('''
        CREATE TABLE `dogs`.`dogs` (
        `cheap_number` INT NOT NULL,
        `name` VARCHAR(45) NOT NULL,
        `image` VARCHAR(1000) NOT NULL,
        `age` FLOAT NOT NULL,
        `color` VARCHAR(45) NOT NULL,
        `race` VARCHAR(45) NOT NULL,
        `about` VARCHAR(45) NOT NULL,
        `phone_number` VARCHAR(45) NOT NULL,
        `owner_name` VARCHAR(45) NOT NULL,
        `price` VARCHAR(45) NOT NULL,
        PRIMARY KEY (`cheap_number`));
    ''')

    cursor.close()
    cnx.close()


def database_exists():
    try:
        cursor, cnx = conn()
        cursor.execute("SHOW DATABASES")
        databases = [row[0] for row in cursor]

        if 'dogs' in databases:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()


@app.get("/check")
def check():
    try:
        if database_exists():
            return "Database exists"
        else:
            # create the db because it doesn't exists
            createDB()
            return "Database not found, new db called dogs created"
    except:
        return "Any issue with the connection"


@app.post("/v1/AddDog")
def AddDog(newDog: Dog):
    cursor, cnx = conn()
    cnx = mysql.connector.connect(
        user='root', password='2705', host='mysql', database='dogs')
    cursor = cnx.cursor()
    try:
        cursor.execute(
            f'''
            INSERT INTO `dogs`.`dogs` 
            (`cheap_number`, `name`, `image`, `age`, `color`, `race`, `about`, `phone_number`, `owner_name`, `price`) 
            VALUES (
            '{newDog.cheap_number}',
            '{newDog.name}',
            '{newDog.image}',
            '{newDog.age}',
            '{newDog.color}',
            '{newDog.race}',
            '{newDog.about}',
            '{newDog.phone_number}',
            '{newDog.owner_name}',
            '{newDog.price}');
            '''
        )
        cnx.commit()
        return "Success"

    except Exception as e:
        return f"cannot return newDog, Error:{e}"

    finally:
        cursor.close()
        cnx.close()

@app.get('/v1/getDogs')
def getDogs():
    cnx = mysql.connector.connect(
        user='root', password='2705', host='mysql', database='dogs')
    cursor = cnx.cursor()
    try:
        cursor.execute(
            "SELECT * FROM dogs"
        )
        
        rows = cursor.fetchall()
        data = {cursor.column_names[i]: [row[i] for row in rows]
                for i in range(len(cursor.column_names))}

        # Convert the dictionary to a dataframe
        df = pd.DataFrame(data)  
        json_obj = df.to_json()
        return json_obj
        
    except:
        return "cannot get dog list"
    finally:
        cursor.close()
        cnx.close()


@app.put('/v1/EditDogs')
def EditDogs(updated_dog : Dog):
    cursor, cnx = conn()
    cnx = mysql.connector.connect(
        user='root', password='2705', host='mysql', database='dogs')
    cursor = cnx.cursor()
    try:
        cursor.execute(
            f'''
            UPDATE dogs SET name = '{updated_dog.name}',
            image = '{updated_dog.image}', age = '{updated_dog.age}', color = '{updated_dog.color}',
            race = '{updated_dog.race}', about = '{updated_dog.about}', phone_number = '{updated_dog.phone_number}',
            owner_name = '{updated_dog.owner_name}', price = '{updated_dog.price}'
            WHERE cheap_number = {updated_dog.cheap_number}
            '''
        )
        
        cnx.commit()
        return "Success"

    except:
        return "cannot update dog"

    finally:
        cursor.close()
        cnx.close()

@app.delete('/v1/RemoveDog/{cheap_number}')
def DeleteDog(cheap_number : int):
    cursor, cnx = conn()
    cnx = mysql.connector.connect(
        user='root', password='2705', host='mysql', database='dogs')
    cursor = cnx.cursor()

    try:
        cursor.execute(
           f'''
           DELETE FROM dogs WHERE cheap_number = {cheap_number}
           ''' 
        )
        cnx.commit()
        return "Dog removed"
    
    except:
        return "cannot remove dog"
    
    finally:
        cursor.close()
        cnx.close()