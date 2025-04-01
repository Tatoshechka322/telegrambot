from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Основные правила заведения"),
        ],
        [
            KeyboardButton(text="Бронирование столов"),
            KeyboardButton(text="⭐ Оставить отзыв"),
        ],
        [
            KeyboardButton(text="Специальные события"),
            KeyboardButton(text="👥 Позови друзей"),
        ],
    ],
    resize_keyboard=True
)


def table_keyboard():
    """Создает клавиатуру с номерами столов."""
    table_numbers = [str(i) for i in range(1, 15)]
    vip_tables = ["vip-1", "vip-2"]
    all_tables = table_numbers + vip_tables
    keyboard = []
    row = []
    for table in all_tables:
        row.append(KeyboardButton(text=table))
        if len(row) == 3:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)

    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
