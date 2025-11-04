import PyPDF2
import re
from typing import Dict, List
import logging
from datetime import datetime
import os

logger = logging.getLogger(__name__)

class PDFResultExtractor:
    def __init__(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        self.file_path = file_path

    def process_document(self) -> Dict:
        """Основной метод обработки документа"""
        try:
            text = self._extract_text()
            competition_info = self._extract_competition_info(text)
            results = self._extract_results(text)
            
            return {
                "competition": competition_info,
                "results": results
            }
        except Exception as e:
            logger.error(f"Ошибка при обработке документа: {e}")
            raise

    def _extract_text(self) -> str:
        """Извлекает текст из PDF файла"""
        try:
            with open(self.file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                return text
        except Exception as e:
            logger.error(f"Ошибка при чтении PDF: {e}")
            raise

    def _extract_competition_info(self, text: str) -> Dict:
        """Извлекает информацию о соревновании"""
        patterns = {
            'name': r'Competition:\s*(.+?)(?:\n|$)',
            'date': r'Date:\s*(.+?)(?:\n|$)',
            'location': r'Place:\s*(.+?)(?:\n|$)',
            'category': r'Category:\s*(.+?)(?:\n|$)',
            'discipline': r'Discipline:\s*(.+?)(?:\n|$)'
        }
        
        info = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, text)
            info[key] = match.group(1).strip() if match else None
            
        return info