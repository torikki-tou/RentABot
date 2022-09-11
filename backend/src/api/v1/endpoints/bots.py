from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorCollection

from src import schemas
from src.api import deps


router = APIRouter()


@router.get('/{bot_id}', response_model=schemas.Bot)
def read_bot(
        *,
        bot_id: str,
        db_collection: AsyncIOMotorCollection = Depends(deps.get_bots_collection)
):
    ...


@router.post('/', response_model=schemas.Bot)
def create_bot(
        *,
        obj_in: schemas.BotCreate,
        db_collection: AsyncIOMotorCollection = Depends(deps.get_bots_collection)
):
    ...


@router.put('/{bot_id}', response_model=schemas.Bot)
def update_bots(
        *,
        bot_id: str,
        obj_in: schemas.BotUpdate,
        db_collection: AsyncIOMotorCollection = Depends(deps.get_bots_collection)
):
    ...


@router.delete('/{bot_id}', response_model=schemas.Bot)
def remove_bot(
        *,
        bot_id: str,
        db_collection: AsyncIOMotorCollection = Depends(deps.get_bots_collection)
):
    ...
