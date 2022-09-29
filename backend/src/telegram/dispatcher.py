from enum import Enum
from contextlib import contextmanager
from typing import ContextManager

from aiogram import Dispatcher, Bot

from src.telegram import scenarios
from src.telegram.helpers.dispatcher import PredefinedDispatcher


class Scenario(str, Enum):
    first = 'first'
    second = 'second'


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
        scenario: Scenario, bot_id: str, bot_token: str
) -> ContextManager[PredefinedDispatcher]:
    dispatcher = get_dispatcher(scenario)
    with dispatcher.bot.with_token(bot_token, validate_token=False),\
            dispatcher.storage.with_prefix(str(bot_id)):
        Dispatcher.set_current(dispatcher)
        Bot.set_current(dispatcher.bot)
        yield dispatcher
