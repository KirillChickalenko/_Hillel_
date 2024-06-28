from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Trip(Base):
    __tablename__ = 'trips'
    id = Column(Integer, primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)
    cost = Column(Float)
    country = Column(String)
    city = Column(String)
    hotel_class = Column(Integer)


engine = create_engine('sqlite:///trips.db', echo=True)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()
