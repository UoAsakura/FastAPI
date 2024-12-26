from sqlalchemy import Column, Date, ForeignKey, Integer, String, JSON, Computed
from app.database import Base


# Создаём модель нашей таблицы hotels
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
