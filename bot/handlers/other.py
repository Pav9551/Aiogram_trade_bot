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
    lines = []
    for balance in parsed_data['balances']:
        lines.append(f"{balance['asset']}, доступно: {balance['free']}, заблокировано: {balance['locked']}")
    text = "\n".join(lines)
    await bot.send_message(user.id, text)
async def __buy(msg: Message) -> None:
    bot: Bot = msg.bot
    user = msg.from_user

    market = mexc_spot_v3.mexc_market()

    # Enter parameters in JSON format in the "params", for example: {"symbol":"BTCUSDT", "limit":"200"}
    # If there are no parameters, no need to send params
    params = {
        "symbol": "KASUSDT",
    }
    Price = market.get_price(params)
    print(Price)
    trade = mexc_spot_v3.mexc_trade()

    # Enter parameters in JSON format in the "params", for example: {"symbol":"BTCUSDT", "limit":"200"}
    # If there are no parameters, no need to send params

    AccountInfo = trade.get_account_info()
    #print(AccountInfo)
    # Парсим данные в словарь Python
    parsed_data = json.loads(json.dumps(AccountInfo))
    print(Price)
    parsed_data = json.loads(json.dumps(Price))
    current_course_of_KAS = float(parsed_data['price']) # курс KAS
    #current_course_of_KAS = 0.179 # курс KAS в момент покупки
    quan_spent_USDT = 6 #потраченные USDT
    quan_curr_KAS = quan_spent_USDT/current_course_of_KAS
    profit = 0.3
    quan_receive_USDT = quan_spent_USDT + quan_spent_USDT * profit/100

    await bot.send_message(user.id, f"{user.username}, you Price: {current_course_of_KAS:10.6f} ,quan_curr_KAS: {quan_curr_KAS:5.2f}, quan_spent_USDT {quan_spent_USDT:5.6f} ,quan_receive_USDT: {quan_receive_USDT:5.6f}")
def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__get_id, commands=["id"])
    dp.register_message_handler(__start, commands=["start"])
    dp.register_message_handler(__balance, commands=["balance"])
    dp.register_message_handler(__buy, commands=["buy"])
    dp.register_message_handler(other_messages, content_types=['text'], state=None)

