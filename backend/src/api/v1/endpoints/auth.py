from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from motor.motor_asyncio import AsyncIOMotorCollection as DBCollection

from src import schemas, repo
from src.core import security
from src.api import deps


router = APIRouter()


@router.post(
    '/token',
    response_model=schemas.Token,
    status_code=status.HTTP_200_OK
)
async def get_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db_collection: DBCollection = Depends(deps.get_users_collection)
):
    user = await repo.user.authenticate(
        db_collection,
        username=form_data.username,
        password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return schemas.Token(
        access_token=security.create_access_token(user.id)
    )
