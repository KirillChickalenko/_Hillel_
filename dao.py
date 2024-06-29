from datetime import date

from database import Trip, session


def create_trip(
    num_of_adults: int,
    num_of_kids: int,
    start_date: date,
    end_date: date,
    cost: float,
    country: str,
    city: str,
    hotel_class: int,
    vehicle: str,
) -> Trip:
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
