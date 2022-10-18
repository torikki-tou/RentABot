from fastapi import APIRouter, Depends, HTTPException, status, Response
from motor.motor_asyncio import AsyncIOMotorCollection as DBCollection

from src import schemas, repo
from src.api import deps
from src.telegram import webhook, validate_token


router = APIRouter()


@router.get(
    '/{bot_id}',
    response_model=schemas.Bot,
    status_code=status.HTTP_200_OK
)
async def read_bot(
        bot_id: str,
        db_collection: DBCollection = Depends(deps.get_db_collection.api.bots),
        user: schemas.UserInDB = Depends(deps.get_current_user)
):
    bot = await repo.bot.get(db_collection, id_=bot_id)
    if not bot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if not(bot.owner_id == user.id or user.is_superuser):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return schemas.Bot(**bot.dict())


@router.post(
    '/',
    response_model=schemas.Bot,
    status_code=status.HTTP_201_CREATED
)
async def create_bot(
        obj_in: schemas.BotCreate,
        db_collection: DBCollection = Depends(deps.get_db_collection.api.bots),
        user: schemas.UserInDB = Depends(deps.get_current_user)
):
    can_be, reason = await repo.bot.can_be_created(
        db_collection, obj_in=obj_in, owner_id=user.id
    )
    if not can_be:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=reason
        )
    if not await validate_token(obj_in.token):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Token is not valid'
        )
    bot = await repo.bot.create_with_owner(
        db_collection,
        obj_in=obj_in,
        owner_id=user.id
    )
    await webhook.set_(bot)
    return schemas.Bot(**bot.dict())


@router.patch(
    '/{bot_id}',
    response_model=schemas.Bot,
    status_code=status.HTTP_200_OK
)
async def update_bot(
        bot_id: str,
        obj_in: schemas.BotUpdate,
        db_collection: DBCollection = Depends(deps.get_db_collection.api.bots),
        user: schemas.UserInDB = Depends(deps.get_current_user)
):
    bot = await repo.bot.get(db_collection, id_=bot_id)
    if not bot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if not(bot.owner_id == user.id or user.is_superuser):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    bot = await repo.bot.update(db_collection, id_=bot_id, obj_in=obj_in)
    return schemas.Bot(**bot.dict())


@router.patch(
    '/{bot_id}/recreate_webhook',
    response_class=Response,
    status_code=status.HTTP_200_OK
)
async def recreate_webhook(
        bot_id: str,
        db_collection: DBCollection = Depends(deps.get_db_collection.api.bots),
        user: schemas.UserInDB = Depends(deps.get_current_user)
):
    bot = await repo.bot.get(db_collection, id_=bot_id)
    if not bot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if not(bot.owner_id == user.id or user.is_superuser):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    await webhook.set_(bot)


@router.get(
    '/{bot_id}/check_webhook',
    response_model=schemas.WebhookUp,
    status_code=status.HTTP_200_OK
)
async def check_webhook(
        bot_id: str,
        db_collection: DBCollection = Depends(deps.get_db_collection.api.bots),
        user: schemas.UserInDB = Depends(deps.get_current_user)
):
    bot = await repo.bot.get(db_collection, id_=bot_id)
    if not bot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if not(bot.owner_id == user.id or user.is_superuser):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return schemas.WebhookUp(is_up=(await webhook.is_up(bot)))


@router.delete(
    '/{bot_id}',
    response_model=schemas.Bot,
    status_code=status.HTTP_200_OK
)
async def remove_bot(
        bot_id: str,
        db_collection: DBCollection = Depends(deps.get_db_collection.api.bots),
        user: schemas.UserInDB = Depends(deps.get_current_user)
):
    bot = await repo.bot.get(db_collection, id_=bot_id)
    if not bot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if not(bot.owner_id == user.id or user.is_superuser):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    bot = await repo.bot.remove(db_collection, id_=bot_id)
    await webhook.delete(bot)
    return schemas.Bot(**bot.dict())
