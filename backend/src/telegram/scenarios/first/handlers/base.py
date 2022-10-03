from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def start(message: Message, state: FSMContext):
    await message.answer('start')
    await state.set_state('first')


async def echo(message: Message, state: FSMContext):
    await message.answer('first')
    await message.answer(await state.get_state())
