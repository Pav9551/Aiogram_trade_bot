from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.filters import register_all_filters
from bot.misc import TgKeys
from bot.handlers import register_all_handlers
from bot.database.models import register_models

from bot.scheduler import Scheduler
from aiogram import Bot, Dispatcher, executor

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
CHAT_ID = TgKeys.CHAT_ID

async def __on_start_up(dp: Dispatcher) -> None:
    register_all_filters(dp)
    register_all_handlers(dp)
    register_models()
    scheduler_ = Scheduler(bot, CHAT_ID)
    scheduler_.start()
def start_bot():
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)








