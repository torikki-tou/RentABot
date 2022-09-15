from typing import Optional

from pydantic import BaseModel


class BotBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class BotCreate(BotBase):
    title: str
    token: str


class BotUpdate(BotBase):
    token: Optional[str] = None


class BotInDBBase(BotBase):
    id: str
    title: str
    owner_id: str


class Bot(BotInDBBase):
    pass


class BotInDB(BotInDBBase):
    token: str
