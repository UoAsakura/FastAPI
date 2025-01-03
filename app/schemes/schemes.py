from typing import Optional
from datetime import date
from fastapi import Query
from pydantic import BaseModel


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


class HotelSeerchArgs:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            has_spa: Optional[bool] = None,
            stars: Optional[int] = Query(None, ge=1, le=5)
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars



# class SBooking(BaseModel):
#     room_id: int
#     date_from: date
#     date_to: date
