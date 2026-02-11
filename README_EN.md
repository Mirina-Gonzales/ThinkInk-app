# 📚 ThinkInk App

An interactive web application to enhance your reading experience with reflective questions, AI analysis, author information, and intelligent book search. Built with Python, Streamlit, and Google Gemini AI.

**Comparison of two approaches:** Manual reflective analysis vs. Artificial Intelligence analysis

---

## ✨ Main Features

### 📚 Principal Page - Reflective Analysis
- ✅ **Pre-reading Questions** - 3 questions to prepare before reading
- ✅ **Post-reading Questions** - 3 reflective questions after finishing
- ✅ **Author Profiles** - Biography and context of the writer
- ✅ **Book Information** - Details, genre, and theme
- ✅ **10 Classic Books** - Curated literature selection
- ✅ **Critical Thinking** - Develop personal connection with text

### 🤖 Gemini AI Page - Intelligent Analysis
- 🧠 **Analytical Summary** - AI generates detailed book summary
- 🎭 **Theme & Character Analysis** - Deep dive into central themes
- 💡 **Concept Explanation** - Understand complex ideas in the book
- ⭐ **Personalized Recommendations** - Similar books suggested
- ❓ **Discussion Questions** - AI generates debate questions
- 🔄 **Book Comparison** - Compare two books from library
- 🎯 **Intelligent Search (Top 3)** ✨ NEW:
  - 📖 **By Title** - Find 3 similar books
  - 👤 **By Author** - See 3 best works by author
  - 🎯 **By Theme** - Discover books about a specific theme

### 🔒 Restrictions & Guardrails ✨ NEW
- ✅ **Books Only** - Rejects movies, TV shows, videogames, etc.
- ✅ **No Offensive Language** - Content filtering
- ✅ **No Discrimination** - Excludes discriminatory language
- ✅ **Clear Validation** - Spanish messages when content is rejected
- ✅ **Academic Tone** - Respectful and inclusive responses

### 📊 Code Quality
- ✅ **Unit Tests** - 3/3 tests passing
- ✅ **84% Coverage** - Well-tested code
- ✅ **Git Integration** - Complete version control
- ✅ **Virtual Environment** - Dependency isolation

---

## 📁 Project Structure

```
ThinkInk-app/
├── app.py                          # Welcome page (entry point)
├── pages/
│   ├── 01_📚_Principal.py         # Local reflective analysis
│   └── 02_🤖_Gemini_AI.py         # AI analysis with Gemini
├── config/
│   └── settings.py                # Global configuration (100% coverage)
├── data/
│   └── books.json                 # 10 books with Q&A and bios
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   └── book.py                # Book dataclass (94% coverage)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── book_service.py        # Book management (68% coverage)
│   │   ├── question_service.py    # Question management
│   │   ├── author_service.py      # Author information
│   │   └── gemini_service.py      # Gemini AI integration (400+ lines)
│   └── ui/
│       ├── __init__.py
│       └── gemini_page.py         # Gemini UI components
├── tests/
│   ├── __init__.py
│   └── test_book_service.py       # Unit tests (97% coverage)
├── htmlcov/                       # Coverage HTML report
├── venv/                          # Python virtual environment
├── .env.example                   # Template for Gemini API key
├── .gitignore                     # Git ignored files
├── requirements.txt               # Project dependencies
├── README.md                      # Documentation in Spanish
├── README_EN.md                   # Documentation in English ✨ NEW
└── .git/                          # Git repository
```

---

## 📦 Modules and Components

### 1️⃣ `config/settings.py` (100% Coverage ✅)

**Purpose:** Centralized configuration

```python
# Main variables:
BASE_DIR              # Project root path
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

### 2️⃣ `src/models/book.py` (94% Coverage)

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
    theme: str = "No especificado"  # ✨ NEW: Main theme
    pre_questions: List[str]      # 3 pre-reading questions
    post_questions: List[str]     # 3 post-reading questions
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
    author_bio="J.R.R. Tolkien was..."
)
```

---

