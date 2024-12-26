from sqlalchemy import Column, Date, ForeignKey, Integer, String, JSON, Computed
from app.database import Base


# Создаём модель нашей таблицы hotels
class Bookings(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, nullable=False)
    room_id = Column(ForeignKey("rooms.id"), nullable=True)
    user_id = Column(ForeignKey("users.id"), nullable=True)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed("(date_from - date_to) * price"), nullable=True)
    total_days = Column(Integer, Computed("date_from - date_to"), nullable=True)
