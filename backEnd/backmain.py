from fastapi import FastAPI
from models import *

app = FastAPI()

#  Hard coded ... remove later
dogsList = [
    Dog(1, "Koko", 2.4, "yellow", "husky", "good with kids !!!")
]


class Backend:
    @app.get("/v1/TestDogsList")
    def TestDogsList():
        return dogsList

    @app.get("/v1/GetDogsList")
    def GetDogsList():
        return "http request to get dogs list from DB by dog service"

    @app.post("/v1/AddDog")
    def AddDog(newDog: Dog):
        return "http request to add new dog to DB by dog service"

    @app.put("/v1/EditDog")
    def EditDog(updateDog: Dog):
        return "http request to update existing dog in DB by dog service"

    @app.delete("/v1/RemoveDog")
    def RemoveDog(dog_id: int):
        return "http request to remove existing dog in DB by dog service"
