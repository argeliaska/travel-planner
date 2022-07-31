from beanie import Document, Indexed
from pydantic import Field, EmailStr
from datetime import datetime
from app.schemas.weather_schema import ForecastOutSchema
from typing import Any


class Travel(Document):
    user_email: Indexed(EmailStr)
    departure_date: datetime = None # 
    arrival_date: datetime = None
    origin: str = None
    origin_name: str = None
    destination: str = None
    destination_name: str = None
    forecasted_weather: Any = None
     
    class Collection:
        name = 'travel'