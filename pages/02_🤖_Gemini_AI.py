import streamlit as st
from dotenv import load_dotenv
from src.services.book_service import BookService
from src.ui.gemini_page import display_gemini_page, display_gemini_setup_instructions

# Cargar variables de entorno
load_dotenv()

# Configurar página
st.set_page_config(
    page_title="🤖 ThinkInk - Gemini AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Header
st.title("🤖 Análisis con Gemini AI 2.0 Flash")
st.markdown(
    "Compara análisis de libros: Preguntas reflexivas vs Inteligencia Artificial"
)
st.divider()

# Inicializar servicio
if "book_service" not in st.session_state:
    st.session_state.book_service = BookService()

book_service = st.session_state.book_service

# Sidebar - Selección de libro
with st.sidebar:
    st.header("📖 Selecciona un libro")
    st.markdown(
        """
    **Compara dos enfoques:**
    - 📚 Página Principal: Preguntas reflexivas y pensamiento crítico
    - 🤖 Esta página: Análisis con IA (Gemini 2.0 Flash)
    """
    )
    st.divider()
    
    books = book_service.get_all_books()
    book_titles = [book.title for book in books]
    
    selected_title = st.selectbox("Elige un libro para analizar:", book_titles)
    selected_book = book_service.get_book_by_title(selected_title)

# Contenido principal
if selected_book:
    st.info(
        f"📚 **Libro seleccionado:** {selected_book.title}\n\n"
        f"✍️ **Autor:** {selected_book.author}\n\n"
        f"📖 **Año:** {selected_book.year} | **Género:** {selected_book.genre}"
    )
    st.divider()
    
    # Mostrar página de Gemini
    display_gemini_page(selected_book)
    
    st.divider()
    display_gemini_setup_instructions()
    
    # Comparativa
    st.markdown("""
    ---
    
    ## 📊 Comparativa: Reflexión Manual vs IA
    
    ### 📚 Página Principal (Reflexión Manual)
    - ✅ Preguntas antes de leer (preparación)
    - ✅ Preguntas después de leer (reflexión personal)
    - ✅ Desarrolla pensamiento crítico
    - ✅ Conexión emocional con el texto
    - ✅ Aprendizaje profundo
    
    ### 🤖 Esta Página (Análisis IA)
    - ✅ Resúmenes instantáneos
    - ✅ Análisis de temas y personajes
    - ✅ Recomendaciones personalizadas
    - ✅ Explicaciones de conceptos complejos
    - ✅ Preguntas de discusión generadas
    - ✅ Comparación entre libros
    
    ### 🎯 Recomendación
    **Lo ideal es combinar ambos enfoques:**
    1. Comienza en la **Página Principal** con las preguntas previas
    2. Lee el libro
    3. Responde las **preguntas finales** en la Página Principal
    4. Usa **Gemini AI** aquí para profundizar y explorar más
    """)

else:
    st.warning("⚠️ Por favor selecciona un libro de la lista.")

# Footer
st.divider()
st.markdown(
    "<div style='text-align: center'><small>🤖 ThinkInk - Gemini AI Analysis | Mejora tu experiencia de lectura</small></div>",
    unsafe_allow_html=True,
)
