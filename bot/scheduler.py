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
        message_text = (
               "Привет! 🌟 Знаешь, что делает нас счастливее и продуктивнее? Жизнь в чистой и уютной квартире! 🌿✨\n\n"
               "Сегодня самое время навести порядок, потому что:\n"
               "- Уборка освобождает пространство не только вокруг, но и в твоей голове. 🧘‍♂️\n"
               "- Чистая квартира помогает лучше концентрироваться и отдыхать. 🌸\n"
               "- Уборка — это отличная физическая нагрузка. 💪\n\n"
               "Представь себе, как приятно будет заварить чашку любимого чая в чистой кухне или отдохнуть на свежем диване. ☕️ "
               "Жизнь станет гораздо приятнее, и ты почувствуешь прилив новых сил!\n\n"
               "Давай, начни прямо сейчас! Включи любимую музыку, возьми губку в руки и преврати уборку в весёлый процесс! 🎶🧽 "
               "Ты справишься, и результат приятно удивит! 😊\n\n"
               "Удачи тебе, и пусть твой дом сияет чистотой! 🌟"
           )
        await self.bot.send_message(chat_id=self.chat_id, text=f"Сообщение отправлено в {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        await self.bot.send_message(chat_id=self.chat_id, text=message_text)
    def start(self):
        """
        Запуск планировщика и добавление задачи отправки сообщений
        """
        self.scheduler.add_job(self.send_message, 'cron', minute='*')
        self.scheduler.start()
