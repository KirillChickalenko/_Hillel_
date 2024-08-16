from datetime import datetime

from fastapi import Path, HTTPException, APIRouter
from pydantic import BaseModel, Field, HttpUrl
from starlette import status

import dao


api_router = APIRouter(prefix='/api')


class NewTravel(BaseModel):
    date_start: datetime
    date_end: datetime
    title: str = Field(max_length=100, examples=["A travel to the UK."])
    description: str = Field(max_length=300, default="", examples=["Perfect travel to London."])
    price: float = Field(ge=0.01, examples=[100.78])
    image: HttpUrl
    hotel_class: int = Field(gt=0, le=5, default=4)
    country: str = Field(default="Great Britain")


class TravelData(NewTravel):
    id: int


@api_router.post("/create", status_code=status.HTTP_201_CREATED)
def create_travel(new_travel: NewTravel) -> TravelData:
    travel = dao.create_travel(**new_travel.dict())
    return travel


@api_router.get("/get_all_travel")
def get_all_travel() -> list[TravelData]:
    travels = dao.get_all_travel(50, 0)
    return travels


@api_router.get("/travel/{travel_id}")
def get_travel_by_name(travel_title: str) -> NewTravel:
    travel = dao.get_travel_by_name(travel_title)
    if not travel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Trip wasn`t found")
    return travel

@api_router.get("/travel/{travel_id}")
def get_travel_by_cost(travel_title: float) -> NewTravel:
    travel = dao.get_travel_by_cost(get_travel_by_cost)
    if not travel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Trip wasn`t found")
    return travel


@api_router.delete("/travel/{travel_id}")
def delete_travel(travel_id: int = Path(gt=0, description="ID of the travel")):
    dao.delete_travel(travel_id=travel_id)
    return None


@api_router.put('/travel/{travel_id}')
def update_travel(travel_id: int, updated_travel: NewTravel) -> TravelData:
    travel = dao.get_travel_by_id(travel_id=travel_id)
    if not travel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    updated_travel_data = updated_travel.dict()
    travel = dao.update_travel(travel_id, updated_travel_data)
    return travel
