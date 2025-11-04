from typing import List, Dict
import pandas as pd
from ..database.models import Result, Competition, Skater
from ..llm.client import LLMClient
import logging

logger = logging.getLogger(__name__)

class AnalyticsProcessor:
    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client

    async def analyze_competition(self, competition_id: int, results: List[Result]) -> Dict:
        """Анализирует результаты конкретного соревнования"""
        try:
            # Преобразуем результаты в DataFrame для анализа
            df = pd.DataFrame([
                {
                    "name": result.skater.name,
                    "country": result.skater.country,
                    "short_program": result.short_program_score,
                    "free_program": result.free_program_score,
                    "total": result.total_score,
                    "rank": result.rank
                }
                for result in results
            ])

            # Базовая статистика
            stats = {
                "total_participants": len(df),
                "average_score": df["total"].mean(),
                "max_score": df["total"].max(),
                "min_score": df["total"].min(),
                "countries": df["country"].nunique()
            }

            # Получаем анализ от LLM
            llm_analysis = await self.llm_client.analyze_competition_results(
                df.to_dict(orient="records")
            )

            return {
                "statistics": stats,
                "llm_analysis": llm_analysis
            }

        except Exception as e:
            logger.error(f"Ошибка при анализе соревнования: {e}")
            raise