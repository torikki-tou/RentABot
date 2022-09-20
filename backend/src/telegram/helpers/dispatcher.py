from aiogram import Dispatcher, Bot

from src.telegram.helpers.storage import RedisStorage


class CustomDispatcher(Dispatcher):
    storage: RedisStorage


def get_base_dispatcher() -> CustomDispatcher:
    bot = Bot('0', validate_token=False)
    storage = RedisStorage(host='redis')
    return CustomDispatcher(bot, storage=storage)
