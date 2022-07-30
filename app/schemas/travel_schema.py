from pydantic import BaseModel
from pydantic import Field
from datetime import date, time, datetime

class TravelCreate(BaseModel):
    departure_date: date = Field(Required=True) # 
    departure_time: time = Field(Required=True) # 
    arrival_date: date = Field(Required=True)
    arrival_time: time = Field(Required=True)
    origin: str = Field(min_length=3, max_length=3)
    origin_name: str = Field(min_length=20, max_length=70)
    destination: str = Field(min_length=3, max_length=3)
    destination_name: str = Field(min_length=20, max_length=70)