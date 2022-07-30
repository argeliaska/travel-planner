from pydantic import BaseModel

class CityGeoOutSchema(BaseModel):
    name: str
    lat: float
    lon: float
    country: str
    state: str

class CityGeoRevOutSchema(BaseModel):
    name: str
    country: str
    state: str
