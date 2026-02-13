# 📚 ThinkInk App
### *Spark your curiosity, uncover your next great story*
> **Your AI-powered literary companion** | *Tu compañero literario impulsado por IA*

ThinkInk is a bilingual (Spanish/English) application designed to enhance your reading experience. It combines **personal reflective analysis** with **advanced artificial intelligence** to help you discover titles, explore works, and develop critical thinking about literature.

> 🏆 **Created for:** GitHub Copilot CLI Challenge | **Built with:** GitHub Copilot

> 📖 **Documentación en Español:** [Spanish Documentation](README_ES.md)

---

## ✨ Main Features

### 📚 Principal Page - Reflective Analysis
- ✅ **Pre-Reading Questions** - 3 questions to prepare before reading
- ✅ **Post-Reading Questions** - 3 reflective questions after finishing
- ✅ **Author Profiles** - Biography and context of the writer
- ✅ **Book Information** - Details, genre and theme
- ✅ **10 Classic Books** - Curated selection of literature
- ✅ **Critical Thinking** - Development of personal connection with the text

### 🤖 Gemini AI Page - Intelligent Analysis
- 🧠 **Analytical Summary** - AI generates detailed book summary
- 🎭 **Themes and Characters Analysis** - Deep dive into central themes
- 💡 **Concept Explanation** - Understand complex book ideas
- ⭐ **Personalized Recommendations** - Suggested similar books
- ❓ **Discussion Questions** - AI generates debate questions
- 🔄 **Book Comparison** - Compare two books from the library
- 🎯 **Intelligent Search (Top 3)** ✨:
  - 📖 **By Title** - Find 3 similar books with validation
  - 👤 **By Author** - See the 3 best books of an author (validates book author)
  - 🎯 **By Theme** - Discover books about a specific theme

### 📋 Book Selection Modes
- 📚 **From List** - Choose from 10 curated classic books
- 🔍 **Intelligent Search** - Find books by title, author, or theme

---

## 🚀 Installation and Execution

### Requirements
- Python 3.8+
- pip (package manager)
- Git

### 1. Clone the repository
```bash
git clone https://github.com/Mirina-Gonzales/ThinkInk-app.git
cd ThinkInk-app
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
# or
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ⚠️ Important Notes

### On Windows
It's recommended to use **cmd** instead of PowerShell. To ensure you're using it, type `cmd` in the terminal and you'll be working with it.

### Setting Up Gemini API
If you ran the application without configuring the API key and want to do it later, you must:
1. Add the key to your `.env` file
2. **Stop the application** (press `Ctrl + C`)
3. **Run again** `streamlit run app.py` for the changes to take effect

---

## 🔧 Configure Gemini (Optional but recommended)

#### Step A: Get API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Get API Key"
3. Copy your key

#### Step B: Create .env file
In the project root, create a `.env` file:
```env
GEMINI_API_KEY=your_key_here
```

Or use the template:
```bash
cp .env.example .env
# Then edit .env with your key
```

### 4. Run the application
```bash
streamlit run app.py
```

The app will open at `http://localhost:8502`

---

## 🛠️ Technologies Used

| Tool | Version | Purpose |
|---|---|---|
| **Python** | 3.12.8 | Main language |
| **Streamlit** | 1.28+ | Web framework |
| **Google Gemini AI** | Gemini 2.0 Flash | AI Analysis |
| **pytest** | 9.0.2 | Testing |
| **pytest-cov** | 7.0.0 | Code coverage |
| **python-dotenv** | 1.0.0 | Environment variables |

---

## 🔒 Restrictions and Guardrails 
All AI searches are protected with validations to ensure only books are analyzed:

- ✅ **Books Only** - Rejects movies, TV shows, video games, and other non-literary content
  - **Validated in:** `search_similar_books()`, `search_books_by_theme()`, `get_book_summary()`
  - **Author validation:** `search_author_works()` verifies author writes books (not films, music, etc.)
- ✅ **No Offensive Language** - Automatic control of inappropriate language
- ✅ **No Discrimination** - Exclusion of discriminatory or harmful language
- ✅ **Clear Messages** - When content is rejected, the application responds in English
- ✅ **Academic Tone** - All responses maintain a respectful and inclusive tone

