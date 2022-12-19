from fastapi import FastAPI
from models import *

app = FastAPI()

#  Hard coded ... remove later
dogsList = [
    # Dog(id=1, name="koko", age=12, color="yellow",
    #     race="husky", desc="good with kids !!!")
]

class Backend:
    @app.get("/v1/TestDogsList")
    def TestDogsList():
        return dogsList


    @app.get("/GetDogsList")
    def GetDogsList():
        return "http request to get dogs list from DB by dog service"


    @app.post("/AddDog")
    def AddDog(newDog: Dog):
        return "http request to add new dog to DB by dog service"


    @app.put("/EditDog")
    def EditDog(updateDog: Dog):
        return "http request to update existing dog in DB by dog service"


    @app.delete("/RemoveDog")
    def RemoveDog(dog_id: int):
        return "http request to remove existing dog in DB by dog service"
