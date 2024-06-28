from fastapi import FastAPI
from datetime import date
from database import Trip, session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette import status



def create_trip(start_date: date, end_date: date, cost: float, country: str, city: str, hotel_class: int) -> Trip:
    trip = Trip(
        start_date=start_date,
        end_date=end_date,
        cost=cost,
        country=country,
        city=city,
        hotel_class=hotel_class,
    )
    session.add(trip)
    session.commit()
    return trip

def get_all_trips(limit: int, skip: int) -> list[Trip]:
    trips = session.query(Trip).limit(limit).offset(skip).all()
    return trips

def get_trip_by_id(trip_id: int) -> Trip | None:
    trip = session.query(Trip).filter(Trip.id == trip_id).first()
    return trip

def update_trip(trip_id: int, trip_data: dict) -> Trip:
    session.query(Trip).filter(Trip.id == trip_id).update(trip_data)
    session.commit()
    trip = session.query(Trip).filter(Trip.id == trip_id).first()
    return trip

def delete_trip(trip_id: int) -> None:
    session.query(Trip).filter(Trip.id == trip_id).delete()
    session.commit()
