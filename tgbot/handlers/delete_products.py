from aiogram import Dispatcher, types

from AssistantPriceBot import db

#removing the product selected by the inline keypad
async def delete_product(call: types.CallbackQuery):
    id_user = call.from_user.id
    for i in call.message.reply_markup:
        for j in i:
            if type(j[0][0]) == dict:
                url_product = j[0][0].get('url')
    await db.delete_product_db(id_user, url_product)
    await call.message.answer("Товар удален")


def register_callback_handler(dp: Dispatcher):
    dp.register_callback_query_handler(delete_product, text = "delete_product")