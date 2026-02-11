import streamlit as st
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar página
st.set_page_config(
    page_title="📚 ThinkInk App",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Header
st.title("📚 ThinkInk - Aplicación de Preguntas sobre Libros")
st.markdown(
    "Prepárate antes de leer, reflexiona después de terminar y conoce más sobre los autores."
)
st.divider()

# Contenido de bienvenida
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ## 📖 ¿Qué es ThinkInk?
    
    ThinkInk es una aplicación diseñada para mejorar tu experiencia de lectura mediante:
    
    ### 🎯 Características Principales
    
    - **📚 Página Principal**
      - Preguntas previas para prepararte
      - Preguntas finales para reflexionar
      - Biografías de autores
      - Enfoque en pensamiento crítico
    
    - **🤖 Página Gemini AI**
      - Análisis con inteligencia artificial
      - Resúmenes instantáneos
      - Recomendaciones personalizadas
      - Explicación de conceptos
      - Comparación de libros
    """)

with col2:
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
    
    ### 📚 10 Libros Disponibles
    - 1984 - George Orwell
    - El Quijote - Miguel de Cervantes
    - Orgullo y Prejuicio - Jane Austen
    - Y 7 más...
    """)

st.divider()

# Instrucciones principales
st.markdown("""
## 🚀 Comienza Ahora

### Opción 1: Análisis Reflexivo (Recomendado)
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

## 📊 Comparativa de Enfoques

| Aspecto | Página Principal | Gemini AI |
|--------|-----------------|-----------|
| **Enfoque** | Reflexivo | Analítico |
| **Tiempo** | Mayor | Instantáneo |
| **Conexión** | Personal | Objetiva |
| **Profundidad** | Emocional | Técnica |
| **Aprendizaje** | Crítico | Informativo |

**💡 Lo ideal:** Usa ambas páginas para una experiencia completa.

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

---

## 📁 Estructura del Proyecto

```
ThinkInk-app/
├── app.py                    # Esta página (inicio)
├── pages/
│   ├── 01_📚_Principal.py    # Análisis reflexivo
│   └── 02_🤖_Gemini_AI.py    # Análisis con IA
├── src/
│   ├── models/
│   ├── services/
│   └── ui/
├── data/
│   └── books.json            # 10 libros
└── venv/                      # Entorno virtual
```

---

## 💡 Tips

- 🔗 Usa ambas páginas para comprensión profunda
- 📝 Descarga los análisis de Gemini
- 🔄 Compara tus respuestas con el análisis IA
- 📚 Lee la biografía del autor
- 🎯 Reflexiona sobre los aprendizajes

""")

# Footer
st.divider()
st.markdown(
    "<div style='text-align: center'><small>📚 ThinkInk App - Mejora tu experiencia de lectura</small></div>",
    unsafe_allow_html=True,
)
