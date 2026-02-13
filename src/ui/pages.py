import streamlit as st
from src.models.book import Book
from src.services.author_service import AuthorService
from src.i18n.i18n_service import t


def display_book_card(book: Book, lang: str = "es"):
    """Muestra una tarjeta del libro"""
    with st.container():
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.metric(t("book_year", lang), book.year)
            st.metric(t("book_genre", lang), book.genre)
        
        with col2:
            st.write(f"**{book.title}**")
            st.write(f"{t('book_author', lang)}: *{book.author}*")
            st.write(book.description)
        
        st.divider()


def display_author_section(book: Book, lang: str = "es"):
    """Muestra la sección del autor"""
    bio = AuthorService.get_author_bio(book)
    st.markdown(AuthorService.format_author_info(book, lang))


def display_questions(questions: list, question_type: str, lang: str = "es"):
    """Muestra las preguntas de forma interactiva"""
    st.subheader(f"📋 {question_type}")
    
    answers = {}
    for i, question in enumerate(questions, 1):
        st.write(f"**{i}. {question}**")
        answer = st.text_area(
            label=f"{t('answer', lang)} {i}" if t("answer", lang) else f"Answer {i}",
            height=100,
            key=f"q_{i}_{question_type}",
            label_visibility="collapsed",
        )
        answers[i] = answer
    
    return answers
