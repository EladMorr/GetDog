from fastapi import FastAPI
import requests
import json
from pydantic import BaseModel

from models import *

app = FastAPI()


class Backend:
    @app.get('/v1/call')
    def call():
        r = requests.get("http://database/send")
        return r.text

    @app.get("/v1/TestDogsList")
    def TestDogsList():
        return "dogsList"

    @app.get("/v1/GetDogsList")
    def GetDogsList():
        r = requests.get("http://database/v1/getDogs")
        return r.json()

    @app.post("/v1/AddDog")
    def AddDog(newDog: Dog):
        r = requests.post("http://database/v1/AddDog", data=json.dumps(newDog.__dict__), headers={
                  'Content-Type': 'application/json'
        })
        return r.text

    @app.put("/v1/EditDog")
    def EditDog(updateDog: Dog):
        r = requests.put("http://database/v1/EditDogs",
                          data=json.dumps(updateDog.__dict__), headers={
                              'Content-Type': 'application/json'
                          })
        return r.text

    @app.delete("/v1/RemoveDog/{cheap_number}")
    def RemoveDog(cheap_number: int):
        r = requests.delete("http://database/v1/RemoveDog/" + str(cheap_number))
        return r.text

    @app.get("/v1/check")
    def check():
        r = requests.get("http://database/check")
        return r.text
