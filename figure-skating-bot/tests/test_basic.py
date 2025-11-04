import pytest
from pathlib import Path

def test_project_structure():
    """Проверка наличия основных файлов проекта"""
    root = Path(__file__).parent.parent
    required_files = [
        'src/main.py',
        'src/bot/handlers.py',
        'src/bot/keyboards.py',
        'src/analytics/processor.py',
        'src/database/models.py',
        'src/llm/client.py',
        'src/pdf/extractor.py',
    ]
    
    for file_path in required_files:
        full_path = root / file_path
        assert full_path.exists(), f"Файл {file_path} не найден"

def test_environment():
    """Проверка окружения"""
    import sys
    print(f"Python version: {sys.version}")
    print(f"Python path: {sys.executable}")