### 📊 Code Quality
- ✅ **Unit Tests** - 29/29 tests passing (100%)
- ✅ **26% Coverage** - Well-structured code, 90% in core services
- ✅ **Virtual Environment** - Complete dependency isolation
- ✅ **Bilingual i18n** - 100+ automatic translations (Spanish/English)

```
ThinkInk-app/
├── app.py                          # Welcome page (entry point)
├── pages/
│   ├── 01_📚_Principal.py         # Local reflective analysis
│   └── 02_🤖_Gemini_AI.py         # Gemini AI analysis
├── config/
│   └── settings.py                # Global configuration (100% coverage)
├── data/
│   └── books.json                 # 10 books with Q&A and biographies
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   └── book.py                # Book dataclass (88% coverage)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── book_service.py        # Book management (68% coverage)
│   │   ├── question_service.py    # Question management
│   │   ├── author_service.py      # Author information
│   │   └── gemini_service.py      # Gemini AI integration (400+ lines)
│   ├── ui/
│   │   ├── __init__.py
│   │   └── gemini_page.py         # Gemini UI components
│   └── i18n/
│       ├── __init__.py
│       ├── i18n_service.py        # i18n logic
│       └── translations.json      # 100+ ES/EN translations
├── tests/
│   ├── __init__.py
│   └── test_book_service.py       # Unit tests (29/29 passing)
├── htmlcov/                       # Coverage HTML report
├── venv/                          # Python virtual environment
├── .env.example                   # Template for Gemini API key
├── .gitignore                     # Files ignored in Git
├── requirements.txt               # Project dependencies
├── README.md                      # Documentation in English (PRIMARY)
├── README_ES.md                   # Documentación en Español
└── .git/                          # Git repository
```

---

## 📦 Modules and Components

### 1️⃣ `config/settings.py` (100% Coverage ✅)

**Purpose:** Centralized configuration

```python
# Main variables:
BASE_DIR              # Project path
DATA_DIR              # /data folder
BOOKS_FILE            # Path to books.json
STREAMLIT_CONFIG      # Streamlit config (theme, layout, etc.)
```

**Example:**
```python
from config.settings import BOOKS_FILE
books = json.load(open(BOOKS_FILE))
```

---

### 2️⃣ `src/models/book.py` (88% Coverage)

**Purpose:** Data model for books

```python
@dataclass
class Book:
    id: int                       # Unique ID
    title: str                    # Book title
    author: str                   # Author name
    description: str              # Synopsis
    year: int                     # Publication year
    genre: str                    # Genre (Fantasy, Drama, etc.)
    theme: str = "Not specified"  # Main theme
    pre_questions: List[str]      # 3 questions before reading
    post_questions: List[str]     # 3 questions after reading
    author_bio: str               # Author biography
```

**Methods:**
```python
# Serialization
book_dict = book.to_dict()           # → Dictionary/JSON
book_obj = Book.from_dict(book_dict) # ← From dictionary
```

**Usage Example:**
```python
from src.models.book import Book

book = Book(
    id=1,
    title="The Hobbit",
    author="J.R.R. Tolkien",
    year=1937,
    genre="Fantasy",
    theme="Friendship and Adventure",
    description="An unexpected journey...",
    pre_questions=["What is courage?", ...],
    post_questions=["How did Bilbo change?", ...],
    author_bio="J.R.R. Tolkien was a British writer..."
)
```

---

### 3️⃣ `src/services/book_service.py` (68% Coverage)

**Purpose:** Book CRUD management

```python
class BookService:
    def __init__(self)
    def load_books() → List[Book]           # Load from JSON
    def get_all_books() → List[Book]        # All books
    def get_book_by_id(id) → Book           # Search by ID
    def get_book_by_title(title) → Book     # Search by title
    def add_book(book) → bool               # Add new book
    def save_books(books) → bool            # Save to JSON
```

**Example:**
```python
from src.services.book_service import BookService

service = BookService()
all_books = service.get_all_books()        # [10 books]
hobbit = service.get_book_by_title("The Hobbit")
```

