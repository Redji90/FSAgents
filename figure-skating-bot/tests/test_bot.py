import asyncio
import pytest
from src.pdf.extractor import PDFResultExtractor
from src.llm.client import LLMClient
from src.database.database import init_db
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.mark.asyncio
async def test_pdf_processing():
    # Проверяем обработку PDF
    extractor = PDFResultExtractor("tests/test_data/test_protocol.pdf")
    data = extractor.process_document()
    
    assert data["competition"]["name"] == "Test Grand Prix 2025"
    assert len(data["results"]) == 3
    assert data["results"][0]["name"] == "ИВАНОВА Анна"

@pytest.mark.asyncio
async def test_database():
    # Проверяем работу с базой данных
    await init_db()
    # TODO: добавить тесты для БД

@pytest.mark.asyncio
async def test_llm():
    # Проверяем работу с LLM
    client = LLMClient()
    test_results = [
        {
            "name": "ИВАНОВА Анна",
            "country": "RUS",
            "total_score": 242.75
        }
    ]
    analysis = await client.analyze_competition_results(test_results)
    assert analysis is not None