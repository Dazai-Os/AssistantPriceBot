from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.markdown import hcode
from aiogram.dispatcher.filters import Text
import requests
from bs4 import BeautifulSoup
from AssistantPriceBot import dp
from AssistantPriceBot import db



class Price_product(StatesGroup):
    waiting_for_url = State()


async def url_start(message: types.Message):
    await Price_product.waiting_for_url.set()
    await message.reply("Отправьте ссылку и товар будет отслеживаться: ")


async def send_product_url(message: types.MessageEntity, state: FSMContext):
    await Price_product.next()
    test_main = await add_user_product(message)
    if test_main == True:
        await message.reply("Товар успешно отслеживается")
    else:
        await message.reply("Товар уже отслеживается")



async def add_user_product(message):
    name_product, now_price = await citilink(message)
    test = await db.add_user_product_db(int(message.from_user.id), str(message.text), str(name_product), str(now_price))
    if test == True:
        return True
    else:
        return False



async def citilink(message):
    link = message.text
    responce = requests.get(link)
    soup = BeautifulSoup(responce.text, 'lxml')
    block = soup.find('div', class_ = "ProductCardLayout__product-description")
    price = block.find('span', class_ = "ProductHeader__price-default_current-price js--ProductHeader__price-default_current-price")

    name_product = block.find('h1', class_ = "Heading Heading_level_1 ProductHeader__title")

    return name_product.get_text(strip = True), price.get_text(strip = True)




def register_url(dp: Dispatcher):
    dp.register_message_handler(url_start, commands = 'send_product_url')
    dp.register_message_handler(send_product_url, state = Price_product.waiting_for_url)