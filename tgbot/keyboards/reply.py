from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard = [
                [KeyboardButton(text = "Отправить url товара"), KeyboardButton(text = "Просмотр товаров")],
                [KeyboardButton(text = "Помощь")],
    ],
    resize_keyboard=True
)
