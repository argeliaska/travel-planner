from pydantic import BaseModel
from datetime import datetime
from typing import List

class TempSchema(BaseModel):
    min: float = 0.0
    max: float = 0.0


class WeatherSchema(BaseModel):
    id: int = 0
    name: str = None
    description: str = None
    icon: str = None


class ForecastOutSchema(BaseModel):
    date: datetime = None
    weather: List[WeatherSchema] = [WeatherSchema()]
    temp: TempSchema = TempSchema()


class WeatherOutSchema(BaseModel):
    temp: float
    weather_name: str
    weather_description: str
    icon: str

