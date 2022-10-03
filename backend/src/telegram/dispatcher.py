from contextlib import contextmanager
from typing import ContextManager

from aiogram import Dispatcher, Bot
from aiogram.utils.exceptions import Unauthorized

from src.telegram import scenarios
from src.telegram.helpers.dispatcher import PredefinedDispatcher
from src.core.settings import Scenario


def get_dispatcher(scenario: Scenario) -> PredefinedDispatcher:
    match scenario:
        case Scenario.first:
            return scenarios.first.dispatcher
        case Scenario.second:
            return scenarios.second.dispatcher
        case _:
            raise


@contextmanager
def dispatcher_context(
        scenario: Scenario, storage_prefix: str, bot_token: str
) -> ContextManager[PredefinedDispatcher]:
    dispatcher = get_dispatcher(scenario)
    try:
        with dispatcher.bot.with_token(bot_token, validate_token=False),\
                dispatcher.storage.with_prefix(storage_prefix):
            Dispatcher.set_current(dispatcher)
            Bot.set_current(dispatcher.bot)
            yield dispatcher
    except Unauthorized:
        ...
