from pydantic import BaseModel

class Dog(BaseModel):
    id: int
    name: str
    age: float
    color: str
    race: str
    desc: str

    # def __init__(self, id, name, age, color, race, desc):
    #     self.id = id
    #     self.name = name
    #     self.age = age
    #     self.color = color
    #     self.race = race
    #     self.desc = desc