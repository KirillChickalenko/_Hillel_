from datetime import date
from pydantic import BaseModel

class NewTrip(BaseModel):
    start_date: date
    end_date: date
    cost: float
    country: str
    city: str
    hotel_class: int

class UpdateTrip(BaseModel):
    trip_id: int
    new_start_date: date
