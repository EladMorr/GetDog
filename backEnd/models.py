from pydantic import BaseModel

class Dog(BaseModel):
    m_id: int
    m_name: str
    m_age: float
    m_color: str
    m_race: str
    m_desc: str
    
    def __init__(self, id, name, age, color, race, desc):
        super().__init__(m_id = id, 
                         m_name = name,
                         m_age = age,
                         m_color = color,
                         m_race = race,
                         m_desc = desc)