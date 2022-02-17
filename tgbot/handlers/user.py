from aiogram import Dispatcher
from aiogram.types import Message, ReplyKeyboardRemove
from tgbot.keyboards.reply import menu
from aiogram.dispatcher.filters import Text


async def user_start(message: Message):
    await message.answer("Привет пользователь. Выбери команду из предложенных и начаинай пользоваться!", reply_markup=menu)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")