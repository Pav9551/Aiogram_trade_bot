from aiogram import Dispatcher, Bot
from aiogram.types import Message

from python.spot import mexc_spot_v3
import json


async def other_messages(msg: Message) -> None:
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Я вас не понял, напишите /start!")


async def __get_id(msg: Message) -> None:
    bot: Bot = msg.bot
    user = msg.from_user
    await bot.send_message(user.id, f"{user.username}: {user.id}")
async def __start(msg: Message) -> None:
    bot: Bot = msg.bot
    user = msg.from_user
    await bot.send_message(user.id, f"{user.username}: {'Это команда старт'}")
async def __balance(msg: Message) -> None:
    bot: Bot = msg.bot
    user = msg.from_user
    trade = mexc_spot_v3.mexc_trade()

    # Enter parameters in JSON format in the "params", for example: {"symbol":"BTCUSDT", "limit":"200"}
    # If there are no parameters, no need to send params

    AccountInfo = trade.get_account_info()
    #print(AccountInfo)
    # Парсим данные в словарь Python
    parsed_data = json.loads(json.dumps(AccountInfo))
    await bot.send_message(user.id, f"{user.username}, you balance: {parsed_data['balances'][0]['free']} {parsed_data['balances'][0]['asset']}")

def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__get_id, commands=["id"])
    dp.register_message_handler(__start, commands=["start"])
    dp.register_message_handler(__balance, commands=["balance"])
    dp.register_message_handler(other_messages, content_types=['text'], state=None)

