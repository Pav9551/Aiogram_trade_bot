from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

class Scheduler:
    def __init__(self, bot: Bot, chat_id: int):
        self.bot = bot
        self.chat_id = chat_id
        self.scheduler = AsyncIOScheduler()

    async def send_message(self):
        """
        Функция для отправки сообщения каждый час
        """
        print('Сообщение отправлено')
        await self.bot.send_message(chat_id=self.chat_id, text=f"Сообщение отправлено в {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def start(self):
        """
        Запуск планировщика и добавление задачи отправки сообщений
        """
        self.scheduler.add_job(self.send_message, 'cron', minute='*')
        self.scheduler.start()
