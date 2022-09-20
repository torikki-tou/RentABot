from typing import List, Union, Dict, Any, Optional

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection as DBCollection

from src.repo.base import BaseRepo
from src.schemas.bot import BotInDB, BotCreate, BotUpdate
from src.core import security


class BotRepo(BaseRepo[BotInDB, BotCreate, BotUpdate]):
    async def get_by_webhook_key(
            self,
            collection: DBCollection,
            key: str
    ) -> Optional[BotInDB]:
        obj = await collection.find_one({'webhook_key': key})
        if not obj:
            return None
        obj['id'] = str(obj.pop('_id'))
        return self.model(**obj)

    async def create(
            self,
            collection: DBCollection,
            obj_in: Union[BotCreate, Dict[str, Any]]
    ) -> BotInDB:
        if not isinstance(obj_in, dict):
            obj_in = obj_in.dict(exclude_unset=True)
        obj_in['webhook_key'] = security.get_webhook_key()
        return await super(BotRepo, self).create(collection, obj_in=obj_in)

    async def create_with_owner(
            self,
            collection: DBCollection,
            obj_in: BotCreate,
            owner_id: str | ObjectId
    ) -> BotInDB:
        obj_in = obj_in.dict()
        obj_in['owner_id'] = str(owner_id)
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
