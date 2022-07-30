from fastapi import APIRouter
from app.api.api_v1.routers import geo

router = APIRouter()

router.include_router(geo.geo_router, prefix='/geo', tags=['GEO'])