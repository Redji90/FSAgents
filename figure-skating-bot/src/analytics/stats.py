from typing import List, Dict
import pandas as pd
from ..database.models import Result, Competition, Skater

class StatsCalculator:
    @staticmethod
    def calculate_skater_stats(results: List[Result]) -> Dict:
        """Рассчитывает статистику для конкретного фигуриста"""
        df = pd.DataFrame([
            {
                "competition": r.competition.name,
                "date": r.competition.date,
                "short_program": r.short_program_score,
                "free_program": r.free_program_score,
                "total": r.total_score,
                "rank": r.rank
            }
            for r in results
        ])

        return {
            "competitions_count": len(df),
            "average_total": df["total"].mean(),
            "best_result": {
                "score": df["total"].max(),
                "competition": df.loc[df["total"].idxmax(), "competition"]
            },
            "average_rank": df["rank"].mean(),
            "progress": {
                "short_program": df["short_program"].diff().mean(),
                "free_program": df["free_program"].diff().mean()
            }
        }

    @staticmethod
    def get_season_summary(results: List[Result]) -> Dict:
        """Формирует сводку за сезон"""
        competitions = pd.DataFrame([
            {
                "name": r.competition.name,
                "date": r.competition.date,
                "total_participants": len(r.competition.results)
            }
            for r in results
        ])

        return {
            "total_competitions": len(competitions),
            "participants_average": competitions["total_participants"].mean(),
            "season_timeline": competitions.to_dict(orient="records")
        }