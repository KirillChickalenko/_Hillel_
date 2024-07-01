from pathlib import Path

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

import config
import dao
from schemas import NewTrip

templates = Jinja2Templates(directory="templates")


def lifespan(app: FastAPI):
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


@app.put("/api/trips/{trip_id}", tags=["API", "Trips"])
def update_trip(
    updated_trip: NewTrip,
    trip_id: int = Path(gt=0, description="ID of the product"),
) -> NewTrip:

    dao.update_trip(trip_id, updated_trip.dict())
    return updated_trip


@app.get("/api/trips/{trip_id}", tags=["API", "Trips"])
def get_trip(trip_id: int = Path(gt=0, description="ID of the trip")) -> NewTrip:
    trip = dao.get_trip_by_id(trip_id=trip_id)
    return trip
