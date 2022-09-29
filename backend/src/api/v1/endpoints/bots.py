from fastapi import APIRouter, Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorCollection as DBCollection

from src import schemas, repo
from src.api import deps
from src.core.settings import settings
from src.telegram import dispatcher_context


router = APIRouter()


@router.get(
    '/{bot_id}',
    response_model=schemas.Bot,
    status_code=status.HTTP_200_OK
)
async def read_bot(
        bot_id: str,
        db_collection: DBCollection = Depends(deps.get_bots_collection)
):
    bot = await repo.bot.get(db_collection, id_=bot_id)
    if not bot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return schemas.Bot(**bot.dict())


@router.post(
    '/',
    response_model=schemas.Bot,
    status_code=status.HTTP_201_CREATED
)
async def create_bot(
        obj_in: schemas.BotCreate,
        db_collection: DBCollection = Depends(deps.get_bots_collection),
        user: schemas.UserInDB = Depends(deps.get_current_user)
):
    bot = await repo.bot.create_with_owner(
        db_collection,
        obj_in=obj_in,
        owner_id=user.id
    )
    with dispatcher_context(bot.scenario, bot.id, bot.token) as dispatcher:
        await dispatcher.bot.set_webhook(
            url=settings.WEBHOOK_URL,
            secret_token=bot.webhook_key,
            drop_pending_updates=True
        )
    return schemas.Bot(**bot.dict())


@router.put(
    '/{bot_id}',
    response_model=schemas.Bot,
    status_code=status.HTTP_200_OK
)
async def update_bot(
        bot_id: str,
        obj_in: schemas.BotUpdate,
        db_collection: DBCollection = Depends(deps.get_bots_collection)
):
    bot = await repo.bot.update(db_collection, id_=bot_id, obj_in=obj_in)
    if not bot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return schemas.Bot(**bot.dict())


@router.delete(
    '/{bot_id}',
    response_model=schemas.Bot,
    status_code=status.HTTP_200_OK
)
async def remove_bot(
        bot_id: str,
        db_collection: DBCollection = Depends(deps.get_bots_collection)
):
    bot = await repo.bot.remove(db_collection, id_=bot_id)
    if not bot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return schemas.Bot(**bot.dict())
