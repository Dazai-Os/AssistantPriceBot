from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

menu = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Отправить url товара")],
        [KeyboardButton(text = "Просмотр товаров")],
    ],
    resize_keyboard=True
)
