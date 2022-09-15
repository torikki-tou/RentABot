from typing import List

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection as DBCollection

from src.repo.base import BaseRepo
from src.schemas.bot import BotInDB, BotCreate, BotUpdate


class BotRepo(BaseRepo[BotInDB, BotCreate, BotUpdate]):
    async def create_with_owner(
            self,
            collection: DBCollection,
            obj_in: BotCreate,
            owner_id: str | ObjectId
    ) -> BotInDB:
        obj_in = obj_in.dict()
        obj_in['owner_id'] = owner_id
        return await self.create(collection, obj_in=obj_in)

    async def get_multy_by_owner(
            self,
            collection: DBCollection,
            owner_id: str | ObjectId,
            skip: int = 0,
            limit: int = 10
    ) -> List[BotInDB]:
        objs = await collection.find(
            {'owner_id': ObjectId(owner_id)},
            skip=skip
        ).to_list(length=limit)
        return [self.model(**obj) for obj in objs]


bot = BotRepo(BotInDB)
