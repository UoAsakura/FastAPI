from fastapi import APIRouter

from app.booking.dao import BookingDAO
from app.booking.schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Брониование"],
)


@router.get("")
async def get_bookings():
    response = BookingDAO.find_all()
    print(type(response))
    return await response
