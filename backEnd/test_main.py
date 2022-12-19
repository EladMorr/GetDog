from backmain import Backend
from models import *

def test_backend_function():
    result = Backend.GetDogsList()
    assert result == "http request to get dogs list from DB by dog service"
    
    newDog = Dog(id=1, name="Koko", age=2, color="yellow", race="husky", desc="cute dog")
    
    result = Backend.AddDog(newDog)
    assert result == "http request to add new dog to DB by dog service"
    
    result = Backend.EditDog(newDog)
    assert result == "http request to update existing dog in DB by dog service"
    
    result = Backend.RemoveDog(newDog)
    assert result == "http request to remove existing dog in DB by dog service"
    