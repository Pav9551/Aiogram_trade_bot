from aiogram import Dispatcher, Bot
from aiogram.types import Message

from python.spot import mexc_spot_v3
import json

from bot.keyboards import get_admin_keyboard,  get_feedback_keyboard, get_mexc_keyboard
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from bot.misc import TgKeys

from mexc_api.mexcClass import mexc_trade



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
    await bot.send_message(user.id, 'Ваш ответ ...', reply_markup=get_mexc_keyboard(user.id))
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
id_for_answer = TgKeys.ID_FOR_ANSWER
async def __admin_exit(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы вышли из панели администратора ⚠️",
                           reply_markup=get_admin_keyboard(user_id))
async def __rate_clarity_full(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Ясность полная",
                           reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer,"Ясность полная")

async def __rate_almost_perfect(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Почти идеально", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer,"Почти идеально")

async def __rate_good_but_some_nuances(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Хорошо, но есть нюансы", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer,"Хорошо, но есть нюансы")

async def __rate_clear_but_dry(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Понятно, но суховато", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer,"Понятно, но суховато")

async def __rate_average(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Средненько", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer,"Средненько")

async def __rate_somewhat_unclear(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Местами непонятно", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer,"Местами непонятно")

async def __rate_difficult(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Сложновато", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer,"Сложновато")

async def __rate_confusing(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Запутанно", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer, "Запутанно")

async def __rate_very_difficult(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Очень сложно", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer, "Очень сложно")

async def __rate_nonsense(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    await bot.send_message(user_id, "Вы: Ты втираешь мне какую-то дичь", reply_markup=get_feedback_keyboard(user_id))
    await bot.send_message(id_for_answer, "Ты втираешь мне какую-то дичь")
def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__get_id, commands=["id"])
    dp.register_message_handler(__start, commands=["start"])
    dp.register_message_handler(__balance, commands=["balance"])
    dp.register_message_handler(__buy, commands=["buy"])
    dp.register_message_handler(other_messages, content_types=['text'], state=None)
def register_keyboards_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(__admin_exit, lambda c: c.data == "admin_exit")
    dp.register_callback_query_handler(__rate_clarity_full, lambda c: c.data == "rate_clarity_full")
    dp.register_callback_query_handler(__rate_almost_perfect, lambda c: c.data == "rate_almost_perfect")
    dp.register_callback_query_handler(__rate_good_but_some_nuances, lambda c: c.data == "rate_good_but_some_nuances")
    dp.register_callback_query_handler(__rate_clear_but_dry, lambda c: c.data == "rate_clear_but_dry")
    dp.register_callback_query_handler(__rate_average, lambda c: c.data == "rate_average")
    dp.register_callback_query_handler(__rate_somewhat_unclear, lambda c: c.data == "rate_somewhat_unclear")
    dp.register_callback_query_handler(__rate_difficult, lambda c: c.data == "rate_difficult")
    dp.register_callback_query_handler(__rate_confusing, lambda c: c.data == "rate_confusing")
    dp.register_callback_query_handler(__rate_very_difficult, lambda c: c.data == "rate_very_difficult")
    dp.register_callback_query_handler(__rate_nonsense, lambda c: c.data == "rate_nonsense")
async def __mexc_BUY(msg: CallbackQuery, state: FSMContext):
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await state.finish()
    query_parameters = {
            'price': 0.1,
            'quantity': 10,
            'side': 'BUY',
            'symbol': 'KASUSDT',
            'type': 'LIMIT'
        }
    mexc = mexc_trade()
    mexc.post_order(query_parameters)
    await bot.send_message(user_id, "Вы: mexc_BUY", reply_markup=get_mexc_keyboard(user_id))
    await bot.send_message(id_for_answer,"Отправлено сообщение на установку ордера BUYLIMIT")
def register_keyboards_handlers_mexc(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(__mexc_BUY, lambda c: c.data == "mexc_BUY")




