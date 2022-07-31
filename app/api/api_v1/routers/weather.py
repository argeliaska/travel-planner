from fastapi import APIRouter
from app.schemas.weather_schema import ForecastOutSchema
from app.services.weather_service import WeatherService
from datetime import datetime, timedelta
from app.core.config import settings
from typing import List

weather_router = APIRouter()

tomorrow = datetime.now()
tomorrow += timedelta(days=1) 

@weather_router.get('/onecall', summary="Gets the current weather info and forecast", 
                    ) # response_model=ForecastOutSchema
def get(lat: float = settings.DEFAULT_ARRIVAL_LAT, 
        lon: float = settings.DEFAULT_ARRIVAL_LON, 
        date_da: datetime = tomorrow):
    return WeatherService.get_forecast(lat, lon, date_da)

@weather_router.get('/forecast', summary="Gets the forecast", 
                    response_model=List[ForecastOutSchema]) # response_model=ForecastOutSchema
def get(lat: float = settings.DEFAULT_ARRIVAL_LAT, 
        lon: float = settings.DEFAULT_ARRIVAL_LON):
    return WeatherService.get_forecasted_weather(lat, lon)

