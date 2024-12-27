from fastapi import FastAPI
from fastapi.params import Depends
from .schemes.schemes import *
from app.booking.router import router as router_booings

# Зпуск приложения
app = FastAPI()

# Подключение роутера bookings
app.include_router(router_booings)

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


# @app.post("/booking")
# def add_booking(booking: SBooking):
#     pass
