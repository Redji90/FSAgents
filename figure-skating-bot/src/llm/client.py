import os
import requests
from typing import Dict, List
import logging
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv()

class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("LLM_API_KEY")
        self.api_url = os.getenv("LLM_API_URL")
        
        if not self.api_key or not self.api_url:
            raise ValueError("Не установлены LLM_API_KEY или LLM_API_URL")

    async def analyze_competition_results(self, results: List[Dict]) -> str:
        """Анализирует результаты соревнований"""
        try:
            prompt = self._create_analysis_prompt(results)
            
            response = requests.post(
                self.api_url,
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={
                    "prompt": prompt,
                    "max_tokens": 500,
                    "temperature": 0.7
                }
            )
            
            response.raise_for_status()
            return response.json()["choices"][0]["text"]
            
        except Exception as e:
            logger.error(f"Ошибка при анализе результатов: {e}")
            raise

    def _create_analysis_prompt(self, results: List[Dict]) -> str:
        """Создает промпт для анализа результатов"""
        return f"""Проанализируй следующие результаты соревнований по фигурному катанию:
        
{self._format_results_for_prompt(results)}

Предоставь:
1. Общий анализ выступлений
2. Выдающиеся результаты
3. Статистические наблюдения
4. Рекомендации по улучшению"""

    def _format_results_for_prompt(self, results: List[Dict]) -> str:
        return "\n".join([
            f"Спортсмен: {r['name']}, Страна: {r['country']}, "
            f"Общий балл: {r['total_score']}, Место: {r['rank']}"
            for r in results
        ])