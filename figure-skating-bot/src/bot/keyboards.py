from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def get_main_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Загрузить протокол")],
        [
            KeyboardButton(text="Анализ соревнований"),
            KeyboardButton(text="Статистика")
        ],
        [KeyboardButton(text="Помощь")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_analytics_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                text="Детальный анализ",
                callback_data="analytics_detailed"
            )
        ],
        [
            InlineKeyboardButton(
                text="Сравнение с прошлыми",
                callback_data="analytics_compare"
            )
        ],
        [
            InlineKeyboardButton(
                text="Статистика выступлений",
                callback_data="analytics_stats"
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)