from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.markdown import hcode
from aiogram.dispatcher.filters import Text
import requests
from bs4 import BeautifulSoup
from AssistantPriceBot import dp
from AssistantPriceBot import db

async def citilink(message):
    link = message.text
    responce = requests.get(link)
    soup = BeautifulSoup(responce.text, 'lxml')
    block = soup.find('div', class_ = "ProductCardLayout__product-description")
    price = block.find('span', class_ = "ProductHeader__price-default_current-price js--ProductHeader__price-default_current-price").text

    name_product = block.find('h1', class_ = "Heading Heading_level_1 ProductHeader__title").text

    return name_product, price

async def add_user_product(message):
    name_product, now_price = await citilink(message)
    track = True
    await db.add_user_product(int(message.from_user.id), str(message.text), str(name_product), str(now_price), bool(track))

class Price_product(StatesGroup):
    waiting_for_url = State()

async def url_start(message: types.Message):
    await Price_product.waiting_for_url.set()
    await message.reply("Отправьте ссылку и товар будет отслеживаться: ")

async def send_product_url(message: types.MessageEntity, state: FSMContext):
    await Price_product.next()
    await add_user_product(message)

def register_url(dp: Dispatcher):
    dp.register_message_handler(url_start, commands = 'send_product_url')
    dp.register_message_handler(send_product_url, state = Price_product.waiting_for_url)