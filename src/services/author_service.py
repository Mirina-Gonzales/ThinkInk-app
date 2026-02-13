from src.models.book import Book
from src.i18n.i18n_service import t


class AuthorService:
    @staticmethod
    def get_author_bio(book: Book) -> str:
        """Obtiene la biografía del autor"""
        return book.author_bio

    @staticmethod
    def format_author_info(book: Book, lang: str = "es") -> str:
        """Formatea la información del autor para mostrar"""
        return f"""
### 🖊️ {t("principal_author_bio", lang)}
**{book.author}**

{book.author_bio}
"""
