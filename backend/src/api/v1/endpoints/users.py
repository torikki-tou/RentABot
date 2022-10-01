from fastapi import APIRouter, Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorCollection as DBCollection

from src import schemas, repo
from src.api import deps

router = APIRouter()


@router.get(
    '/{user_id}',
    response_model=schemas.User,
    status_code=status.HTTP_200_OK
)
async def read_user(
        user_id: str,
        db_collection: DBCollection = Depends(deps.get_users_collection)
):
    user = await repo.user.get(db_collection, id_=user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return schemas.User(**user.dict())


@router.post(
    '/',
    response_model=schemas.User,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
        obj_in: schemas.UserCreate,
        db_collection: DBCollection = Depends(deps.get_users_collection)
):
    can_be, reason = await repo.user.can_be_created(
        db_collection, obj_in=obj_in
    )
    if not can_be:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=reason
        )
    user = await repo.user.create(db_collection, obj_in=obj_in)
    return schemas.User(**user.dict())


@router.patch(
    '/{user_id}',
    response_model=schemas.User,
    status_code=status.HTTP_200_OK
)
async def update_user(
        user_id: str,
        obj_in: schemas.UserUpdate,
        db_collection: DBCollection = Depends(deps.get_users_collection)
):
    user = await repo.user.update(db_collection, id_=user_id, obj_in=obj_in)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return schemas.User(**user.dict())


@router.delete(
    '/{user_id}',
    response_model=schemas.User,
    status_code=status.HTTP_200_OK
)
async def remove_user(
        user_id: str,
        db_collection: DBCollection = Depends(deps.get_users_collection)
):
    user = await repo.user.remove(db_collection, id_=user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return schemas.User(**user.dict())
