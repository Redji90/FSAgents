import PyPDF2
import re
from typing import Dict, List, Optional
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class PDFResultExtractor:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def process_document(self) -> Dict:
        """Основной метод обработки документа"""
        text = self._extract_text()
        competition_info = self._extract_competition_info(text)
        results = self._extract_results(text)
        
        return {
            "competition": competition_info,
            "results": results
        }

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
            'name': r'(?:Competition|Championship):\s*(.+?)(?:\n|$)',
            'date': r'Date:\s*(.+?)(?:\n|$)',
            'location': r'Place:\s*(.+?)(?:\n|$)',
            'category': r'Category:\s*(.+?)(?:\n|$)',
            'discipline': r'Discipline:\s*(.+?)(?:\n|$)'
        }
        
        info = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, text)
            info[key] = match.group(1).strip() if match else None
            
        # Преобразование даты в datetime объект
        if info.get('date'):
            try:
                info['date'] = datetime.strptime(info['date'], '%d.%m.%Y').date()
            except ValueError:
                logger.warning(f"Не удалось разобрать дату: {info['date']}")
                
        return info

    def _extract_results(self, text: str) -> List[Dict]:
        """Извлекает результаты участников"""
        results = []
        
        # Паттерн для поиска результатов
        # Пример строки: 1 ИВАНОВА Анна RUS 82.50 160.25 242.75
        pattern = r'(\d+)\s+([A-ZА-Я]+\s+[A-ZА-Я]+)\s+([A-Z]{3})\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)'
        
        matches = re.finditer(pattern, text)
        for match in matches:
            result = {
                'rank': int(match.group(1)),
                'name': match.group(2),
                'country': match.group(3),
                'short_program': float(match.group(4)),
                'free_program': float(match.group(5)),
                'total': float(match.group(6))
            }
            results.append(result)
            
        return results