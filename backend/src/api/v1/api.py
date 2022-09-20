from fastapi import APIRouter

from src.api.v1.endpoints import (
    users,
    bots,
    auth,
    webhook
)


router = APIRouter()
router.include_router(
    router=users.router, prefix='/users', tags=['users'])
router.include_router(
    router=bots.router, prefix='/bots', tags=['bots'])
router.include_router(
    router=auth.router, prefix='/auth', tags=['auth'])
router.include_router(
    router=webhook.router, prefix='/webhook', tags=['webhook'])
