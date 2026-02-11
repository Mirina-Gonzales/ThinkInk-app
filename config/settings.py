import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
BOOKS_FILE = DATA_DIR / "books.json"

STREAMLIT_CONFIG = {
    "page_title": "📚 ThinkInk App",
    "page_icon": "📖",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
}
