from aiogram import Bot
from aiogram.types import Message
from core.keyboards.inline import *
from core.keyboards.reply import reply_keyboard
import surrogates

sp_object = ["Иностранный язык в сфере юриспруденции",
             "Элективные дисциплины по физической культуре и спорту",
             "Уголовное право",
             "Трудовое право",
             "Криминология",
             "Социокультурная коммуникация",
             "Семейное право",
             "Налоговое право",
             "Гражданское право",
             "Безопасность жизнедеятельности",
             "Право социального обеспечения",
             "Английский язык",
             "Немецкий язык",
             "История России",
             "Основы программирования",
             "Математический анализ",
             "Физика",
             "Основы экономики и финансовой грамотности",
             "Дискреная математика"]


async def idk(message: Message):
    await message.answer(f'Простите, я вас не понимаю.' + surrogates.decode("\U0001f972"))


async def reset(message: Message):
    await message.answer(f"Вы успешно сбросили клавиатуру", reply_markup=reply_keyboard)


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, F"Привет, {message.from_user.first_name}, рад тебя видеть в"
                                                 F" нашем образовательном боте.", reply_markup=reply_keyboard)
    await message.answer_sticker('CAACAgEAAxkBAAIE5GXOP6giDChxrSaNJ2QGW6OoIrmsAALxAQACOA6CEXTVKqzkcGAkNAQ')


async def get_sticker(message: Message, bot: Bot):
    await message.answer("Классный стикер, я его себе сохраню")
    await message.answer_sticker(message.sticker.file_id)


async def news(message: Message):
    await message.answer(f'<a href="https://vernost67.ru/news">- Сайт</a>\n<a '
                         f'href="https://t.me/vernostChannel">- Канал</a>\n Чтобы вы не пропустили ни одной новости о'
                         f' наших друзьях.', parse_mode="HTML",
                         disable_web_page_preview=True)


async def all_objects(message: Message):
    await message.answer(f'<b>{sp_object[0]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=foreign_language_in_the_field_of_jurisprudence)
    await message.answer(f'<b>{sp_object[1]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=elective_disciplines_in_physical_culture_and_sports)
    await message.answer(f'<b>{sp_object[2]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=criminal_law)
    await message.answer(f'<b>{sp_object[3]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=labor_Law)
    await message.answer(f'<b>{sp_object[4]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=criminology)
    await message.answer(f'<b>{sp_object[5]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=sociocultural_communication)
    await message.answer(f'<b>{sp_object[6]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=family_law)
    await message.answer(f'<b>{sp_object[7]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=tax_law)
    await message.answer(f'<b>{sp_object[8]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=civil_law)
    await message.answer(f'<b>{sp_object[9]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=life_safety)
    await message.answer(f'<b>{sp_object[10]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=the_right_of_obligatory_security)
    await message.answer(f'<b>{sp_object[11]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=english_language)
    await message.answer(f'<b>{sp_object[12]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=german_language)
    await message.answer(f'<b>{sp_object[13]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=russian_history)
    await message.answer(f'<b>{sp_object[14]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=basics_of_programming)
    await message.answer(f'<b>{sp_object[15]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=mathematical_analysis)
    await message.answer(f'<b>{sp_object[16]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=physics)
    await message.answer(f'<b>{sp_object[17]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=fundamentals_of_economics_and_financial_literacy)
    await message.answer(f'<b>{sp_object[18]}</b>', parse_mode="HTML", disable_web_page_preview=True,
                         reply_markup=discrete_mathematics)


async def about(message: Message):
    await message.answer(f'"Верность" - это приют и реабилитационный центр. Наш бот был разработан для более удобного '
                         f'поиска хозяев для животных, чтобы каждый из них смог найти вечно любящий дом. Мы хотим '
                         f'помочь приюту и спасти больше жизней❤. Подробности на<a href="https://vernost67.ru/"> '
                         f'сайте</a>', parse_mode="HTML", disable_web_page_preview=True)
