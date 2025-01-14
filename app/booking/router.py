
from fastapi import APIRouter
from fastapi.params import Depends

from app.booking.dao import BookingDAO
from app.booking.schemas import SBooking
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Брониование"],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingDAO.find_all(user_id=1)



