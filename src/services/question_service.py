from typing import List, Dict
from src.models.book import Book


class QuestionService:
    @staticmethod
    def get_pre_questions(book: Book) -> List[str]:
        """Obtiene preguntas previas a la lectura"""
        return book.pre_questions

    @staticmethod
    def get_post_questions(book: Book) -> List[str]:
        """Obtiene preguntas posteriores a la lectura"""
        return book.post_questions

    @staticmethod
    def format_questions_for_display(questions: List[str]) -> str:
        """Formatea las preguntas para mostrar"""
        formatted = "\n".join([f"• {q}" for q in questions])
        return formatted

    @staticmethod
    def evaluate_answers(answers: Dict[str, str]) -> Dict:
        """Evalúa las respuestas del usuario (base para futura expansión)"""
        return {
            "total_questions": len(answers),
            "answered": len([a for a in answers.values() if a.strip()]),
        }
