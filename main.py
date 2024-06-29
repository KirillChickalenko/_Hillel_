from datetime import datetime

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette import status
from fastapi import FastAPI
import config
from database import Trip

import dao
from schemas import NewTrip
from schemas import UpdateTrip

templates = Jinja2Templates(directory='templates')

def lifespan(app: FastAPI):
    yield

app = FastAPI(
    debug=config.DEBUG,
    lifespan=lifespan,
)

@app.post('/create', status_code=201)
def create(trip_data: NewTrip) -> NewTrip:
    trip = dao.create_trip(**trip_data.dict())
    return trip

@app.delete('/delete/{trip_id}', status_code=204)
def delete(trip_id: int) -> None:
    dao.delete_trip(trip_id)

@app.put('/update/start_date', status_code=200)
def update_start_date(trip_data: UpdateTrip) -> UpdateTrip:
    trip_id = trip_data.trip_id
    new_start_date = trip_data.new_start_date

@app.put('/update/end_date', status_code=200)
def update_end_date(trip_data: UpdateTrip) -> UpdateTrip:
    trip_id = trip_data.trip_id
    new_end_date = trip_data.new_end_date
