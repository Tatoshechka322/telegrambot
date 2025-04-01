import logging

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from keyboards import menu_keyboard, table_keyboard

router = Router()

logging.basicConfig(level=logging.INFO)

booked_tables = {}

@router.message(F.text == "Карта столов")
async def send_table_map(message: Message):
    logging.info("Вызван send_table_map")
    photo = FSInputFile("images/table_map.jpg")
    await message.answer_photo(photo, caption="Схема расположения столов.")


@router.message(F.text == "Основные правила заведения")
async def send_rules(message: Message):
    logging.info("Вызван send_rules")
    rules_text = """
    📜 Основные правила нашего заведения:

    1. Бронирование стола:
       - Время бронирования стола составляет 2 часа. Если вы хотите продлить бронь, пожалуйста, свяжитесь с нами заранее.
       - Бронь снимается через 15 минут после указанного времени, если вы не предупредили о задержке.

    2. Свои напитки и еда:
       - Приносить с собой напитки и еду, к сожалению, нельзя. У нас широкий ассортимент блюд и напитков на любой вкус!

    3. Возрастные ограничения:
       - В вечернее время (после 21:00) вход лицам младше 18 лет воспрещен.

    4. Дресс-код:
       - Мы приветствуем стильную и опрятную одежду. Спортивная одежда и обувь не рекомендуются.
    """
    await message.answer(rules_text, reply_markup=menu_keyboard)


@router.message(F.text == "Бронирование столов")
async def book_table(message: Message):
    logging.info("Вызван book_table")
    await message.answer("Выберите номер стола:", reply_markup=table_keyboard())


@router.message(F.text == "Специальные события")
async def send_events(message: Message):
    logging.info("Вызван send_events")
    events_text = """
    🎉 Специальные события этой недели:

    Понедельник: "Вечер настольных игр"
    - Крутая атмосфера для игр с самыми близкими людьми!

    Среда: "Вечер живой музыки"
    - С 20:00 для вас играет кавер-группа "Золотые хиты". Вход свободный!

    Пятница: "Коктейльная вечеринка"
    - С 22:00 скидка 50% на все коктейли в баре!

    Суббота: "Японский уикенд"
    - Проведите прекрасный вечер с нашей чайной церемонией с различными сортами чая!

    Воскресенье: "Караоке-ночь"
    - С 19:00 пойте любимые песни и получайте призы!

    Не пропустите наши яркие события! 🎉
    """
    await message.answer(events_text, reply_markup=menu_keyboard)


@router.message(F.text.in_({"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "vip-1", "vip-2"}))
async def process_table_booking(message: Message):
    logging.info("Вызван process_table_booking")
    table_number = message.text
    if table_number in booked_tables:
        await message.answer(f"❌ Этот стол уже забронирован, выберите другой.", reply_markup=table_keyboard())
    else:
        booked_tables[table_number] = message.from_user.id
        await message.answer(f"✅ Стол {table_number} успешно забронирован на ваше имя!", reply_markup=menu_keyboard)


@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        "Приветствуем, дорогой гость! Что бы ты хотел сделать?",
        reply_markup=menu_keyboard
    )