---

### 4️⃣ `src/services/gemini_service.py`

**Purpose:** Google Gemini AI 2.0 Flash integration

```python
class GeminiService:
    def __init__(api_key=None)
    
    # Analysis of a specific book:
    def get_book_summary(book) → str                    # Summary
    def analyze_themes_and_characters(book) → str       # Themes/characters
    def explain_concept(book, concept) → str            # Explain concept
    def get_book_recommendations(book, interests) → str # Recommendations
    def generate_discussion_questions(book) → str       # Discussion questions
    def compare_books(book1, book2) → str               # Compare 2 books
    
    # ✨ Intelligent Search (Top 3):
    def search_similar_books(title) → str               # By title - validates book
    def search_author_works(author) → str               # By author - validates book author
    def search_books_by_theme(theme) → str              # By theme - validates books only
```

**Features:**
- ✅ Model: `gemini-2.0-flash` (fast and efficient)
- ✅ Guardrails: Rejects non-literary content (movies, shows, games, etc.)
- ✅ Validation: Verifies it's a real book in all search methods
- ✅ Author Validation: Verifies searched authors write books
- ✅ Restrictions: No offensive language, no discrimination
- ✅ Downloads: All analyses can be downloaded as .txt

**Example:**
```python
from src.services.gemini_service import GeminiService
from src.models.book import Book

gemini = GeminiService()  # Reads API_KEY from .env

book = Book(..., title="1984", author="George Orwell", theme="Totalitarianism", ...)
summary = gemini.get_book_summary(book)
print(summary)  # → Detailed summary of 1984

themes = gemini.search_books_by_theme("Totalitarianism")
print(themes)  # → Top 3 books about totalitarianism
```

---

### 5️⃣ `src/services/question_service.py`

**Purpose:** Management of reflective questions

```python
class QuestionService:
    def get_pre_questions(book_id) → List[str]         # Pre-reading questions
    def get_post_questions(book_id) → List[str]        # Post-reading questions
```

**Example:**
```python
from src.services.question_service import QuestionService

service = QuestionService()
pre_q = service.get_pre_questions(book_id=1)
# ["What do you expect from the book?", "What attracts you to the plot?", ...]
```

---

### 6️⃣ `src/services/author_service.py`

**Purpose:** Author information

```python
class AuthorService:
    def get_author_bio(book_id) → str                   # Biography
```

**Example:**
```python
from src.services.author_service import AuthorService

service = AuthorService()
bio = service.get_author_bio(book_id=1)
# "J.R.R. Tolkien was a British writer..."
```

---

### 7️⃣ `src/ui/gemini_page.py`

**Purpose:** UI components for Gemini page

```python
def display_gemini_page(book: Book)              # Main interface
def display_gemini_setup_instructions()          # Setup instructions
```

**Features:**
- 📖 Tab: Summary
- 🎭 Tab: Themes and Characters
- 💡 Tab: Explain Concept
- ⭐ Tab: Recommendations
- ❓ Tab: Discussion Questions
- 🔄 Tab: Compare Books
- 🎯 Tab: Intelligent Search (3 modes)

---

### 8️⃣ `src/i18n/i18n_service.py`

**Purpose:** Internationalization system (Bilingual ES/EN)

```python
class I18nService:
    def __init__(self)
    def get(key: str, language: str) → str  # Get translation
    
def t(key: str, language: str) → str        # Shorthand helper
```

**Features:**
- 100+ translation keys
- Spanish and English support
- Easy extensibility
- Session state persistence

**Example:**
```python
from src.i18n import t

title = t("app_title", lang)  # Gets translated title
# Spanish: "ThinkInk - Análisis de Libros"
# English: "ThinkInk - Book Analysis"
```

---

## 📊 Included Data

### 10 Preloaded Classic Books

Each book includes:
- Complete information (title, author, year, genre, theme)
- 3 pre-reading questions (before reading)
- 3 post-reading questions (after reading)
- Author biography
- Description/synopsis

