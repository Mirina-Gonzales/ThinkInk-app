import streamlit as st
from dotenv import load_dotenv
from src.services.book_service import BookService
from src.models.book import Book
from src.ui.gemini_page import display_gemini_page, display_gemini_setup_instructions
from src.i18n.i18n_service import t

# Cargar variables de entorno
load_dotenv()

# Obtener idioma
lang = st.session_state.get('language', 'es')

# Configurar página
st.set_page_config(
    page_title="🤖 ThinkInk - Gemini AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Header
st.title(t("gemini_page_title", lang))
st.markdown(
    t("gemini_page_subtitle", lang)
)
st.divider()

# Inicializar servicio
if "book_service" not in st.session_state:
    st.session_state.book_service = BookService()

book_service = st.session_state.book_service

# Sidebar - Selección de libro
with st.sidebar:
    st.header(t("sidebar_select_book", lang))
    st.markdown(
        t("sidebar_compare_approaches", lang) + ":\n"
        "- " + t("sidebar_approach_principal", lang) + "\n"
        "- " + t("sidebar_approach_gemini", lang)
    )
    st.divider()
    
    # Opción: Lista predefinida o entrada personalizada
    input_mode = st.radio(
        t("input_mode", lang),
        [t("input_mode_list", lang), t("input_mode_custom", lang), t("input_mode_search", lang)],
        horizontal=False
    )
    
    selected_book = None
    
    if input_mode == t("input_mode_list", lang):
        books = book_service.get_all_books()
        book_titles = [book.title for book in books]
        
        selected_title = st.selectbox(t("choose_book", lang), book_titles)
        selected_book = book_service.get_book_by_title(selected_title)
    
    elif input_mode == t("input_mode_custom", lang):
        st.subheader(t("gemini_book_input", lang))
        st.info(t("gemini_book_input_note", lang))
        
        title = st.text_input(
            t("custom_title", lang),
            placeholder=t("custom_title_placeholder", lang),
            key="custom_title"
        )
        
        author = st.text_input(
            t("custom_author", lang),
            placeholder=t("custom_author_placeholder", lang),
            key="custom_author"
        )
        
        year = st.number_input(
            t("custom_year", lang),
            min_value=1800,
            max_value=2100,
            value=2024,
            key="custom_year"
        )
        
        genre = st.text_input(
            t("custom_genre", lang),
            placeholder=t("custom_genre_placeholder", lang),
            key="custom_genre"
        )
        
        theme = st.text_input(
            t("custom_theme", lang),
            placeholder=t("custom_theme_placeholder", lang),
            key="custom_theme"
        )
        
        description = st.text_area(
            t("custom_description", lang),
            placeholder=t("custom_description_placeholder", lang),
            height=80,
            key="custom_description"
        )
        
        # Crear libro personalizado
        if title and author:
            selected_book = Book(
                id=999,  # ID temporal
                title=title,
                author=author,
                description=description or f"Análisis de {title}",
                year=int(year),
                genre=genre or "No especificado",
                pre_questions=[],
                post_questions=[],
                author_bio=f"Autor: {author}"
            )
            st.session_state.custom_theme = theme
            st.success(t("book_created", lang) + f" {title}")
        else:
            st.warning(t("book_warning", lang))
            selected_book = None
    
    else:  # Búsqueda inteligente (Top 3)
        st.subheader(t("search_intelligent", lang))
        st.markdown(t("search_instruction", lang))
        st.info(t("gemini_only_books", lang))
        
        search_type = st.radio(
            t("search_type", lang),
            [t("search_by_title", lang), t("search_by_author", lang), t("search_by_theme", lang)],
            key="search_type"
        )
        
        if search_type == t("search_by_title", lang):
            search_query = st.text_input(
                t("search_title_input", lang),
                placeholder=t("search_title_placeholder", lang),
                key="search_title"
            )
            if search_query:
                st.info(t("search_title_searching", lang).replace('{query}', search_query))
                selected_book = Book(
                    id=998,
                    title=f"Top 3 similares a: {search_query}",
                    author="Búsqueda Gemini",
                    description=f"Gemini buscará 3 libros similares a: {search_query}",
                    year=2024,
                    genre="Búsqueda",
                    theme="Literatura",
                    pre_questions=[],
                    post_questions=[],
                    author_bio="Análisis de Gemini"
                )
                st.session_state.search_mode = "titles"
                st.session_state.search_query = search_query
        elif search_type == t("search_by_author", lang):
            author_query = st.text_input(
                t("search_author_input", lang),
                placeholder=t("search_author_placeholder", lang),
                key="search_author"
            )
            if author_query:
                st.info(t("search_author_searching", lang).replace('{query}', author_query))
                selected_book = Book(
                    id=998,
                    title=f"Top 3 obras de: {author_query}",
                    author=author_query,
                    description=f"Gemini mostrará las 3 mejores obras de {author_query}",
                    year=2024,
                    genre="Búsqueda",
                    theme="Literatura",
                    pre_questions=[],
                    post_questions=[],
                    author_bio=f"Búsqueda de obras del autor: {author_query}"
                )
                st.session_state.search_mode = "author"
                st.session_state.search_query = author_query
        else:  # Por tema
            theme_query = st.text_input(
                t("search_theme_input", lang),
                placeholder=t("search_theme_placeholder", lang),
                key="search_theme"
            )
            if theme_query:
                st.info(t("search_theme_searching", lang).replace('{query}', theme_query))
                selected_book = Book(
                    id=998,
                    title=f"Top 3 libros sobre: {theme_query}",
                    author="Búsqueda Gemini",
                    description=f"Gemini mostrará 3 libros que abordan el tema: {theme_query}",
                    year=2024,
                    genre="Búsqueda",
                    theme=theme_query,
                    pre_questions=[],
                    post_questions=[],
                    author_bio="Análisis de Gemini"
                )
                st.session_state.search_mode = "theme"
                st.session_state.search_query = theme_query

# Contenido principal
if selected_book:
    theme_display = st.session_state.get("custom_theme", selected_book.theme)
    st.info(
        f"📚 **{t('book_selected', lang)}** {selected_book.title}\n\n"
        f"✍️ **{t('book_author', lang)}** {selected_book.author}\n\n"
        f"📖 **{t('book_year', lang)}:** {selected_book.year} | **{t('book_genre', lang)}:** {selected_book.genre} | **{t('book_theme', lang)}:** {theme_display}"
    )
    st.divider()
    
    # Mostrar página de Gemini
    display_gemini_page(selected_book)
    
    st.divider()
    display_gemini_setup_instructions()
    
    # Comparativa
    st.markdown("---\n\n")
    st.markdown("## " + t("comparison_title", lang))
    st.markdown(t("comparison_manual", lang))
    st.markdown(t("comparison_ai", lang))
    st.markdown(t("comparison_recommendation", lang))

elif input_mode == t("input_mode_list", lang):
    st.warning(t("book_not_selected_list", lang))
else:
    st.info(t("book_not_selected_custom", lang))

# Footer
st.divider()
st.markdown(
    "<div style='text-align: center'><small>🤖 ThinkInk - Gemini AI Analysis | " + t("app_subtitle", lang) + "</small></div>",
    unsafe_allow_html=True,
)
