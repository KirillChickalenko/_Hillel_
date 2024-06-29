from datetime import date

from pydantic import BaseModel


class NewTrip(BaseModel):
    start_date: date
    end_date: date
    cost: float
    country: str
    city: str
    hotel_class: int
    num_of_adults: str
    num_of_kids: str
    vehicle: str
