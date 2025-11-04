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
from ..analytics.processor import analyze_results
from ..pdf.extractor import PDFResultExtractor
from ..database.crud import create_competition, get_competitions

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать! Я помогу проанализировать результаты соревнований по фигурному катанию.",
        reply_markup=get_main_keyboard()
    )

@router.message(F.text == "Загрузить протокол")
async def handle_upload_request(message: Message):
    await message.answer(
        "Пожалуйста, отправьте PDF файл с протоколом соревнований."
    )

@router.message(F.document)
async def handle_pdf(message: Message):
    if not message.document.mime_type == "application/pdf":
        await message.answer("Пожалуйста, отправьте файл в формате PDF.")
        return
    
    try:
        # Скачивание и обработка PDF
        file = await message.bot.get_file(message.document.file_id)
        file_path = f"temp/{message.document.file_name}"
        await message.bot.download_file(file.file_path, file_path)
        
        extractor = PDFResultExtractor(file_path)
        competition_data = extractor.process_document()
        
        # Сохранение в базу данных
        db_competition = await create_competition(competition_data)
        
        await message.answer(
            f"Протокол обработан успешно!\n"
            f"Соревнование: {db_competition.name}\n"
            f"Дата: {db_competition.date}"
        )
    except Exception as e:
        await message.answer(f"Произошла ошибка при обработке файла: {str(e)}")