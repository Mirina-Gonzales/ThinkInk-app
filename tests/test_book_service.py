"""
Unit tests for BookService, Book model, and related services.
Run with: pytest tests/ -v
Coverage: pytest --cov=src --cov=config tests/ --cov-report=html
"""

import pytest
from src.models.book import Book
from src.services.book_service import BookService
from src.services.question_service import QuestionService
from src.services.author_service import AuthorService


class TestBookModel:
    """Tests for Book dataclass"""
    
    def test_book_creation(self):
        """Test creating a Book instance"""
        book = Book(
            id=1,
            title="Test Book",
            author="Test Author",
            year=2025,
            genre="Fiction",
            theme="Adventure",
            description="A test book",
            pre_questions=["Q1", "Q2", "Q3"],
            post_questions=["Q4", "Q5", "Q6"],
            author_bio="Bio of test author"
        )
        assert book.id == 1
        assert book.title == "Test Book"
        assert book.author == "Test Author"
        assert book.year == 2025
        assert book.genre == "Fiction"
        assert book.theme == "Adventure"
        
    def test_book_default_theme(self):
        """Test that theme defaults to 'No especificado'"""
        book = Book(
            id=1,
            title="Test",
            author="Author",
            year=2025,
            genre="Fiction",
            description="Test",
            pre_questions=[],
            post_questions=[],
            author_bio="Bio"
        )
        assert book.theme == "No especificado"
    
    def test_book_to_dict(self):
        """Test converting Book to dictionary"""
        book = Book(
            id=1,
            title="Test Book",
            author="Test Author",
            year=2025,
            genre="Fiction",
            theme="Adventure",
            description="A test book",
            pre_questions=["Q1"],
            post_questions=["Q2"],
            author_bio="Bio"
        )
        book_dict = book.to_dict()
        
        assert isinstance(book_dict, dict)
        assert book_dict["id"] == 1
        assert book_dict["title"] == "Test Book"
        assert book_dict["author"] == "Test Author"
        assert book_dict["year"] == 2025
        assert book_dict["genre"] == "Fiction"
        assert book_dict["theme"] == "Adventure"
        assert book_dict["pre_questions"] == ["Q1"]
        assert book_dict["post_questions"] == ["Q2"]
    
    def test_book_from_dict(self):
        """Test creating Book from dictionary"""
        book_dict = {
            "id": 1,
            "title": "Test Book",
            "author": "Test Author",
            "year": 2025,
            "genre": "Fiction",
            "theme": "Adventure",
            "description": "A test book",
            "pre_questions": ["Q1"],
            "post_questions": ["Q2"],
            "author_bio": "Bio"
        }
        book = Book.from_dict(book_dict)
        
        assert book.id == 1
        assert book.title == "Test Book"
        assert book.author == "Test Author"
        assert book.year == 2025
        assert book.genre == "Fiction"
        assert book.theme == "Adventure"
        assert book.pre_questions == ["Q1"]
    
    def test_book_serialization_roundtrip(self):
        """Test that to_dict -> from_dict preserves data"""
        original = Book(
            id=1,
            title="Test Book",
            author="Test Author",
            year=2025,
            genre="Fiction",
            theme="Adventure",
            description="A test book",
            pre_questions=["Q1", "Q2"],
            post_questions=["Q3", "Q4"],
            author_bio="Bio"
        )
        
        book_dict = original.to_dict()
        restored = Book.from_dict(book_dict)
        
        assert restored.id == original.id
        assert restored.title == original.title
        assert restored.author == original.author
        assert restored.year == original.year
        assert restored.genre == original.genre
        assert restored.theme == original.theme


class TestBookService:
    """Tests for BookService"""
    
    @pytest.fixture
    def service(self):
        """Create BookService instance for testing"""
        return BookService()
    
    def test_get_all_books_count(self, service):
        """Test that we load at least 10 books"""
        books = service.get_all_books()
        assert isinstance(books, list)
        assert len(books) >= 10
    
    def test_get_book_by_id(self, service):
        """Test getting a book by ID"""
        book = service.get_book_by_id(1)
        assert book is not None
        assert book.id == 1
        assert isinstance(book, Book)
    
    def test_get_book_by_id_not_found(self, service):
        """Test getting a book with invalid ID returns None"""
        book = service.get_book_by_id(99999)
        assert book is None
    
    def test_get_book_by_title_real_book(self, service):
        """Test getting a book by title using real book data"""
        book = service.get_book_by_id(1)
        
        # Get the same book by title
        found = service.get_book_by_title(book.title)
        assert found is not None
        assert found.id == book.id
    
    def test_get_book_by_title_case_insensitive(self, service):
        """Test that title search is case insensitive"""
        book = service.get_book_by_id(1)
        
        # Search with different case
        found = service.get_book_by_title(book.title.lower())
        assert found is not None
    
    def test_get_book_by_title_not_found(self, service):
        """Test getting a book with invalid title returns None"""
        book = service.get_book_by_title("Nonexistent Book Title XYZ 123 ABC")
        assert book is None
    
    def test_get_books_by_genre(self, service):
        """Test getting books by genre"""
        books = service.get_all_books()
        
        if len(books) > 0:
            first_genre = books[0].genre
            genre_books = service.get_books_by_genre(first_genre)
            
            assert len(genre_books) > 0
            assert all(book.genre.lower() == first_genre.lower() for book in genre_books)
    
    def test_save_books(self, service):
        """Test saving books doesn't raise exception"""
        # This should not raise an exception
        service.save_books()
    
    def test_book_attributes_preserved(self, service):
        """Test that book attributes are preserved correctly"""
        book = service.get_book_by_id(1)
        
        assert book.id is not None
        assert book.title is not None and len(book.title) > 0
        assert book.author is not None and len(book.author) > 0
        assert book.year is not None and book.year > 0
        assert book.genre is not None and len(book.genre) > 0
        assert book.description is not None and len(book.description) > 0
        assert book.pre_questions is not None and len(book.pre_questions) > 0
        assert book.post_questions is not None and len(book.post_questions) > 0
        assert book.author_bio is not None and len(book.author_bio) > 0
    
    def test_books_have_valid_years(self, service):
        """Test that all books have valid publication years"""
        books = service.get_all_books()
        
        for book in books:
            assert isinstance(book.year, int)
            assert book.year > 0
            assert book.year <= 2025


