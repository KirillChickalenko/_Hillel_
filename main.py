from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

import config
import dao
from schemas import NewTrip

templates = Jinja2Templates(directory="templates")


def lifespan():
    yield


app = FastAPI(
    debug=config.DEBUG,
    lifespan=lifespan,
)


@app.post("/create", status_code=201)
def create(trip_data: NewTrip) -> NewTrip:
    trip = dao.create_trip(**trip_data.dict())
    return trip


@app.delete("/delete/{trip_id}", status_code=204)
def delete(trip_id: int) -> None:
    dao.delete_trip(trip_id)
