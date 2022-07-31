from fastapi import APIRouter
from app.schemas.weather_schema import ForecastOutSchema
from app.services.weather_service import WeatherService
from datetime import datetime, timedelta
from app.core.config import settings

weather_router = APIRouter()

tomorrow = datetime.now()
tomorrow += timedelta(days=1) 

@weather_router.get('/onecall', summary="Gets the current weather info and forecast", 
                    ) # response_model=ForecastOutSchema
def get(lat: float = settings.DEFAULT_DEPARTURE_LAT, 
        lon: float = settings.DEFAULT_DEPARTURE_LON, 
        date_da: datetime = tomorrow):
    return WeatherService.get_forecast(lat, lon, date_da)


