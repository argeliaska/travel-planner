from fastapi import APIRouter
from app.api.api_v1.routers import geo
from app.api.api_v1.routers import weather
from app.api.api_v1.routers import travel

router = APIRouter()

router.include_router(geo.geo_router, prefix='/geo', tags=['GEO'])
router.include_router(weather.weather_router, prefix='/weather', tags=['WEATHER'])
router.include_router(travel.travel_router, prefix='/travel', tags=['TRAVEL'])