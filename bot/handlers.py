from aiogram import types
from aiogram.types import InputFile
from main import bot, dp, booked_tables

@dp.message_handler(lambda message: message.text == "📍 Карта столов")
async def send_table_map(message: types.Message):
    photo = InputFile("images/table_map.jpg")  # Используем схему столов
    await bot.send_photo(message.chat.id, photo, caption="Вот схема расположения столов.")

@dp.message_handler(lambda message: message.text == "📅 Бронирование столов")
async def book_table(message: types.Message):
    await message.answer("Введите номер стола, который хотите забронировать:")

@dp.message_handler(lambda message: message.text.isdigit())  
async def process_table_booking(message: types.Message):
    table_number = int(message.text)
    
    if table_number in booked_tables:
        await message.answer("❌ Этот стол уже забронирован, выберите другой.")
    else:
        booked_tables[table_number] = message.from_user.id  
        await message.answer(f"✅ Стол {table_number} успешно забронирован на ваше имя!")
