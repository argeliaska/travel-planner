from fastapi import APIRouter, Body
from fastapi import status, HTTPException
from app.core.config import settings
from app.services.travel_service import TravelService
from app.schemas.travel_schema import travel_out, TravelIn, TravelOut, travel_in_example
from datetime import datetime
from typing import List, Union

travel_router = APIRouter()
travel_in_example = travel_in_example()

@travel_router.post('/create', summary="Creates a new plan trip", response_model=TravelOut)
async def create(data: TravelIn = Body(example=travel_in_example)):
    travels_conflict = await TravelService.get_travels(data.user_email, data.departure_date, data.arrival_date)
    
    if len(travels_conflict) > 0:
        travel_conflict = travels_conflict[0]
        travel_dates = datetime.strftime(travel_conflict.departure_date, "%d/%m/%Y %H:%M:%S") + \
                        ' to ' + \
                        datetime.strftime(travel_conflict.arrival_date, "%d/%m/%Y %H:%M:%S")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'The travel plan cannot be created. There is a travel scheduled on {travel_dates}'
        )

    travel = TravelService.cast_travel_db_format(data)
    print('create travel cast_travel_db_format', travel.forecasted_weather)

    travel_created = await TravelService.create(travel)

    return travel_out(travel_created)

@travel_router.get('/user', summary='Gets the travels by user_email', response_model=List[TravelOut])
async def get_by_user(user_email: str = settings.DEFAULT_USER_EMAIL):
    travels_by_user = await TravelService.get_by_user_email(user_email)

    return [travel_out(travel) for travel in travels_by_user]

@travel_router.get('/id/{id}')
def get_by_id(id:str):
    return TravelService.get_by_id(id)

@travel_router.get('/list', summary='Gets all travels', response_model=List[TravelOut])
async def travel_list(departure_date:datetime=datetime.now(), arrival_date:datetime=datetime.now(), user_email: Union[str, None] = None):
    travels_by_user = await TravelService.get_travels(departure_date, arrival_date, user_email)

    return [travel_out(travel) for travel in travels_by_user]
