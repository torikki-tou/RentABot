from fastapi import Depends

from src.db import get_mongo_client, config


def get_api_database():
    return get_mongo_client()[config.Database.API.value]


def get_users_collection(database=Depends(get_api_database)):
    return database[config.Collection.USERS.value]


def get_bots_collection(database=Depends(get_api_database)):
    return database[config.Collection.BOTS.value]
