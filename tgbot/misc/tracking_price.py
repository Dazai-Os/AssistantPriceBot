import asyncio
from AssistantPriceBot import db, bot
from .parser import citilink


async def sleep_for_check_price():
    await asyncio.sleep(3600)

async def check_price(loop):
    while True:
        data = await db.get_url_price()
        for i in data:
            name_product, now_price = await citilink(i[1])
            if now_price > i[3]:
               await bot.send_message(int(i[0]), f'Цена на товар {name_product} снизилась!')
               await bot.send_message(int(i[0]), str(i[3]))
        await sleep_for_check_price()
