from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="Загрузить протокол")],
        [KeyboardButton(text="Анализ результатов")],
        [KeyboardButton(text="Статистика")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_analytics_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="По спортсменам", callback_data="analytics_by_skater")],
        [InlineKeyboardButton(text="По соревнованиям", callback_data="analytics_by_competition")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)