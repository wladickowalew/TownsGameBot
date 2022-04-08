import logging
from os import getenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from strings import *
from objects import *
from utils import MyStates

bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.INFO)

commands = {
    "/start": START_DESCRIBE,
    "/help": HELP_DESCRIBE,
    "/start_game": START_GAME_DESCRIBE
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
    await message.answer(START_MESSAGE + create_help())


@dp.message_handler(commands="start_game")
async def start_game(message: types.Message):
    if message.from_user.id not in users:
        user = User(message.from_user.id)
    else:
        user = users[message.from_user.id]
    state = dp.current_state(user=user.id)
    await state.set_state(TestStates.WAITING_ANSWER[0])
    await message.answer(START_GAME_MESSAGE)
    await bot.send_photo(chat_id=user.id, photo=open(user.get_photo(),'rb'))

if __name__ == "__main__":
    print(TestStates.all())
    executor.start_polling(dp, skip_updates=True)
