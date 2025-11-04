# main.py
import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher()

async def main():
    # Импорт обработчиков
    from bot.handlers import router
    
    # Регистрация роутера
    dp.include_router(router)
    
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())