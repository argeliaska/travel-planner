from fastapi import APIRouter
from app.schemas.geo_schema import CityGeoOutSchema
from app.services.geo_services import GeoService
from typing import List

geo_router = APIRouter()

@geo_router.get('/info', summary="Gets the geographical info of a city", response_model=List[CityGeoOutSchema])
def get_geo_info(q: str):
    return GeoService.get(q)