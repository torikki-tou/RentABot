from enum import Enum

from src.telegram import scenarios
from src.telegram.helpers.dispatcher import CustomDispatcher


class Scenario(str, Enum):
    first = 'first'
    second = 'second'


def get_dispatcher(scenario: Scenario) -> CustomDispatcher:
    match scenario:
        case Scenario.first:
            dispatcher = scenarios.first.dispatcher
        case Scenario.second:
            dispatcher = scenarios.second.dispatcher
        case _:
            raise
    return dispatcher
