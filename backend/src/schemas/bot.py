from typing import Optional

from pydantic import BaseModel

from src.core.settings import Scenario


class BotBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    scenario: Optional[Scenario] = None


class BotCreate(BotBase):
    title: str
    token: str
    scenario: Scenario


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
    webhook_key: str


class WebhookUp(BaseModel):
    is_up: bool
