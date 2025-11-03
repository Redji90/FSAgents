from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создание кнопок для клавиатуры
button_start = KeyboardButton("Начать")
button_results = KeyboardButton("Результаты")
button_analytics = KeyboardButton("Аналитика")
button_help = KeyboardButton("Помощь")

# Создание основной клавиатуры
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(button_start, button_results, button_analytics, button_help)