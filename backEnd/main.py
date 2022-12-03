from turtle import color
from unicodedata import name
from fastapi import FastAPI
from models import *

app = FastAPI()

dogsList = [
    Dog(id=1, name="koko", age=12, color="yellow",
        race="husky", desc="good with kids")
]


@app.get("/TestDogsList")
def test1():
    return dogsList


@app.get("/GetDogsList")
def GetDogsList():
    return "http request to get dogs list from DB by dog service"


@app.post("/AddDog")
def AddDog(newDog: Dog):
    return "http request to add new dog to DB by dog service"


@app.post("/EditDog")
def EditDog(updateDog: Dog):
    return "http request to update existing dog in DB by dog service"


@app.post("/RemoveDog")
def RemoveDog(id: int):
    return "http request to remove existing dog in DB by dog service"
