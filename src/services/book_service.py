import json
from typing import List, Optional
from pathlib import Path

from src.models.book import Book
from config.settings import BOOKS_FILE


class BookService:
    def __init__(self, books_file: Path = BOOKS_FILE):
        self.books_file = books_file
        self.books = self._load_books()

    def _load_books(self) -> List[Book]:
        """Carga los libros desde el archivo JSON"""
        if not self.books_file.exists():
            return []
        
        with open(self.books_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        return [Book.from_dict(book) for book in data]

    def get_all_books(self) -> List[Book]:
        """Retorna todos los libros"""
        return self.books

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        """Obtiene un libro por ID"""
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def get_book_by_title(self, title: str) -> Optional[Book]:
        """Obtiene un libro por título"""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def save_books(self):
        """Guarda los libros en el archivo JSON"""
        self.books_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.books_file, "w", encoding="utf-8") as f:
            data = [book.to_dict() for book in self.books]
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add_book(self, book: Book) -> bool:
        """Añade un nuevo libro"""
        if self.get_book_by_id(book.id):
            return False
        self.books.append(book)
        self.save_books()
        return True

    def get_books_by_genre(self, genre: str) -> List[Book]:
        """Obtiene libros por género"""
        return [book for book in self.books if book.genre.lower() == genre.lower()]
