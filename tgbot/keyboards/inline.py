import aiogram
from aiogram import types
from aiogram.utils.exceptions import MessageNotModified
from aiogram.utils.callback_data import CallbackData
from AssistantPriceBot import db

async def view_keyboard(url_product, message):
    buttons_view = [
        types.InlineKeyboardButton(text="Товар", url=url_product),
        types.InlineKeyboardButton(text="Удалить товар", callback_data = "delete_product")
    ]
    keyboard_view = types.InlineKeyboardMarkup(row_width=3)
    keyboard_view.add(*buttons_view)
    return keyboard_view

async def tracking_keyboard(url_pr):
    buttons_view = [
        types.InlineKeyboardButton(text="Товар", url=url_pr)
    ]
    keyboard_view = types.InlineKeyboardMarkup(row_width=3)
    keyboard_view.add(*buttons_view)
    return keyboard_view