### 3️⃣ `src/services/book_service.py` (68% Coverage)

**Purpose:** Book CRUD management

```python
class BookService:
    def __init__(self)
    def load_books() → List[Book]           # Load from JSON
    def get_all_books() → List[Book]        # Get all books
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

### 4️⃣ `src/services/gemini_service.py` ✨ NEW

**Purpose:** Google Gemini AI 2.0 Flash integration

```python
class GeminiService:
    def __init__(api_key=None)
    
    # Analysis of a specific book:
    def get_book_summary(book) → str                    # Summary
    def analyze_themes_and_characters(book) → str       # Themes/characters
    def explain_concept(book, concept) → str            # Explain concept
    def get_book_recommendations(book, interests) → str # Recommendations
    def generate_discussion_questions(book) → str       # Debate questions
    def compare_books(book1, book2) → str               # Compare 2 books
    
    # ✨ Intelligent Search (Top 3):
    def search_similar_books(title) → str               # By title
    def search_author_works(author) → str               # By author
    def search_books_by_theme(theme) → str              # By theme ✨ NEW
```

**Features:**
- ✅ Model: `gemini-2.0-flash` (fast and efficient)
- ✅ Guardrails: Rejects non-literary content
- ✅ Validation: Verifies it's a real book
- ✅ Restrictions: No offensive language, no discrimination
- ✅ Downloads: All analyses can be downloaded as .txt

**Example:**
```python
from src.services.gemini_service import GeminiService
from src.models.book import Book

gemini = GeminiService()  # Reads API_KEY from .env

book = Book(..., title="1984", author="George Orwell", theme="Totalitarianism", ...)
summary = gemini.get_book_summary(book)
print(summary)  # → Detailed 1984 summary

themes = gemini.search_books_by_theme("Totalitarianism")
print(themes)  # → Top 3 books about totalitarianism
```

---

### 5️⃣ `src/services/question_service.py`

**Purpose:** Reflective questions management

```python
class QuestionService:
    def get_pre_questions(book_id) → List[str]         # Pre-reading Qs
    def get_post_questions(book_id) → List[str]        # Post-reading Qs
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

### 7️⃣ `src/ui/gemini_page.py` ✨ NEW

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

## 🚀 Installation and Execution

### Requirements
- Python 3.8+
- pip (package manager)
- Git

### 1. Clone the repository
```bash
git clone <repository-url>
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

### 4. Configure Gemini (Optional but recommended)

#### Step A: Get API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Get API Key"
3. Copy your key

#### Step B: Create .env file
In the project root, create `.env`:
```env
GEMINI_API_KEY=your_key_here
```

Or use the template:
```bash
cp .env.example .env
# Then edit .env with your key
```

### 5. Run the application
```bash
streamlit run app.py
```

The app will open at `http://localhost:8502`

---

## 📊 Included Data

### 10 Preloaded Classic Books

Each book includes:
- Complete information (title, author, year, genre, **theme**)
- 3 pre-reading questions (before reading)
- 3 post-reading questions (after reading)
- Author biography
- Description/synopsis

**Included Books:**
1. Don Quixote - Miguel de Cervantes
2. Pride and Prejudice - Jane Austen
3. One Hundred Years of Solitude - Gabriel García Márquez
4. 1984 - George Orwell
5. The Hobbit - J.R.R. Tolkien
6. Little Women - Louisa May Alcott
7. Dracula - Bram Stoker
8. The Adventures of Sherlock Holmes - Arthur Conan Doyle
9. The French Revolution - Informative book
10. Psychology of Learning - Educational book

---

## 🧪 Tests and Coverage

### Run Tests
```bash
pytest tests/ -v
```

### Test Results
```
test_book_service.py::TestBookService::test_load_books ✅ PASSED
test_book_service.py::TestBookService::test_get_book_by_id ✅ PASSED
test_book_service.py::TestBookService::test_get_book_by_title ✅ PASSED

================================ 3 passed in 0.01s ===================================
```

### View Coverage
```bash
pytest --cov=src --cov=config tests/ --cov-report=html
# Opens: htmlcov/index.html
```

