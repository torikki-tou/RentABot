from motor.motor_asyncio import AsyncIOMotorClient

from src.core import settings


class MongoClient:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)

    def __call__(self) -> AsyncIOMotorClient:
        return self.client

    def __del__(self) -> None:
        self.client.close()


get_mongo_client = MongoClient()
