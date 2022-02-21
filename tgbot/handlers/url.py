from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.filters.state import State, StatesGroup

from AssistantPriceBot import db
from tgbot.misc.parser import citilink


class PriceProduct(StatesGroup):
    waiting_for_url = State()


#message handler start
async def url_start(message: types.Message):
    await message.answer("Отправьте ссылку с ситилинка и товар будет отслеживаться(Пример ссылки - https://www.citilink.ru/product/holodilnik-lg-ga-b509cetl-bezhevyi-1387047/):")
    await PriceProduct.waiting_for_url.set()


#calls the add user function, and tells you if the product is already there
async def send_product_url(message: types.MessageEntity):
    await PriceProduct.next()

    test_main = await add_user_product(message)
    if test_main:
        await message.reply("Товар успешно отслеживается")
    else:
        await message.reply("Товар уже отслеживается")


#calls the add user method in a database class. handles an invalid link
async def add_user_product(message):
    link = message.text
    if "https://www.citilink.ru" in str(link):
        name_product, now_price = await citilink(link)
        test = await db.add_user_product_db(int(message.from_user.id), str(message.text),
                                            str(name_product), str(now_price))
    else:
        await message.reply("Вы прислали некоректную ссылку")
        raise CancelHandler()
    return test


def register_url(dp: Dispatcher):
    dp.register_message_handler(url_start, commands = 'send_product_url')
    dp.register_message_handler(url_start, Text(equals='Отправить url товара'))
    dp.register_message_handler(send_product_url, state = PriceProduct.waiting_for_url)