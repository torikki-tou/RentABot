from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def start(message: Message, state: FSMContext):
    await message.answer('start')
    await state.set_state('second')


async def echo(message: Message, state: FSMContext):
    await message.answer('second')
    await message.answer(await state.get_state())
