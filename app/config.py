from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    def get_database_url(cls):
        DB_URL = f"postgresql+asyncpg://{cls.DB_USER}:{cls.DB_PASS}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"
        return DB_URL

    DATABASE_URL = get_database_url

    def get_settings(self):
        return Settings()

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

DATABASE_URL = settings.get_database_url()
