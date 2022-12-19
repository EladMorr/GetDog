from backmain import Backend
from models import *

def test_backend_function():
    result = Backend.GetDogsList()
    assert result == "http request to get dogs list from DB by dog service"
    
    newDog = Dog(1, "Koko", 2, "yellow", "husky", "cute dog")
    
    result = Backend.AddDog(newDog)
    assert result == "http request to add new dog to DB by dog service"
    
    result = Backend.EditDog(newDog)
    assert result == "http request to update existing dog in DB by dog service"
    
    result = Backend.RemoveDog(newDog)
    assert result == "http request to remove existing dog in DB by dog service"
    