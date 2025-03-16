import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InputFile
from aiogram.utils import executor

from config import TOKEN  # Импортируем токен из config.py

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Словарь для отслеживания брони
booked_tables = {}

# Импорт кнопок
from keyboards import menu_keyboard

# Приветствие
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Приветствуем, дорогой гость! Что бы ты хотел сделать?", 
        reply_markup=menu_keyboard
    )

# Запуск бота
if name == "__main__":
    executor.start_polling(dp, skip_updates=True)

