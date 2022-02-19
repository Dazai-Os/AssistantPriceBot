import asyncio

from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware, BaseMiddleware
from aiogram import Dispatcher, executor, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.utils.exceptions import Throttled

class AntiFlood(BaseMiddleware):
    def __init__(self, limit = 5, key_prefix='antiflood_'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(AntiFlood, self).__init__()
    
    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()

        if handler:
            limit = getattr(handler, 'throttling_rate_limit', self.rate_limit)
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"

        try:
            await dispatcher.throttle(key, rate=limit)
        except Throttled as t:
            await self.message_throttled(message, t)

            raise CancelHandler()
        
    async def message_throttled(self, message, throttled):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if handler:
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")
        else:
            key = f"{self.prefix}_message"
        
        delta = throttled.rate - throttled.delta

        if throttled.exceeded_count <= 2:
            await message.reply('Слишком много Запросов! Ждите 5 секунд.')
        
        thr = await dispatcher.check_key(key)

        if thr.exceeded_count == throttled.exceeded_count and throttled.exceeded_count > 3:
            await message.reply('Вы пока не можете отправлять сообщения подождите 5 секунд!')
        await asyncio.sleep(delta)
