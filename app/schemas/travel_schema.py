from pydantic import BaseModel, validator, root_validator
from pydantic import Field, EmailStr
from typing import List, Any
from datetime import date, time, datetime
from app.schemas.weather_schema import ForecastOutSchema
from app.models.travel_model import Travel
from app.core.config import settings

def travel_out(travel: Travel) -> dict:
    return {
        'id': str(travel.id),
        'user_email': travel.user_email,
        'departure_date': travel.departure_date,
        'arrival_date': travel.arrival_date,
        'origin': travel.origin,
        'origin_name': travel.origin_name,
        'destination': travel.destination,
        'destination_name': travel.destination_name,
        'forecasted_weather': travel.forecasted_weather
    }

def travel_in_example() -> dict:
    return {
        'user_email': 'user@heru.com',
        'departure_date': '2022-08-02T13:00:00',
        'arrival_date': '2022-08-07T21:00:00',
        'origin_lat': settings.DEFAULT_DEPARTURE_LAT,
        'origin_lon': settings.DEFAULT_DEPARTURE_LON,
        'destination_lat': settings.DEFAULT_ARRIVAL_LAT,
        'destination_lon': settings.DEFAULT_ARRIVAL_LON
    }


class TravelIn(BaseModel):
    user_email: EmailStr = Field(..., )
    departure_date: datetime = Field(default_factory=datetime.now(), Required=True) # 
    arrival_date: datetime = Field(default_factory=datetime.now(), Required=True) # 
    origin_lat: float = Field(default=settings.DEFAULT_DEPARTURE_LAT)
    origin_lon: float = Field(default=settings.DEFAULT_DEPARTURE_LON)
    destination_lat: float = Field(default=settings.DEFAULT_ARRIVAL_LAT)
    destination_lon: float = Field(default=settings.DEFAULT_ARRIVAL_LON)

    @root_validator(pre=True)
    def check_user_email_omitted(cls, values):
        assert 'user_email' in values, 'user_email should be included'
        return values

    @root_validator(pre=True)
    def check_departure_date_omitted(cls, values):
        assert 'departure_date' in values, 'departure_date should be included'
        return values

    @root_validator(pre=True)
    def check_arrival_date_omitted(cls, values):
        assert 'arrival_date' in values, 'arrival_date should be included'
        return values

    @root_validator(pre=True)
    def check_origin_lat_omitted(cls, values):
        assert 'origin_lat' in values, 'origin_lat should be included'
        return values

    @root_validator(pre=True)
    def check_origin_lon_omitted(cls, values):
        assert 'origin_lon' in values, 'origin_lon should be included'
        return values

    @root_validator(pre=True)
    def check_destination_lat_omitted(cls, values):
        assert 'destination_lat' in values, 'destination_lat should be included'
        return values

    @root_validator(pre=True)
    def check_destination_lon_omitted(cls, values):
        assert 'destination_lon' in values, 'destination_lon should be included'
        return values

    @validator('departure_date', 'arrival_date')
    def date_must_be_gt_today(cls, v):
        if v:
            dte = datetime.fromisoformat(str(v))
            if dte <= datetime.utcnow(): 
                raise ValueError('must be greater than today')
        return v

    @validator('arrival_date')
    def arrival_date_be_gt_departure_date(cls, v, values, **kwargs):
        if v:
            arrival_dte = datetime.fromisoformat(str(v))
            departure_dte = str(values['departure_date'])

            ad = datetime.strptime(str(v), '%Y-%m-%d %H:%M:%S')
            dd = datetime.strptime(departure_dte, '%Y-%m-%d %H:%M:%S')
            days_trip_td = ad - dd

            if arrival_dte <= datetime.fromisoformat(departure_dte): 
                raise ValueError('must be greater than departure_date')
            if days_trip_td.days > settings.MAX_DAYS_TRIP:
                raise ValueError(f'trip cannot be longer than {settings.MAX_DAYS_TRIP} days')
        return v
    
    @validator('destination_lon')
    def destination_lat_lon_diff_origin_lat_lon(cls, v, values, **kwargs):
        if v:
            origin_lat = values['origin_lat']
            origin_lon = values['origin_lon']

            destination_lat = values['destination_lat']
            destination_lon = v

            if destination_lat == origin_lat and destination_lon == origin_lon: 
                raise ValueError('destination must be different than origin')
        return v

class TravelCreate(BaseModel):
    user_email: EmailStr = None
    departure_date: datetime = None
    arrival_date: datetime = None
    origin: str = None
    origin_name: str = None
    destination: str = None
    destination_name: str = None
    forecasted_weather: Any = None

class TravelOut(BaseModel):
    id: str = None
    user_email: EmailStr = None
    departure_date: datetime = None
    arrival_date: datetime = None
    origin: str = None
    origin_name: str = None
    destination: str = None
    destination_name: str = None
    forecasted_weather: Any = None