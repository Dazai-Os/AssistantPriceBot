from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.callback_data import CallbackData
from AssistantPriceBot import db
from tgbot.misc.parser import citilink


class Price_product(StatesGroup):
    waiting_for_url = State()


async def url_start(message: types.Message):
    await Price_product.waiting_for_url.set()
    await message.answer("Отправьте ссылку и товар будет отслеживаться:")


async def send_product_url(message: types.MessageEntity, state: FSMContext):
    await Price_product.next()
    test_main = await add_user_product(message)
    if test_main:
        await message.reply("Товар успешно отслеживается")
    else:
        await message.reply("Товар уже отслеживается")



async def add_user_product(message):
    link = message.text
    name_product, now_price = await citilink(link)
    test = await db.add_user_product_db(int(message.from_user.id), str(message.text), str(name_product), str(now_price))
    if test:
        return True
    else:
        return False



def register_url(dp: Dispatcher):
    dp.register_message_handler(url_start, commands = 'send_product_url')
    dp.register_message_handler(url_start, Text(equals='Отправить url товара'))
    dp.register_message_handler(send_product_url, state = Price_product.waiting_for_url)