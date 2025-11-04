# main.py
import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from bot.handlers import router
from database.database import init_db

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Загрузка переменных окружения
load_dotenv()

# Инициализация бота
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher()

async def main():
    # Инициализация базы данных
    await init_db()
    
    # Регистрация роутеров
    dp.include_router(router)
    
    # Запуск бота
    logger.info("Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())