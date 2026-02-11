import unittest
from pathlib import Path
import json
import tempfile

from src.services.book_service import BookService
from src.models.book import Book


class TestBookService(unittest.TestCase):
    def setUp(self):
        """Crear archivo temporal para pruebas"""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.books_file = Path(self.temp_dir.name) / "test_books.json"
        
        # Crear datos de prueba
        test_data = [
            {
                "id": 1,
                "title": "Test Book",
                "author": "Test Author",
                "description": "A test book",
                "year": 2020,
                "genre": "Fiction",
                "pre_questions": ["Q1"],
                "post_questions": ["Q2"],
                "author_bio": "Test bio",
            }
        ]
        
        with open(self.books_file, "w") as f:
            json.dump(test_data, f)
        
        self.service = BookService(self.books_file)
    
    def tearDown(self):
        """Limpiar archivos temporales"""
        self.temp_dir.cleanup()
    
    def test_load_books(self):
        """Prueba que los libros se cargan correctamente"""
        books = self.service.get_all_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Test Book")
    
    def test_get_book_by_id(self):
        """Prueba obtener libro por ID"""
        book = self.service.get_book_by_id(1)
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Test Book")
    
    def test_get_book_by_title(self):
        """Prueba obtener libro por título"""
        book = self.service.get_book_by_title("Test Book")
        self.assertIsNotNone(book)
        self.assertEqual(book.author, "Test Author")


if __name__ == "__main__":
    unittest.main()
