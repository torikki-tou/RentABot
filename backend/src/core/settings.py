from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_CONNECTION_STRING: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


settings = Settings()
