from aiogram import Dispatcher, Bot

from src.telegram.helpers.storage import UpgradedRedisStorage


class PredefinedDispatcher(Dispatcher):
    storage: UpgradedRedisStorage


def get_base_dispatcher() -> PredefinedDispatcher:
    bot = Bot('0', validate_token=False)
    storage = UpgradedRedisStorage(host='redis')
    return PredefinedDispatcher(bot, storage=storage)
