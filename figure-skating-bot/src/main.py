# main.py
import logging
from bot import handlers
from aiogram import Bot, Dispatcher, executor
from config import config

API_TOKEN = config['API_TOKEN']

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Register handlers
handlers.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)