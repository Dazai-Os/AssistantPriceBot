from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

async def help_start(message: types.Message):
    await message.answer("""Пока поддерживается отслеживание только с ситилинка""")
    await message.answer("""Команда /send_product_url (Отправить url товара) - это команда с помощью, которой вы добавляете товары с citilink в отслеживаемое
    Чтобы ей поспользоваться вы должны найти интересующий вас товар на ситилинке и прислать url ссылку этого товара""")
    
    await message.answer("""Команда /view_product (Просмотр товаров) - это команда, которая показывает и присылает вместе с ссылками 
отслеживаемы ваши товары""")
    

def register_help(dp: Dispatcher):
    dp.register_message_handler(help_start, commands = 'help')
    dp.register_message_handler(help_start, Text(equals = "Помощь"))