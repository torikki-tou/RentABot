from src.repo.base import BaseRepo
from src.schemas.user import UserInDBBase, UserCreate, UserUpdate


class UserRepo(BaseRepo[UserInDBBase, UserCreate, UserUpdate]):
    pass
