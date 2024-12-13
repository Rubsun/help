from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message

from src.handlers.user_handlers.command.router import router
from src.user_data import user_data

@router.message(F.text == 'Очистить корзину')
@router.message(Command('delete'))
async def delete_list(message: Message):
    user_data[message.from_user.id]["list"] = []
    await message.answer("Корзина очищена")