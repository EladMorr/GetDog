from pydantic import BaseModel


class Dog(BaseModel):
    cheap_number: int
    image: str
    name: str
    color: str
    age: float
    race: str
    about: str
    phone_number: str
    owner_name: str
    price: str
