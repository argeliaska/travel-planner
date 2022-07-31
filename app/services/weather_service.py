from http import HTTPStatus
from fastapi.exceptions import HTTPException
from app.utils import get_response
from app.core.config import settings
from app.schemas.weather_schema import ForecastOutSchema, WeatherOutSchema
from datetime import datetime, date
import logging

class WeatherService():
    @staticmethod
    def get_forecast(lat: float, lon: float, date_da: datetime):
        
        results = []

        url = f'{settings.WEATHER_API_URL}'
        params = {'lat': lat, 'lon': lon}
        params.update(settings.OPEN_WEATHER_APIKEY_PARAM)
        resp = get_response(url, params)
        if resp:
            if 'daily' in resp:
                for day_forecast in resp.get('daily'):
                    date_forecast = datetime.fromtimestamp(day_forecast.get('dt'))

                    if date_forecast.date() == date_da.date():
                        f_date = date_forecast.date()                
                        f_weather = day_forecast.get('weather')
                        f_temp = day_forecast.get('temp')

                        forecast = ForecastOutSchema()
                        forecast.date = f_date
                        forecast.weather = f_weather
                        forecast.temp.min = f_temp.get('min')
                        forecast.temp.max = f_temp.get('max')
                        results.append(forecast)
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail="City not found, incorrect latitud or longitud"
            )

        return results