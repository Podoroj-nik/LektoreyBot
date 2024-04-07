from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Список предметов:"
        ),
    ]
], resize_keyboard=True, input_field_placeholder='Выберите кнопку')
