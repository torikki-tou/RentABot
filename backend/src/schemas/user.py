from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None


class UserCreate(UserBase):
    name: str
    email: str
    password: str


class UserUpdate(UserBase):
    password: str


class UserInDBBase(UserBase):
    hashed_password: str


class User(UserInDBBase):
    pass
