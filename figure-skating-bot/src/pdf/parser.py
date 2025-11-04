# Этот файл отвечает за парсинг извлеченных данных и подготовку их для анализа.

from typing import Dict, List
import re
from dataclasses import dataclass
from datetime import datetime

@dataclass
class CompetitionResult:
    rank: int
    name: str
    country: str
    short_program: float
    free_program: float
    total: float

class ResultParser:
    @staticmethod
    def parse_isu_protocol(text: str) -> List[CompetitionResult]:
        """Парсит протокол формата ISU"""
        results = []
        
        # Разделяем текст на строки и ищем секцию с результатами
        lines = text.split('\n')
        result_section = False
        
        for line in lines:
            if 'Final Results' in line:
                result_section = True
                continue
                
            if result_section and line.strip():
                # Пример строки: 1 ИВАНОВА Анна RUS 82.50 160.25 242.75
                parts = line.split()
                if len(parts) >= 6 and parts[0].isdigit():
                    try:
                        result = CompetitionResult(
                            rank=int(parts[0]),
                            name=f"{parts[1]} {parts[2]}",
                            country=parts[3],
                            short_program=float(parts[4]),
                            free_program=float(parts[5]),
                            total=float(parts[6])
                        )
                        results.append(result)
                    except (ValueError, IndexError):
                        continue
                        
        return results

    @staticmethod
    def format_results(results: List[CompetitionResult]) -> str:
        """Форматирует результаты для вывода"""
        output = "Результаты соревнований:\n\n"
        for r in results:
            output += (f"{r.rank}. {r.name} ({r.country})\n"
                      f"   КП: {r.short_program:.2f} "
                      f"ПП: {r.free_program:.2f} "
                      f"Сумма: {r.total:.2f}\n")
        return output