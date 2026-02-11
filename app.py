import streamlit as st
from config.settings import STREAMLIT_CONFIG
from src.services.book_service import BookService
from src.services.question_service import QuestionService
from src.ui.pages import display_book_card, display_author_section, display_questions
from src.ui.gemini_page import display_gemini_page, display_gemini_setup_instructions

# Configurar página
st.set_page_config(**STREAMLIT_CONFIG)

# Inicializar sesión
if "book_service" not in st.session_state:
    st.session_state.book_service = BookService()

book_service = st.session_state.book_service

# Header
st.title("📚 ThinkInk - Aplicación de Preguntas sobre Libros")
st.markdown(
    "Prepárate antes de leer, reflexiona después de terminar y conoce más sobre los autores."
)
st.divider()

# Sidebar - Selección de libro
with st.sidebar:
    st.header("📖 Biblioteca")
    books = book_service.get_all_books()
    book_titles = [book.title for book in books]
    
    selected_title = st.selectbox("Selecciona un libro:", book_titles)
    selected_book = book_service.get_book_by_title(selected_title)

# Tabs principales
if selected_book:
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["📘 Información", "❓ Preguntas Previas", "✅ Preguntas Finales", "🖊️ Autor", "🤖 Gemini AI"]
    )
    
    with tab1:
        st.subheader(f"{selected_book.title}")
        display_book_card(selected_book)
    
    with tab2:
        st.subheader("Preguntas Antes de Leer")
        st.info(
            "💡 Responde estas preguntas ANTES de comenzar a leer. Te ayudarán a preparar tu mente para los temas del libro."
        )
        pre_answers = display_questions(
            selected_book.pre_questions, "Preguntas Previas"
        )
        
        if st.button("Guardar respuestas previas", key="save_pre"):
            st.success("✅ Respuestas previas guardadas!")
    
    with tab3:
        st.subheader("Preguntas Después de Leer")
        st.info(
            "💭 Responde estas preguntas DESPUÉS de terminar el libro. Servirán para reflexionar sobre lo leído."
        )
        post_answers = display_questions(
            selected_book.post_questions, "Preguntas Finales"
        )
        
        if st.button("Guardar respuestas finales", key="save_post"):
            st.success("✅ Respuestas finales guardadas!")
    
    with tab4:
        display_author_section(selected_book)
        
        with st.expander("📊 Más estadísticas del autor"):
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Libro", selected_book.title)
                st.metric("Género", selected_book.genre)
            with col2:
                st.metric("Año de publicación", selected_book.year)
                st.metric("Autor", selected_book.author)
    
    with tab5:
        display_gemini_page(selected_book)
        st.divider()
        display_gemini_setup_instructions()

else:
    st.warning("⚠️ Por favor selecciona un libro de la lista.")

# Footer
st.divider()
st.markdown(
    "<div style='text-align: center'><small>📚 ThinkInk App - Mejora tu experiencia de lectura</small></div>",
    unsafe_allow_html=True,
)
