import uuid
from datetime import date

from database import Trip, User, session
from utils.utils_hashlib import get_password_hash


def create_trip(
    country: str,
    city: str,
    start_date: date,
    end_date: date,
    cost: float,
    hotel_class: int,
    amount_of_adults: int,
    amount_of_kids: int,
    vehicle: str,
) -> Trip:
    trip = Trip(
        country=country,
        city=city,
        start_date=start_date,
        end_date=end_date,
        cost=cost,
        hotel_class=hotel_class,
        amount_of_adults=amount_of_adults,
        amount_of_kids=amount_of_kids,
        vehicle=vehicle,
    )
    session.add(trip)
    session.commit()
    return trip


def delete_trip(trip_id: int) -> None:
    session.query(Trip).filter(Trip.id == trip_id).delete()
    session.commit()


def update_trip(trip_id: int, trip: dict) -> Trip:
    session.query(Trip).filter(Trip.id == trip_id).update(trip)
    session.commit()
    product = session.query(Trip).filter(Trip.id == trip_id).first()
    return product


def get_trip_by_id(product_id) -> Trip | None:
    trip = session.query(Trip).filter(Trip.id == product_id).first()
    return trip



def create_user(name: str, email: str, password: str) -> User:
    user = User(
        name=name,
        email=email,
        hashed_password=get_password_hash(password),
    )
    session.add(user)
    session.commit()
    return user


def get_user_by_email(email: str) -> User | None:
    user = session.query(User).filter(User.email == email).first()
    return user


def get_user_by_uuid(user_uuid: uuid.UUID) -> User | None:
    user = session.query(User).filter(User.user_uuid == user_uuid).first()
    return user


def activate_user_account(user: User) -> User:
    if user.is_verified:

        return user

    user.is_verified = True
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
