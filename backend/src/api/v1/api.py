from fastapi import APIRouter

from src.api.v1.endpoints import users, bots


router = APIRouter()
router.include_router(router=users.router, prefix='/users')
router.include_router(router=bots.router, prefix='/bots')
