from pydantic import BaseModel

class Dog(BaseModel):
    id: int
    name: str
    age: float
    color: str
    race: str
    desc: str
