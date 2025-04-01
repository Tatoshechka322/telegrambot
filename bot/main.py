import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config import TOKEN
from handlers import router  # Импортируем роутер из handlers.py

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать работу с ботом")
    ]
    await bot.set_my_commands(commands)


async def main():
    print("Бот запущен...")
    await set_commands(bot)
    dp.include_router(router)  # Подключаем обработчики из handlers.py
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

