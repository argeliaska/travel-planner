from fastapi import APIRouter
from app.schemas.geo_schema import CityGeoOutSchema, CityGeoRevOutSchema
from app.services.geo_services import GeoService
from typing import List

geo_router = APIRouter()

@geo_router.get('/info', summary="Gets the geographical info of a city", response_model=List[CityGeoOutSchema])
def get_geo_info(q: str):
    return GeoService.get_info(q)

@geo_router.get('/info_rev', summary="Gets the info of a city by latitude and longitud", response_model=List[CityGeoOutSchema])
def get_geo_info_rev(lat: float, lon: float):
    return GeoService.get_info_rev(lat, lon)