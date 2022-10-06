from functools import cached_property
from typing import Callable

from motor.motor_asyncio import AsyncIOMotorDatabase
from motor.motor_asyncio import AsyncIOMotorCollection as DBCollection

from src.db import get_mongo_client


class APICollections:
    def __init__(self, database: AsyncIOMotorDatabase):
        self.__database = database

    @cached_property
    def users(self) -> Callable[[], DBCollection]:
        return lambda: self.__database.users

    @cached_property
    def bots(self) -> Callable[[], DBCollection]:
        return lambda: self.__database.bots


class Databases:

    def __init__(self):
        self.__client = get_mongo_client()

    @cached_property
    def api(self) -> APICollections:
        return APICollections(self.__client.api)


get_db_collection = Databases()
