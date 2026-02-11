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
    pre_questions: List[str]
    post_questions: List[str]
    author_bio: str

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "year": self.year,
            "genre": self.genre,
            "pre_questions": self.pre_questions,
            "post_questions": self.post_questions,
            "author_bio": self.author_bio,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
