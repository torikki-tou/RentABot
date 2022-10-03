from aiogram.dispatcher.filters.builtin import CommandStart

from src.telegram.scenarios.second import handlers
from src.telegram.helpers.dispatcher import get_base_dispatcher


dispatcher = get_base_dispatcher()

dispatcher.register_message_handler(
    handlers.base.start, CommandStart(), state='*')
dispatcher.register_message_handler(
    handlers.base.echo, state='*')
