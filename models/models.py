from pydantic import BaseModel

class Dog(BaseModel):
    cheap_number: int
    images: str
    names: str
    colors: str
    ages: float
    race: str
    about: str
    phone_number : str
    owner_name : str
    price : str
    
    def __init__(self, cheap_number, images, names, colors, ages, race, about, phone_number, owner_name, price):
        super().__init__(cheap_number = cheap_number, 
                         images = images,
                         names = names,
                         colors = colors,
                         ages = ages,
                         race = race,
                         about = about,
                         phone_number = phone_number,
                         owner_name = owner_name,
                         price = price)
