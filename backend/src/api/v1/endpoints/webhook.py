from fastapi import (
    APIRouter, Depends, status, Request, Response, HTTPException
)
from motor.motor_asyncio import AsyncIOMotorCollection as DBCollection
from aiogram.types import Update

from src import repo
from src.api import deps
from src.telegram.dispatcher import get_dispatcher


router = APIRouter()


@router.post(
    '/{bot_key}',
    response_class=Response,
    status_code=status.HTTP_200_OK
)
async def webhook(
        bot_key: str,
        req: Request,
        db_collection: DBCollection = Depends(deps.get_bots_collection)
):
    bot_data = await repo.bot.get_by_webhook_key(db_collection, key=bot_key)
    if not bot_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    dispatcher = get_dispatcher(bot_data.scenario)
    with dispatcher.bot.with_token(bot_data.token, validate_token=False),\
            dispatcher.storage.with_prefix(str(bot_data.id)):
        await dispatcher.process_update(Update(await req.json()))
