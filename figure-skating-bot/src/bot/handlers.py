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
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from ..pdf.extractor import PDFResultExtractor
from ..analytics.processor import analyze_results
from ..llm.client import LLMClient
from ..database.crud import create_competition, get_competitions
from .keyboards import get_main_keyboard, get_analytics_keyboard
import logging

logger = logging.getLogger(__name__)
router = Router()
llm_client = LLMClient()

class AnalyticsStates(StatesGroup):
    waiting_for_competition = State()
    waiting_for_analysis_type = State()

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
    
    try:
        await message.answer("Обрабатываю протокол...")
        
        # Скачивание файла
        file = await message.bot.get_file(message.document.file_id)
        file_path = f"temp/{message.document.file_name}"
        await message.bot.download_file(file.file_path, file_path)
        
        # Обработка PDF
        extractor = PDFResultExtractor(file_path)
        data = extractor.process_document()
        
        # Сохранение в БД
        competition = await create_competition(data["competition"])
        
        # Анализ через LLM
        initial_analysis = await llm_client.analyze_competition_results(data["results"])
        
        await message.answer(
            f"✅ Протокол обработан успешно!\n\n"
            f"Соревнование: {competition.name}\n"
            f"Дата: {competition.date}\n\n"
            f"Краткий анализ:\n{initial_analysis}",
            reply_markup=get_analytics_keyboard()
        )
        
    except Exception as e:
        logger.error(f"Ошибка при обработке PDF: {e}")
        await message.answer("Произошла ошибка при обработке файла. Попробуйте другой файл.")
    finally:
        # Очистка временных файлов
        import os
        if os.path.exists(file_path):
            os.remove(file_path)

@router.callback_query(F.data.startswith("analytics_"))
async def handle_analytics(callback: CallbackQuery, state: FSMContext):
    analysis_type = callback.data.split("_")[1]
    
    try:
        competitions = await get_competitions()
        if not competitions:
            await callback.message.answer("Нет доступных соревнований для анализа.")
            return
            
        await state.set_state(AnalyticsStates.waiting_for_competition)
        await state.update_data(analysis_type=analysis_type)
        
        competitions_text = "\n".join(
            f"{i}. {comp.name} ({comp.date})"
            for i, comp in enumerate(competitions, 1)
        )
        
        await callback.message.answer(
            f"Выберите соревнование (введите номер):\n\n{competitions_text}"
        )
        
    except Exception as e:
        logger.error(f"Ошибка при получении списка соревнований: {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")