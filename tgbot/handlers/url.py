from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.markdown import hcode
from aiogram.dispatcher.filters import Text
import requests
from bs4 import BeautifulSoup
from AssistantPriceBot import dp

async def citilink(message):
    link = message.text
    responce = requests.get(link)
    soup = BeautifulSoup(responce.text, 'lxml')
    block = soup.find('div', class_ = "ProductCardLayout__product-description")
    check_price = block.find('span', class_ = "ProductHeader__price-default_current-price js--ProductHeader__price-default_current-price").text

    return check_price


class Price_product(StatesGroup):
    waiting_for_url = State()

async def url_start(message: types.Message):
    await Price_product.waiting_for_url.set()
    await message.reply("Отправьте ссылку: ")

async def send_product_url(message: types.MessageEntity, state: FSMContext):
    await Price_product.next()
    await message.answer(str(await citilink(message)))

def register_url(dp: Dispatcher):
    dp.register_message_handler(url_start, commands = 'send_product_url')
    dp.register_message_handler(send_product_url, state = Price_product.waiting_for_url)
