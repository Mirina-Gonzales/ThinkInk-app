from src.models.book import Book


class AuthorService:
    @staticmethod
    def get_author_bio(book: Book) -> str:
        """Obtiene la biografía del autor"""
        return book.author_bio

    @staticmethod
    def format_author_info(book: Book) -> str:
        """Formatea la información del autor para mostrar"""
        return f"""
### 🖊️ Sobre el Autor
**{book.author}**

{book.author_bio}
"""
