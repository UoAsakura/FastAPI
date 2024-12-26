from sqlalchemy import Column, Integer, String, JSON

from app.database import Base


# Создаём модель нашей таблицы hotels
class Hotels(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # nullable=False столбцы не могут быть пустыми
    location = Column(String, nullable=False)
    services = Column(JSON)
    rooms_quntity = Column(Integer, nullable=False)
    image_id = Column(Integer)
