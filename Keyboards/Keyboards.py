from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType,InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot
from aiogram.types import BotCommand
from Telegram_bot.answer_data.answer_bot_data import COMANDS_START_MENU




button_OK = KeyboardButton(text="Обязательно приду на футбол 🖐")
button_NO = KeyboardButton(text="Занят.Бухаю 🍻")



url_button_1 = InlineKeyboardButton(
    text='Курс "Телеграм-боты на Python и AIOgram"',
    url='https://stepik.org/120924'
    )

url_button_2 = InlineKeyboardButton(
    text='Документация Telegram Bot API',
    url='https://core.telegram.org/bots/api')

url_button_3 = InlineKeyboardButton(
    text="BMV X5 2015",
    url="https://qna.habr.com/q/1242714",

)
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1],
                     [url_button_2],
                     [url_button_3]]
    )




# Функция для настройки кнопки Menu бота

