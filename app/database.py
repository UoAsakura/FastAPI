from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Указываем данные нашей БД
DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"
DB_PASS = "postgres"
DB_NAME = "postgres"

# Путь к нашей БД
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# Движок на котором мы будем взаимодействовать с БД при помощи ассинхронных сообщений
engine = create_async_engine(DATABASE_URL)
# Создание ассинхронных сессий, которые не будут истекать при коммите
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Для аккумуляции метаданных о всех таблицах, для работы с миграциями
class Base(DeclarativeBase):
    pass
