from typing import TypeVar, Generic

from bson import ObjectId
from pydantic import BaseModel

InDBType = TypeVar('InDBType', bound=BaseModel)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class BaseRepo(Generic[InDBType, CreateSchemaType, UpdateSchemaType]):
    def __call__(self): return self

    @staticmethod
    async def get(collection, id_: str | ObjectId) -> InDBType:
        return collection.find_one({'_id': ObjectId(id_)})

    @staticmethod
    async def create(collection, obj_in: CreateSchemaType) -> ObjectId:
        return collection.insert_one(obj_in.dict()).inserted_id

    @staticmethod
    async def update(collection, id_: str | ObjectId, obj_in: UpdateSchemaType) -> InDBType:
        return collection.update_one({'_id': id_}, {'$set': obj_in.dict()}).raw_result

    @staticmethod
    async def remove(collection, id_: str | ObjectId) -> InDBType:
        return collection.delete_one({'_id': id_}).raw_result
