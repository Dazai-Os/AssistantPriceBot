from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.markdown import hcode
from aiogram.dispatcher.filters import Text
from AssistantPriceBot import dp
from AssistantPriceBot import db

class View_product(StatesGroup):
    waiting_for_view = State()

async def view_start(message):
    answer_view = await db.view_product(message.from_user.id)
    auto_number = 1
    for i in answer_view:
        result = str(auto_number) + "." + i[1] + " - " + i[2]
        await message.reply(result)
        await message.answer(i[0])
        auto_number += 1
    

def register_view_pr(dp: Dispatcher):
    dp.register_message_handler(view_start, commands="view_all_products")
