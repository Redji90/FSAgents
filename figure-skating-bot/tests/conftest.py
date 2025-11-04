import pytest
import sys
from pathlib import Path

# Добавляем корневую директорию проекта в PYTHONPATH
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))