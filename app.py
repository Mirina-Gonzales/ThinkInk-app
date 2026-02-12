import streamlit as st
from dotenv import load_dotenv
from src.i18n import i18n, t

# Cargar variables de entorno
load_dotenv()

# Configurar página
st.set_page_config(
    page_title="📚 ThinkInk App",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inicializar idioma en session_state
if "language" not in st.session_state:
    st.session_state.language = "es"

# Selector de idioma en sidebar
with st.sidebar:
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🇪🇸 Español", use_container_width=True):
            st.session_state.language = "es"
            st.rerun()
    with col2:
        if st.button("🇬🇧 English", use_container_width=True):
            st.session_state.language = "en"
            st.rerun()
    st.markdown("---")

# Obtener idioma actual
lang = st.session_state.language

# Header
st.title(t("app_title", lang))
st.markdown(t("app_subtitle", lang))
st.divider()

# Contenido de bienvenida
col1, col2 = st.columns(2)

with col1:
    st.image("imagen_1.png", use_column_width=True)
    st.markdown("")  # Espaciador

with col2:
    if lang == "es":
        st.markdown("""
        ## 🎯 Cómo Usar
        
        ### Paso 1: Página Principal
        1. Selecciona un libro del sidebar
        2. Responde las **preguntas previas**
        3. Lee el libro
        4. Responde las **preguntas finales**
        5. Lee la biografía del autor
        
        ### Paso 2: Análisis con IA
        1. Ve a la página **🤖 Gemini AI**
        2. Elige el mismo libro (o diferente)
        3. Selecciona un tipo de análisis
        4. Revisa los resultados
        5. Compara con tus respuestas
        
        """)
    else:
        st.markdown("""
        ## 🎯 How to Use
        
        ### Step 1: Principal Page
        1. Select a book from the sidebar
        2. Answer the **pre-reading questions**
        3. Read the book
        4. Answer the **post-reading questions**
        5. Read the author's biography
        
        ### Step 2: AI Analysis
        1. Go to the **🤖 Gemini AI** page
        2. Choose the same book (or different)
        3. Select a type of analysis
        4. Review the results
        5. Compare with your answers
        
        """)

st.divider()

# Instrucciones principales
if lang == "es":
    st.markdown("""
    ## 🚀 Comienza Ahora
    
    ### Opción 1: Análisis Reflexivo 
    👉 **Ve a la página "📚 Principal"** en el menú lateral
    
    Aquí encontrarás:
    - Selección de 10 libros clásicos
    - Preguntas para reflexionar
    - Información sobre autores
    - Ideal para desarrollar pensamiento crítico
    
    ### Opción 2: Análisis con IA
    👉 **Ve a la página "🤖 Gemini AI"** en el menú lateral
    
    Aquí encontrarás:
    - Análisis automáticos con Google Gemini 2.0 Flash
    - Resúmenes, temas, recomendaciones
    - Comparativa entre enfoques
    - Ideal para explorar perspectivas diferentes
    
    ---
    
    ## ⚙️ Configuración
    
    ### Para usar Gemini AI:
    1. Obtén una API key en: https://makersuite.google.com/app/apikey
    2. Crea un archivo `.env` en la raíz con: `GEMINI_API_KEY=tu_key`
    3. Reinicia la app
    4. ¡Listo! Ya puedes usar la página Gemini AI
    
    ### Sin configurar Gemini:
    - ✅ La página Principal funciona completamente
    - ⚠️ La página Gemini AI mostrará un mensaje de configuración
    """)
else:
    st.markdown("""
    ## 🚀 Get Started Now
    
    ### Option 1: Reflective Analysis
    👉 **Go to the "📚 Principal" page** in the side menu
    
    You will find:
    - Selection of 10 classic books
    - Questions to reflect on
    - Author information
    - Ideal for developing critical thinking
    
    ### Option 2: AI Analysis
    👉 **Go to the "🤖 Gemini AI" page** in the side menu
    
    You will find:
    - Automated analysis with Google Gemini 2.0 Flash
    - Summaries, themes, recommendations
    - Comparison between approaches
    - Ideal for exploring different perspectives
    
    ---
    
    ## ⚙️ Configuration
    
    ### To use Gemini AI:
    1. Get an API key at: https://makersuite.google.com/app/apikey
    2. Create a `.env` file in the root with: `GEMINI_API_KEY=your_key`
    3. Restart the app
    4. Done! Now you can use the Gemini AI page
    
    ### Without configuring Gemini:
    - ✅ The Principal page works completely
    - ⚠️ The Gemini AI page will show a configuration message
    """)

# Footer
st.divider()
if lang == "es":
    st.markdown(
        "<div style='text-align: center'><small>📚 ThinkInk App - Mejora tu experiencia de lectura</small></div>",
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        "<div style='text-align: center'><small>📚 ThinkInk App - Enhance your reading experience</small></div>",
        unsafe_allow_html=True,
    )
