from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from ..answer_data.answer_bot_data import ANSWER
from aiogram import Router
from Telegram_bot.Keyboards.Keyboards import keyboard


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки с параметром "url"',
        reply_markup=keyboard)
async def process_help_command(message: Message):
    await message.answer(text=ANSWER['/help'])
