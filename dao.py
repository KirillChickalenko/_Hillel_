from fastapi import FastAPI
from datetime import date
from database import Trip, session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette import status



def create_trip(num_of_adults:int, num_of_kids:int, start_date: date, end_date: date, cost: float, country: str, city: str, hotel_class: int, vehicle: str) -> Trip:
    trip = Trip(
        num_of_adults=num_of_adults,
        num_of_kids=num_of_kids,
        start_date=start_date,
        end_date=end_date,
        cost=cost,
        country=country,
        city=city,
        hotel_class=hotel_class,
        vehicle=vehicle,
    )
    session.add(trip)
    session.commit()
    return trip

def get_all_trips(limit: int, skip: int) -> list[Trip]:
    trips = session.query(Trip).limit(limit).offset(skip).all()
    return trips


def delete_trip(trip_id: int) -> None:
    session.query(Trip).filter(Trip.id == trip_id).delete()
    session.commit()

def update_start_date(trip_id: int, new_start_date: date) -> Trip:
    update_data = {"start_date": new_start_date}
    updated_trip = update_start_date(trip_id, new_start_date)
    return updated_trip

def update_end_date(trip_id: int, new_end_date: date) -> Trip:
    update_data = {"end_date": new_end_date}
    updated_trip = update_start_date(trip_id, new_end_date)
    return updated_trip
