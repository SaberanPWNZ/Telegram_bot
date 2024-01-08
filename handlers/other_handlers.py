
from aiogram import Router, F
from ..answer_data.answer_bot_data import ANSWER
from aiogram.filters import CommandStart
from aiogram.types import (Message,
                           ReplyKeyboardRemove)


router = Router()


# @router.message()
# async def send_echo(message: Message):
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.reply(text=answer['no_echo'])


# @router.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(
#         text='Футбол СБ на 10:00. Будешь?',
#         reply_markup=Kb
#     )
#
#
# # Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
# @router.message(F.text == 'Обязательно приду на футбол 🖐')
# async def process_football_yes_answer(message: Message):
#     await message.answer(
#         text='КРАСАВА, НЕ ОПАЗДЫВАЙ!',
#         #reply_markup=ReplyKeyboardRemove()
#     )
#
#
# @router.message(F.text == 'Занят.Бухаю 🍻')
# async def process_football_no_answer(message: Message):
#     await message.answer(
#         text='Понимаю, 3-й тайм тоже важно.\n'
#              'Рожкову - Привет!',
#         #reply_markup=ReplyKeyboardRemove()
#     )