class TestQuestionService:
    """Tests for QuestionService"""
    
    def test_get_pre_questions(self):
        """Test getting pre-reading questions from a book"""
        book = Book(
            id=1,
            title="Test Book",
            author="Test Author",
            year=2025,
            genre="Fiction",
            description="Test",
            pre_questions=["Why?", "What?", "How?"],
            post_questions=["Q1"],
            author_bio="Bio"
        )
        
        questions = QuestionService.get_pre_questions(book)
        
        assert isinstance(questions, list)
        assert len(questions) == 3
        assert "Why?" in questions
    
    def test_get_post_questions(self):
        """Test getting post-reading questions from a book"""
        book = Book(
            id=1,
            title="Test Book",
            author="Test Author",
            year=2025,
            genre="Fiction",
            description="Test",
            pre_questions=["Q1"],
            post_questions=["Reflection", "Growth", "Change"],
            author_bio="Bio"
        )
        
        questions = QuestionService.get_post_questions(book)
        
        assert isinstance(questions, list)
        assert len(questions) == 3
        assert "Reflection" in questions
    
    def test_format_questions_for_display(self):
        """Test formatting questions for display"""
        questions = ["Question 1", "Question 2", "Question 3"]
        
        formatted = QuestionService.format_questions_for_display(questions)
        
        assert isinstance(formatted, str)
        assert "•" in formatted
        assert "Question 1" in formatted
    
    def test_evaluate_answers(self):
        """Test evaluating user answers"""
        answers = {
            "q1": "Answer 1",
            "q2": "Answer 2",
            "q3": ""
        }
        
        result = QuestionService.evaluate_answers(answers)
        
        assert isinstance(result, dict)
        assert result["total_questions"] == 3
        assert result["answered"] == 2
    
    def test_evaluate_answers_all_empty(self):
        """Test evaluating empty answers"""
        answers = {"q1": "", "q2": "", "q3": ""}
        
        result = QuestionService.evaluate_answers(answers)
        
        assert result["total_questions"] == 3
        assert result["answered"] == 0


class TestAuthorService:
    """Tests for AuthorService"""
    
    def test_get_author_bio(self):
        """Test getting author biography"""
        book = Book(
            id=1,
            title="Test Book",
            author="Test Author",
            year=2025,
            genre="Fiction",
            description="Test",
            pre_questions=["Q1"],
            post_questions=["Q2"],
            author_bio="This is a test biography."
        )
        
        bio = AuthorService.get_author_bio(book)
        
        assert isinstance(bio, str)
        assert len(bio) > 0
        assert "test biography" in bio
    
    def test_format_author_info(self):
        """Test formatting author information"""
        book = Book(
            id=1,
            title="Test Book",
            author="Jane Doe",
            year=2025,
            genre="Fiction",
            description="Test",
            pre_questions=["Q1"],
            post_questions=["Q2"],
            author_bio="Jane Doe is a famous author."
        )
        
        formatted = AuthorService.format_author_info(book)
        
        assert isinstance(formatted, str)
        assert "Jane Doe" in formatted


class TestIntegration:
    """Integration tests"""
    
    def test_book_service_with_questions_and_author(self):
        """Test BookService with Question and Author services"""
        service = BookService()
        
        # Get a book
        book = service.get_book_by_id(1)
        assert book is not None
        
        # Get questions for the book
        pre_q = QuestionService.get_pre_questions(book)
        post_q = QuestionService.get_post_questions(book)
        assert len(pre_q) > 0
        assert len(post_q) > 0
        
        # Get author info
        bio = AuthorService.get_author_bio(book)
        assert len(bio) > 0
    
    def test_all_books_have_complete_data(self):
        """Test that all books have complete data"""
        service = BookService()
        books = service.get_all_books()
        
        for book in books:
            assert book.id > 0
            assert len(book.title) > 0
            assert len(book.author) > 0
            assert book.year > 0
            assert len(book.genre) > 0
            assert len(book.description) > 0
            assert len(book.pre_questions) > 0
            assert len(book.post_questions) > 0
            assert len(book.author_bio) > 0
    
    def test_book_title_uniqueness(self):
        """Test that book titles are unique"""
        service = BookService()
        books = service.get_all_books()
        
        titles = [book.title for book in books]
        assert len(titles) == len(set(titles))


class TestErrorHandling:
    """Tests for error handling"""
    
    def test_invalid_book_id_returns_none(self):
        """Test that invalid book ID returns None"""
        service = BookService()
        book = service.get_book_by_id(-1)
        assert book is None
    
    def test_empty_title_search_returns_none(self):
        """Test that empty title search returns None"""
        service = BookService()
        book = service.get_book_by_title("")
        assert book is None
    
    def test_book_service_graceful_handling(self):
        """Test BookService handles edge cases gracefully"""
        service = BookService()
        
        # These should not raise exceptions
        books = service.get_all_books()
        assert len(books) > 0
        
        book = service.get_book_by_id(0)
        assert book is None
    
    def test_question_service_format_empty_questions(self):
        """Test formatting empty question list"""
        formatted = QuestionService.format_questions_for_display([])
        assert isinstance(formatted, str)
