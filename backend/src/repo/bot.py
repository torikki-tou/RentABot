from typing import List

from bson import ObjectId

from src.repo.base import BaseRepo
from src.schemas.bot import BotInDBBase, BotUpdate, BotCreate


class BotRepo(BaseRepo[BotUpdate, BotCreate, BotInDBBase]):
    @staticmethod
    def get_multy_by_owner(
            collection,
            owner_id: str | ObjectId,
            skip: int = 0,
            limit: int = 10
    ) -> List[BotInDBBase]:
        return collection.find({'owner_id': ObjectId(owner_id)}, skip=skip).to_list(length=limit)
