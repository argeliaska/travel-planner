from pydantic import BaseSettings
from decouple import config

APP_DESC = 'This personal travel planner will help you scheduler '\
           'your travel by showing the weather for departure and return date. <br/>'\
           '<br/>API USAGE TIPS:'\
                '<ul><li>To get latitud and longitud of a city, use the endpoint info under GEO</li>'\
                '</ul>'

class Settings(BaseSettings):
    API_V1: str = '/api/v1'
    APP_DESCRIPTION: str = APP_DESC
    OPEN_WEATHER_APIKEY: str =  config('OPEN_WEATHER_APIKEY')
    WEATHER_API_URL: str = config('WEATHER_API_URL')
    GEO_API_URL: str = config('GEO_API_URL')
    GEO_REV_API_URL: str = config('GEO_REV_API_URL')
    OPEN_WEATHER_APIKEY_PARAM: dict = {'appid' : OPEN_WEATHER_APIKEY}
    CITIES_GEO_INFO_LIMIT: dict = {'limit' : 5}
    DEFAULT_DEPARTURE_LAT: float = config('DEFAULT_DEPARTURE_LAT')
    DEFAULT_DEPARTURE_LON: float = config('DEFAULT_DEPARTURE_LON')
    DEFAULT_ARRIVAL_LAT: float = config('DEFAULT_ARRIVAL_LAT')
    DEFAULT_ARRIVAL_LON: float = config('DEFAULT_ARRIVAL_LON')

settings = Settings()