# import requests
# import time
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, ChatMemberUpdatedFilter, KICKED, BaseFilter
from aiogram.types import Message, ChatMemberUpdated
from environs import Env
import os

env = Env()              # Создаем экземпляр класса Env
env.read_env()

bot_token = env('BOT_TOKEN')
API_URL = f'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('
dp = Dispatcher()
bot = Bot(bot_token)
# logging.basicConfig(level=logging.DEBUG)
# logging.getLogger(__name__)


@dp.message(Command(commands="start"))  # Обработка комонды Старт
async def echo_start_command(message: Message):
    await message.answer("Shalom!")


@dp.message(F.content_type == "photo")
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[-1].file_id)



@dp.message(Command(commands="end"))
async def send_echo(message: Message):
    await message.answer(text="go out")
    # logging.debug('Это лог уровня DEBUG')
    # logging.info('Это лог уровня INFO')
    # logging.warning('Это лог уровня WARNING')
    # logging.error('Это лог уровня ERROR')
    # logging.critical('Это лог уровня CRITICAL')


async def send_help_info(message: Message):
    await message.answer(text="This bot on test stage now\n Please, don't upset :D")


# dp.message.register(echo_start_command, Command(commands='start'))
dp.message.register(send_help_info, Command(commands='help'))
dp.message.register(send_echo)
dp.message.register(send_photo_echo, F.photo)



if __name__ == "__main__":
    dp.run_polling(bot)
