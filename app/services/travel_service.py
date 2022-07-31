from app.models.travel_model import Travel
from datetime import datetime
from pydantic import EmailStr
from typing import List, Union
from app.schemas.travel_schema import TravelCreate, TravelIn
from .geo_services import GeoService
from .weather_service import WeatherService

class TravelService:
    @staticmethod
    def cast_travel_db_format(payload: TravelIn):

        forecasted_results = []
        origin_lat = payload.origin_lat
        origin_lon = payload.origin_lon
        destination_lat = payload.destination_lat
        destination_lon = payload.destination_lon

        origin = GeoService.get_info_rev(origin_lat, origin_lon)
        destination = GeoService.get_info_rev(destination_lat, destination_lon)

        travel = TravelCreate()
        travel.user_email = payload.user_email
        travel.departure_date = payload.departure_date
        travel.arrival_date = payload.arrival_date
        if origin:
            travel.origin = origin.country
            travel.origin_name = f'{origin.name}, {origin.state}, {origin.country}'
        if destination:
            travel.destination = destination.country
            travel.destination_name = f'{destination.name}, {destination.state}, {destination.country}'

        forecasted_weather = WeatherService.get_forecasted_weather(destination_lat, destination_lon)
        for item in forecasted_weather:
            forecasted_results.append(item)

        travel.forecasted_weather = {"results":forecasted_results}

        return travel

    @staticmethod
    async def list_travels(user_email: str) -> List[Travel]:
        travels = await Travel.find(Travel.user_email == user_email).to_list()
        return travels

    @staticmethod
    async def create(travel: TravelCreate):
        
        new_travel = Travel(
            user_email = travel.user_email,
            departure_date = travel.departure_date,
            arrival_date = travel.arrival_date,
            origin = travel.origin,
            origin_name = travel.origin_name,
            destination = travel.destination,
            destination_name = travel.destination_name,
            forecasted_weather = travel.forecasted_weather
        )

        await new_travel.save()
        return new_travel

    
    @staticmethod
    async def get_travels(departure_date: datetime, arrival_date: datetime, user_email: str=None) -> List[Travel]:
        travels = None
        results = []
        print(departure_date)
        # iso_departure_date = departure_date.strftime('%Y-%m-%dT%H:%M:%S')
        # iso_arrival_date = arrival_date.strftime('%Y-%m-%dT%H:%M:%S')
        
        if user_email:
            travels = Travel.find({'user_email': user_email},
                                {'departure_date':{'$gte':departure_date,'$lt':arrival_date}},
                                {'arrival_date':{'$gte':departure_date,'$lt':arrival_date}}
                    )
        else:
            travels = Travel.find(
                                {'departure_date':{'$gte':departure_date,'$lt':arrival_date}},
                                {'arrival_date':{'$gte':departure_date,'$lt':arrival_date}}
                )

        for document in await travels.to_list():
            results.append(document)

        return results

    @staticmethod
    async def get_by_user_email(user_email: EmailStr):
        results = []

        travels_by_user = Travel.find_many(Travel.user_email == user_email)
        for document in await travels_by_user.to_list():
            results.append(document)

        return results

    @staticmethod
    async def find_by_id(id: str):
        travel = await Travel.find_one(Travel.id == ObjectId(id))
        return travel