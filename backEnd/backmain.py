from fastapi import FastAPI
from models import *

app = FastAPI()

#  Hard coded ... remove later
dogsList = [
    Dog(1, "Koko", 2.4, "yellow", "husky", "good with kids !!!")
]


class Backend:
    @app.get("/v1/TestDogsList")
    async def TestDogsList():
        return dogsList

    @app.get("/GetDogsList")
    async def GetDogsList():
        return "http request to get dogs list from DB by dog service"

    @app.post("/AddDog/")
    async def AddDog(newDog: Dog):
        return "http request to add new dog to DB by dog service"

    @app.put("/EditDog")
    async def EditDog(updateDog: Dog):
        return "http request to update existing dog in DB by dog service"

    @app.delete("/RemoveDog")
    async def RemoveDog(dog_id: int):
        return "http request to remove existing dog in DB by dog service"
