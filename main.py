import asyncio
import logging
from datetime import datetime
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from os import getenv
from aiogram.utils.exceptions import BotBlocked

from strings import *
from objects import *
from utils import TestStates

bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.INFO)

commands = {
    "/start": "Приветствует пользователя!",
    "/help": "Выводит это сообщение помощи"
}


def create_help():
    ans = ""
    for command in commands:
        ans += f"{command} - {commands[command]}\n"
    return ans


@dp.message_handler(commands="help")
async def cmd_test1(message: types.Message):
    await message.answer(create_help())


@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    hello = "Приветствую тебя, я мало чего могу, но вот, что могу:\n"
    await message.answer(hello + create_help())


if __name__ == "__main__":
    print(TestStates.all())
    executor.start_polling(dp, skip_updates=True)