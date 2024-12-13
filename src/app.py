import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.bot import setup_bot, setup_dp
from dotenv import load_dotenv

from src.handlers.user_handlers.command.router import router as command_router
from src.handlers.user_handlers.callback.router import router as callback_router
load_dotenv()


async def start_polling():
    bot = Bot(token=getenv('BOT_TOKEN'))
    dp = Dispatcher(storage=MemoryStorage())
    setup_dp(dp)
    setup_bot(bot)
    dp.include_router(command_router)
    dp.include_router(callback_router)
    await bot.delete_webhook()
    await dp.start_polling(bot)



if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    asyncio.run(start_polling())
