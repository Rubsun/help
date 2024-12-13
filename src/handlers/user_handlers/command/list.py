from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command

from src.handlers.user_handlers.command.router import router
from src.user_data import user_data

@router.message(F.text == 'Корзина')
@router.message(Command('list'))
async def command_list(message: Message):
    materials = user_data[message.from_user.id]["list"]
    if materials:
        await message.answer("Ваш список:\n" + "\n".join(materials))
    else:
        await message.answer("Ваш список пуст.")
