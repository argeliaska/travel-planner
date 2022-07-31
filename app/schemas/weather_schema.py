from pydantic import BaseModel
from datetime import datetime
from typing import List, Any

class TempSchema(BaseModel):
    min: float = 0.0
    max: float = 0.0


class WeatherSchema(BaseModel):
    id: int = 0
    main: str = None
    description: str = None
    icon: str = None


class ForecastOutSchema(BaseModel):
    date: datetime = None
    temp: Any = None
    weather: List = []

class ForecastOutSchema1(BaseModel):
    date: datetime = None
    temp: TempSchema = TempSchema()
    weather: List[WeatherSchema] = [WeatherSchema()]


class WeatherOutSchema(BaseModel):
    temp: float
    weather_name: str
    weather_description: str
    icon: str