import uuid
from datetime import datetime

from sqlalchemy import (UUID, Boolean, Column, DateTime, Float, Integer,
                        Sequence, String, create_engine)
from sqlalchemy.orm import declarative_base, sessionmaker

import config

Base = declarative_base()


class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, Sequence("trip_id_seq"), primary_key=True)
    country = Column(String(100), nullable=False, default="The United Kingdom")
    city = Column(String(100), nullable=False, default="London")
    start_date = Column(DateTime, default=datetime)
    end_date = Column(DateTime, default=datetime)
    cost = Column(Float, nullable=False, default=100.0)
    hotel_class = Column(Integer, nullable=False, default=0)
    amount_of_adults = Column(Integer, nullable=False, default=0)
    amount_of_kids = Column(Integer, nullable=False, default=0)
    vehicle = Column(String(100), nullable=False, default="Plane")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    user_uuid = Column(UUID, default=uuid.uuid4)
    is_verified = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

    def __str__(self):
        return f"<User: {self.name=}; {self.surname=}>"

    __repr__ = __str__

engine = create_engine("sqlite:///trips.db", echo=True)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()
