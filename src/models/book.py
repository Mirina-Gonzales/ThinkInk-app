from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    id: int
    title: str
    author: str
    description: str
    year: int
    genre: str
    theme: str = "No especificado"
    pre_questions: List[str] = None
    post_questions: List[str] = None
    author_bio: str = ""

    def __post_init__(self):
        if self.pre_questions is None:
            self.pre_questions = []
        if self.post_questions is None:
            self.post_questions = []

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "year": self.year,
            "genre": self.genre,
            "theme": self.theme,
            "pre_questions": self.pre_questions,
            "post_questions": self.post_questions,
            "author_bio": self.author_bio,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
