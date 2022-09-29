from aiogram import Dispatcher, Bot

from src.telegram.helpers.storage import RedisStorage


class PredefinedDispatcher(Dispatcher):
    storage: RedisStorage


def get_base_dispatcher() -> PredefinedDispatcher:
    bot = Bot('0', validate_token=False)
    storage = RedisStorage(host='redis')
    return PredefinedDispatcher(bot, storage=storage)
