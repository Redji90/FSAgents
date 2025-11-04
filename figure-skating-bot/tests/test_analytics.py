import pytest
from src.analytics.processor import AnalyticsProcessor
from src.llm.client import LLMClient

@pytest.fixture
def sample_results():
    return [
        {
            "name": "ИВАНОВА Анна",
            "country": "RUS",
            "short_program": 82.50,
            "free_program": 160.25,
            "total": 242.75,
            "rank": 1
        },
        {
            "name": "ПЕТРОВА Мария",
            "country": "RUS",
            "short_program": 80.15,
            "free_program": 155.30,
            "total": 235.45,
            "rank": 2
        }
    ]

@pytest.mark.asyncio
async def test_analytics_processor(sample_results):
    processor = AnalyticsProcessor(LLMClient())
    stats = processor.calculate_basic_stats(sample_results)
    
    assert stats["total_participants"] == 2
    assert stats["average_score"] > 235
    assert stats["max_score"] == 242.75