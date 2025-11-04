import pytest
from src.pdf.extractor import PDFResultExtractor
from pathlib import Path

@pytest.fixture
def sample_competition_text():
    return """
    Competition: Test Grand Prix 2025
    Date: 04.11.2025
    Place: Moscow, Russia
    Category: Senior
    Discipline: Ladies
    
    Final Results
    1 ИВАНОВА Анна RUS 82.50 160.25 242.75
    2 ПЕТРОВА Мария RUS 80.15 155.30 235.45
    """

def test_extract_competition_info(sample_competition_text):
    extractor = PDFResultExtractor("dummy.pdf")
    info = extractor._extract_competition_info(sample_competition_text)
    
    assert info["name"] == "Test Grand Prix 2025"
    assert info["location"] == "Moscow, Russia"
    assert info["category"] == "Senior"
    assert info["discipline"] == "Ladies"