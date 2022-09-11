from typing import Optional

from pydantic import BaseModel


class BotBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    owner_id: Optional[str] = None


class BotCreate(BotBase):
    title: str
    token: str
    owner_id: str


class BotUpdate(BotBase):
    token: str


class BotInDBBase(BotBase):
    id: str
    title: str
    description: Optional[str] = None
    token: str
    owner_id: str


class Bot(BotInDBBase):
    pass
