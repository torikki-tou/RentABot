from aiogram.types import Message


async def start(message: Message):
    await message.answer('start')


async def echo(message: Message):
    await message.answer('second')
