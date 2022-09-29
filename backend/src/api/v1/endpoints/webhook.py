from fastapi import (APIRouter, Depends, status, Body, Response)
from aiogram.types import Update

from src import schemas
from src.api import deps
from src.telegram import dispatcher_context


router = APIRouter()


@router.post(
    '/',
    response_class=Response,
    status_code=status.HTTP_200_OK
)
async def webhook(
        req: dict = Body(),
        bot: schemas.BotInDB = Depends(deps.get_current_bot),
):
    with dispatcher_context(bot.scenario, bot.id, bot.token) as dispatcher:
        await dispatcher.process_update(Update.to_object(req))
