from app.utils import get_response
from app.core.config import settings
from app.schemas.geo_schema import CityGeoOutSchema

import logging

class GeoService():
    @staticmethod
    def get(q: str=None):
        
        results = []
        
        if q:
            url = f'{settings.GEO_API_URL}'
            params = {'q': q}
            params.update(settings.OPEN_WEATHER_APIKEY_PARAM)
            params.update(settings.CITIES_GEO_INFO_LIMIT)
            resp = get_response(url, params)

            results = [CityGeoOutSchema(**city) for city in resp]

        return results