from http import HTTPStatus
from fastapi.exceptions import HTTPException
from app.utils import get_response
from app.core.config import settings
from app.schemas.geo_schema import CityGeoOutSchema, CityGeoRevOutSchema

import logging

class GeoService():
    @staticmethod
    def get_info(q: str=None):
        
        results = []
        
        if q:
            url = f'{settings.GEO_API_URL}'
            params = {'q': q}
            params.update(settings.OPEN_WEATHER_APIKEY_PARAM)
            params.update(settings.CITIES_GEO_INFO_LIMIT)
            resp = get_response(url, params)
            
            if resp:
                results = [CityGeoOutSchema(**city) for city in resp]
            else:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND,
                    detail="City not found"
                )

        return results

    @staticmethod
    def get_info_rev(lat: float=None, lon: float=None):
        
        result = None

        url = f'{settings.GEO_REV_API_URL}'
        params = {'lat': lat, 'lon': lon}
        params.update(settings.OPEN_WEATHER_APIKEY_PARAM)
        resp = get_response(url, params)
        if resp:
            result = CityGeoRevOutSchema(**resp)
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail="City not found, incorrect latitud or longitud"
            )

        return result
    