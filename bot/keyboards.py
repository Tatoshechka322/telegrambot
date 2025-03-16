from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("📍 Карта столов"))
menu_keyboard.add(KeyboardButton("📜 Основные правила заведения"))
menu_keyboard.add(KeyboardButton("📅 Бронирование столов"))
menu_keyboard.add(KeyboardButton("⭐ Оставить отзыв"))
menu_keyboard.add(KeyboardButton("🎉 Специальные события"))
menu_keyboard.add(KeyboardButton("🎁 Позови друзей"))
