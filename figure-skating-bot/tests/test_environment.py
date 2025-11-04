import sys
import pytest

def test_python_version():
    """Проверка версии Python"""
    version = sys.version_info
    print(f"Python версия: {version.major}.{version.minor}.{version.micro}")
    assert version.major == 3

def test_pytest_working():
    """Проверка работы pytest"""
    assert True