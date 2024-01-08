import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from Telegram_bot.handlers import other_handlers, user_handlers
from config_data.config import Config, load_config


async def main() -> None:
    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token,parse_mode='HTML')
    dp = Dispatcher()

    # dp.include_router(other_handlers.router)
    dp.include_router(user_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
