from aiogram import types
from aiogram.filters import CommandStart

from src.handlers.user_handlers.command.router import router
from src.keyboards import main_menu
from src.user_data import user_data


@router.message(CommandStart())
async def start_command(message: types.Message):
    user_data[message.from_user.id] = {"selected": [], "list": []}
    await message.answer(
        "Привет! Я помогу подобрать материалы для вышивки. Что вы хотите подобрать?",
        reply_markup=main_menu
    )
