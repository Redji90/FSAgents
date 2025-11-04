# src/bot/handlers.py

from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот для анализа результатов по фигурному катанию.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Используйте /start для начала.')

def analyze_results(update: Update, context: CallbackContext) -> None:
    # Логика для анализа результатов фигурного катания
    update.message.reply_text('Анализ результатов...')

def get_season_stats(update: Update, context: CallbackContext) -> None:
    # Логика для получения статистики за сезон
    update.message.reply_text('Получение статистики за сезон...')

def handle_pdf(update: Update, context: CallbackContext) -> None:
    # Логика для работы с PDF
    update.message.reply_text('Обработка PDF файлов...')

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from .keyboards import get_main_keyboard, get_analytics_keyboard
import logging

logger = logging.getLogger(__name__)
router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать в бот анализа результатов фигурного катания!\n"
        "Используйте меню для навигации.",
        reply_markup=get_main_keyboard()
    )

@router.message(F.text == "Загрузить протокол")
async def handle_upload_request(message: Message):
    await message.answer(
        "Отправьте PDF файл с протоколом соревнований.\n"
        "Поддерживаются официальные протоколы ISU.",
    )

@router.message(F.document)
async def handle_pdf(message: Message):
    if not message.document.mime_type == "application/pdf":
        await message.answer("Пожалуйста, отправьте файл в формате PDF.")
        return

    await message.answer("Обрабатываю протокол...")
    # TODO: Добавить обработку PDF