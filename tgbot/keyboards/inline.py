import aiogram
from aiogram import types
from aiogram.utils.exceptions import MessageNotModified
from aiogram.utils.callback_data import CallbackData

async def view_keyboard(message):
    buttons_view = [
        types.InlineKeyboardButton(text="Товар", url=message)
    ]
    keyboard_view = types.InlineKeyboardMarkup(row_width=3)
    keyboard_view.add(*buttons_view)
    return keyboard_view
