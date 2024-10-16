from aiogram import Dispatcher

from bot.handlers.admin import register_admin_handlers
from bot.handlers.other import register_other_handlers
from bot.handlers.user import register_user_handlers
from bot.handlers.other import register_keyboards_handlers
from bot.handlers.other import register_keyboards_handlers_mexc

def register_all_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_user_handlers,
        register_admin_handlers,
        register_other_handlers,
        register_keyboards_handlers,
        register_keyboards_handlers_mexc,
    )
    for handler in handlers:
        handler(dp)


