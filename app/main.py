from fastapi import FastAPI
from fastapi.params import Depends
from pydantic import BaseModel
from .schemes.schemes import *

app = FastAPI()


@app.get("/hotels")
def get_hotels(
        search_args: HotelSeerchArgs = Depends()
) -> list[BaseModel]:
    hotels = [
        {
            "address": "Ул. Колотушкина, дом 1",
            "name": "Hotel California",
            "stars": 5,
        }
    ]
    return hotels


@app.post("/booking")
def add_booking(booking: SBooking):
    pass