**Coverage Metrics:**
- `config/settings.py`: 100% ✅
- `tests/test_book_service.py`: 97% ✅
- `src/models/book.py`: 94% ✅
- `src/services/book_service.py`: 68%
- **Total: 84%**

---

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
      "How would you define friendship?",
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
3. Answer the **pre-reading questions** thoughtfully
4. You can download or note your answers

#### **Phase 2: Reading**
- Read the book at your own pace
- Take notes about main ideas
- Reflect while reading

#### **Phase 3: Manual Reflection (Principal Page)**
1. Return to the app
2. Answer the **post-reading questions**
3. Compare your pre and post answers
4. Notice your growth

#### **Phase 4: AI Analysis (Gemini AI Page)**
1. Use "From list" to analyze the same book with AI
2. Compare your reflective analysis with Gemini's
3. Deepen with theme and concept analysis
4. Get recommendations for similar books
5. Download analyses for future reference

#### **Phase 5: Exploration (Intelligent Search)**
- Search books by theme (e.g., "Friendship", "Justice")
- Explore favorite authors' works
- Find books similar to what you read

---

## 💡 Use Cases

### For Students 📖
- Prepare for class discussions
- Understand complex themes quickly
- Analyze required reading books
- Develop critical thinking

### For Teachers 👨‍🏫
- Generate discussion questions
- Create reading activities
- Analyze book themes for lessons
- Personalize recommendations

### For Casual Readers 📕
- Discover new books by theme
- Better understand what you read
- Connect emotionally with stories
- Expand literary horizons

### For Researchers 🔍
- Search books about specific topics
- Compare works by different authors
- Explore literary trends
- Quick content analysis

---

## 🛠️ Technologies Used

| Tool | Version | Purpose |
|---|---|---|
| **Python** | 3.8+ | Main language |
| **Streamlit** | 1.28+ | Web framework |
| **Google Gemini AI** | 2.0-flash | AI analysis |
| **pytest** | 9.0+ | Testing |
| **pytest-cov** | - | Code coverage |
| **python-dotenv** | - | Environment variables |

---

## 📝 Recent Git Commits

```
feat: Add theme-based search in intelligent search
feat: Restrict to books only with content guardrails
feat: Add intelligent search mode for Gemini page
feat: Add custom book/movie input to Gemini AI page
feat: Upgrade to gemini-2.0-flash model
feat: Refactor to multi-page Streamlit app
feat: Add Google Gemini AI integration
```

---

## 🤝 Contributions

Contributions are welcome. Please:
1. Fork the repository
2. Create a branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'feat: Description'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 📄 License

This project is under MIT License. See `LICENSE` file for details.

---

## 👨‍💻 Author

**Developed by:** Development Team

---

## 🐛 Bug Reports

If you find a bug, please:
1. Check if it's a known issue
2. Provide a clear bug description
3. Include steps to reproduce
4. Open an issue on GitHub

---

## 🗺️ Future Roadmap

### v2.0 (Next Improvements)
- [ ] Complete database (100+ books)
- [ ] User authentication
- [ ] Personal progress tracking
- [ ] Reading statistics
- [ ] Reader community
- [ ] Personalized recommendations based on history
- [ ] Integration with book APIs (Google Books, OpenLibrary)
- [ ] Export analyses as PDF
- [ ] Improved dark/light mode
- [ ] Multi-language support

### v2.5
- [ ] Literary podcasts
- [ ] Virtual reading clubs
- [ ] Reading challenges
- [ ] Badges and achievements
- [ ] Social sharing

---

## 📞 Support

For questions or support:
- 📧 Email: [your-email@example.com]
- 💬 Discord: [server-link]
- 🐦 Twitter: [@your-username]

---

## ⭐ If you like it, give us a star on GitHub!

```
        📚
       /|\
        | 
       / \
    ThinkInk ⭐
```

---

**Version:** 2.0  
**Last Updated:** February 2025  
**Status:** ✅ In Production  
**Documentation available in:** [Español](README.md)