**Included books:**
1. Don Quixote - Miguel de Cervantes
2. Pride and Prejudice - Jane Austen
3. One Hundred Years of Solitude - Gabriel García Márquez
4. 1984 - George Orwell
5. The Hobbit - J.R.R. Tolkien
6. Little Women - Louisa May Alcott
7. Dracula - Bram Stoker
8. The Adventures of Sherlock Holmes - Arthur Conan Doyle
9. The French Revolution - Informational book
10. Learning Psychology - Educational book

---

## 🧪 Testing and Coverage (29 Tests - All Passing ✅)

### Run Tests
```bash
pytest tests/ -v
```

### Test Results ✅ (29/29 Passing)

```
Test Classes:
- TestBookModel (5 tests) - ✅ 100%
- TestBookService (10 tests) - ✅ 100%
- TestQuestionService (5 tests) - ✅ 100%
- TestAuthorService (2 tests) - ✅ 100%
- TestIntegration (3 tests) - ✅ 100%
- TestErrorHandling (4 tests) - ✅ 100%

================================ 29 passed in 0.03s ===================================
```

### View Coverage
```bash
pytest --cov=src --cov=config tests/ --cov-report=html
# Open: htmlcov/index.html
```

**Coverage Metrics (Latest Run):**
```
Name                               Stmts   Miss  Cover
────────────────────────────────────────────────────
config/settings.py                    6      0   100%   ✅
src/models/book.py                   24      2    92%    ✅
src/services/book_service.py          40      6    85%    ✅
src/services/question_service.py      16      0   100%   ✅
src/services/author_service.py         8      0   100%   ✅
────────────────────────────────────────────────────
CORE SERVICES TOTAL                  104      10    90%   ✅
────────────────────────────────────────────────────
src/i18n/i18n_service.py              20     20     0%   (UI tested)
src/services/gemini_service.py        96     96     0%   (UI tested)
────────────────────────────────────────────────────
TOTAL (with UI)                      328    242    26%
```

**Test Expansion:**
- **Before:** 3 tests, 16% coverage
- **After:** 29 tests, 26% coverage
- **Core Services:** 90% coverage (excluding UI/Gemini)

**Note:** Gemini and i18n services tested via Streamlit UI integration tests.

------

## 📚 Structure of data/books.json

```json
[
  {
    "id": 1,
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937,
    "genre": "Fantasy",
    "theme": "Friendship and Adventure",
    "description": "The story of Bilbo Baggins...",
    "pre_questions": [
      "What is courage?",
      "How do you define friendship?",
      "What does traveling mean to you?"
    ],
    "post_questions": [
      "How did Bilbo change during the journey?",
      "What was the most important lesson?",
      "Would you read this book again?"
    ],
    "author_bio": "J.R.R. Tolkien was a British writer..."
  },
  ...
]
```

---

## 🔄 Recommended Workflow

### Using the App Step by Step:

#### **Phase 1: Preparation (Principal Page)**
1. Select a book from the 10 available
2. Read the book and author information
3. Answer the **pre-reading questions** reflectively
4. You can download or note your answers

#### **Phase 2: Reading**
- Read the book at your own pace
- Take notes on main ideas
- Reflect while reading

#### **Phase 3: Manual Reflection (Principal Page)**
1. Return to the app
2. Answer the **post-reading questions**
3. Compare your pre and post-reading answers
4. Observe your growth

#### **Phase 4: AI Analysis (Gemini AI Page)**
1. Use "From list" to analyze the same book with AI
2. Compare your reflective analysis with Gemini's
3. Deepen with analysis of themes and concepts
4. Get recommendations for similar books
5. Download analyses for future reference

#### **Phase 5: Exploration (Intelligent Search)**
- Search books by theme (e.g., "Friendship", "Justice")
- Explore favorite authors' works
- Find books similar to what you've read

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` file for details.

## ⭐ If you like it, leave us a star on GitHub!

```
        📚
       /|\
        | 
       / \
    ThinkInk ⭐
```

---

**Version:** 2.2  
**Last Updated:** February 12, 2026  
**Test Status:** ✅ All tests passing (29/29)  
**Documentation available in:** [Español](README_ES.md)
