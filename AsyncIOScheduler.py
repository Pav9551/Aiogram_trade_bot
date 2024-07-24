import logging
from aiogram import Bot, Dispatcher, executor, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'  # Замените на ваш реальный токен

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание экземпляров бота и диспетчера
bot = Bot(token='1937872018:AAFFfPbY_DcKp1080IE2i0tRgpUnYvWZYlc')
dp = Dispatcher(bot)

# Инициализация планировщика
scheduler = AsyncIOScheduler()

# ID чата для отправки сообщений (используйте get_chat_id для получения ID)
CHAT_ID = '808941537'  # Замените на ваш ID чата

async def send_message():
    """
    Функция для отправки сообщения каждый час
    """
    print('Сообщение отправлено')
    await bot.send_message(chat_id=CHAT_ID, text=f"Сообщение отправлено в {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Планирование отправки сообщений каждый час
scheduler.add_job(send_message, 'cron', minute='*')

# Команда start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Этот бот будет отправлять сообщение каждый час.")

if __name__ == '__main__':
    # Запуск планировщика
    scheduler.start()
    # Запуск поллинга
    executor.start_polling(dp, skip_updates=True)


### Шаг 4: Получите ID чата (опционально)

###Если вы хотите определить ID индивидуального чата, добавьте временную команду для получения этого ID:

'''python
# Команда для получения chat_id
@dp.message_handler(commands=['get_chat_id'])
async def get_chat_id(message: types.Message):
    await message.reply(f"Your chat ID is: {message.chat.id}")
'''
