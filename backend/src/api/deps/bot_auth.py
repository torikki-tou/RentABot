from fastapi import Depends, Header, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorCollection as DBCollection

from src import schemas, repo
from src.api import deps


async def get_current_bot(
        webhook_key: str = Header(alias='X-Telegram-Bot-Api-Secret-Token'),
        db_collection: DBCollection = Depends(deps.get_bots_collection)
) -> schemas.BotInDB:
    bot = await repo.bot.get_by_webhook_key(db_collection, key=webhook_key)
    if not bot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return bot
