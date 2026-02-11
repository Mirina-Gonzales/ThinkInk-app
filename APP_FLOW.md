# 🚀 ThinkInk App - Flujo Completo

## 📊 Flujo General de Usuario

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         USUARIO ACCEDE A LA APP                         │
│                    http://localhost:8502 (streamlit)                    │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │  PÁGINA DE INICIO (app.py)  │
                    │  - Welcome message          │
                    │  - Instrucciones            │
                    │  - Características          │
                    └──────────────┬──────────────┘
                                   │
                ┌──────────────────┼──────────────────┐
                │                  │                  │
                │     ✓ NUEVO      │     ✓ NUEVO     │
         ┌──────▼──────┐    ┌──────▼──────┐   ┌─────▼──────┐
         │  SELECTOR   │    │  SELECTOR   │   │  SELECTOR  │
         │  IDIOMA 🇪🇸 │    │  IDIOMA 🇬🇧 │   │  LIBRO 📚  │
         └──────┬──────┘    └──────┬──────┘   └─────┬──────┘
                │                  │               │
                └──────────────────┼───────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   SIDEBAR - NAVEGACIÓN      │
                    │   - 🇪🇸 Español             │
                    │   - 🇬🇧 English             │
                    │   - 📚 Principal            │
                    │   - 🤖 Gemini AI            │
                    └──────────────┬──────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
   ┌────▼────────────┐    ┌────────▼────────┐    ┌──────────▼────┐
   │ 📚 PRINCIPAL    │    │ 🤖 GEMINI AI   │    │ 🏠 HOME PAGE  │
   │ (Local)         │    │ (IA - Cloud)   │    │ (Bienvenida)  │
   └────┬────────────┘    └────────┬────────┘    └──────────┬────┘
        │                          │                       │
        │                          │                       │
        └──────────────────────────┼───────────────────────┘
```

---

## 🏠 PÁGINA 1: HOME (app.py) - Bienvenida

```
app.py (PÁGINA INICIAL)
│
├─ 1. CONFIGURACIÓN INICIAL
│  ├─ st.set_page_config(...) ← Config Streamlit
│  └─ st.session_state ← Init language = "es"
│
├─ 2. SELECTOR DE IDIOMA (Sidebar)
│  ├─ st.button("🇪🇸 Español")
│  │  └─ st.session_state.language = "es"
│  │     └─ st.rerun() ← Recarga con nuevo idioma
│  │
│  └─ st.button("🇬🇧 English")
│     └─ st.session_state.language = "en"
│        └─ st.rerun() ← Recarga con nuevo idioma
│
├─ 3. OBTENER IDIOMA ACTUAL
│  └─ lang = st.session_state.language
│
├─ 4. MOSTRAR CONTENIDO BILINGÜE
│  ├─ st.title(t("app_title", lang))
│  │  └─ Llama: i18n.get("app_title", lang)
│  │     └─ translations.json
│  │        ├─ ES: "🤖 ThinkInk - Análisis de Libros"
│  │        └─ EN: "🤖 ThinkInk - Book Analysis"
│  │
│  ├─ st.markdown(t("app_subtitle", lang))
│  ├─ Instrucciones bilingües
│  ├─ Características
│  ├─ Comparativa
│  └─ Configuración Gemini
│
└─ 5. NAVEGACIÓN HACIA OTRAS PÁGINAS
   └─ Sidebar muestra: 📚 Principal | 🤖 Gemini AI
      └─ Usuario hace clic en cualquiera
```

---

## 📚 PÁGINA 2: PRINCIPAL (01_📚_Principal.py) - Análisis Reflexivo

```
pages/01_📚_Principal.py
│
├─ 1. INICIALIZACIÓN
│  ├─ from src.i18n import t
│  ├─ from src.services.book_service import BookService
│  ├─ lang = st.session_state.get("language", "es")
│  └─ book_service = BookService()
│
├─ 2. SIDEBAR - SELECCIÓN DE LIBRO
│  ├─ st.header(t("sidebar_select_book", lang))
│  ├─ books = book_service.get_all_books() ← Carga data/books.json
│  │  └─ [10 libros clásicos]
│  │
│  ├─ st.selectbox(t("choose_book", lang), books)
│  │  └─ Usuario selecciona libro
│  │
│  └─ selected_book = book_service.get_book_by_title(selected_title)
│
├─ 3. MOSTRAR INFORMACIÓN DEL LIBRO
│  ├─ st.info(
│  │    f"📚 {selected_book.title}
│  │     ✍️ {selected_book.author}
│  │     📖 {selected_book.year} | {selected_book.genre}
│  │     🎯 {selected_book.theme}")
│  │
│  └─ ESTRUCTURA Book:
│     ├─ id
│     ├─ title
│     ├─ author
│     ├─ year
│     ├─ genre
│     ├─ theme ← NUEVO
│     ├─ description
│     ├─ pre_questions
│     ├─ post_questions
│     └─ author_bio
│
├─ 4. TABS - CONTENIDO REFLEXIVO
│  │
│  ├─ TAB 1: INFORMACIÓN DEL LIBRO
│  │  └─ Muestra detalles + descripción
│  │
│  ├─ TAB 2: PREGUNTAS PREVIAS ❓
│  │  ├─ st.subheader(t("principal_pre_questions", lang))
│  │  ├─ st.write(t("principal_pre_questions_desc", lang))
│  │  │  └─ "Responde ANTES de leer"
│  │  │
│  │  ├─ MOSTRAR 3 PREGUNTAS:
│  │  │  └─ for i, question in enumerate(selected_book.pre_questions):
│  │  │     └─ st.write(f"{i+1}. {question}")
│  │  │
│  │  ├─ ÁREA PARA RESPUESTAS:
│  │  │  └─ st.text_area(t("answer_placeholder", lang))
│  │  │
│  │  └─ BOTÓN GUARDAR:
│  │     └─ if st.button(t("btn_save_pre_answers", lang)):
│  │        └─ st.success(t("success_pre_answers", lang))
│  │
│  ├─ TAB 3: PREGUNTAS FINALES ❓
│  │  ├─ st.subheader(t("principal_post_questions", lang))
│  │  ├─ st.write(t("principal_post_questions_desc", lang))
│  │  │  └─ "Responde DESPUÉS de leer"
│  │  │
│  │  ├─ MOSTRAR 3 PREGUNTAS:
│  │  │  └─ for i, question in enumerate(selected_book.post_questions):
│  │  │     └─ st.write(f"{i+1}. {question}")
│  │  │
│  │  ├─ ÁREA PARA RESPUESTAS:
│  │  │  └─ st.text_area(t("answer_placeholder", lang))
│  │  │
│  │  └─ BOTÓN GUARDAR:
│  │     └─ if st.button(t("btn_save_post_answers", lang)):
│  │        └─ st.success(t("success_post_answers", lang))
│  │
│  └─ TAB 4: SOBRE EL AUTOR ✍️
│     ├─ st.subheader(t("principal_author_bio", lang))
│     └─ st.write(selected_book.author_bio)
│        └─ Muestra biografía del autor
│
└─ 5. COMPARATIVA (Expandible)
   └─ st.expander(t("comparison_title", lang))
      ├─ Ventajas enfoque reflexivo
      └─ vs. Ventajas enfoque IA
```

---

## 🤖 PÁGINA 3: GEMINI AI (02_🤖_Gemini_AI.py) - Análisis con IA

```
pages/02_🤖_Gemini_AI.py
│
├─ 1. INICIALIZACIÓN
│  ├─ from src.i18n import t
│  ├─ from src.services.gemini_service import GeminiService
│  ├─ from src.services.book_service import BookService
│  ├─ lang = st.session_state.get("language", "es")
│  ├─ gemini_service = GeminiService() ← Conecta Gemini
│  └─ book_service = BookService()
│
├─ 2. SIDEBAR - SELECTOR DE LIBRO (3 OPCIONES) 📚
│  │
│  ├─ OPCIÓN 1: DE LA LISTA
│  │  ├─ st.radio(t("input_mode", lang), 
│  │  │           [t("input_mode_list", lang), ...])
│  │  │
│  │  ├─ Si seleccionó "De la lista":
│  │  │  ├─ books = book_service.get_all_books()
│  │  │  ├─ st.selectbox(t("choose_book", lang))
│  │  │  └─ selected_book = book_service.get_book_by_title(title)
│  │  │
│  │  └─ selected_book → Libro de los 10 predefinidos
│  │
│  ├─ OPCIÓN 2: INGRESO PERSONALIZADO 🎬
│  │  ├─ Si seleccionó "Ingreso personalizado":
│  │  │
│  │  ├─ FORMULARIO:
│  │  │  ├─ title = st.text_input(t("custom_title", lang))
│  │  │  ├─ author = st.text_input(t("custom_author", lang))
│  │  │  ├─ year = st.number_input(t("custom_year", lang))
│  │  │  ├─ genre = st.text_input(t("custom_genre", lang))
│  │  │  ├─ theme = st.text_input(t("custom_theme", lang))
│  │  │  │            └─ ✨ NUEVO CAMPO
│  │  │  └─ description = st.text_area(t("custom_description", lang))
│  │  │
│  │  ├─ VALIDACIÓN:
│  │  │  └─ if title and author:
│  │  │     └─ selected_book = Book(...)
│  │  │        └─ Crea objeto dinámico
│  │  │     └─ st.success(t("book_created", lang))
│  │  │
│  │  └─ selected_book → Libro temporal creado (ID=999)
│  │
│  └─ OPCIÓN 3: BÚSQUEDA INTELIGENTE (TOP 3) 🔍
│     ├─ Si seleccionó "Búsqueda inteligente":
│     │
│     ├─ SUB-OPCIÓN A: POR TÍTULO
│     │  ├─ search_query = st.text_input(t("search_title_input", lang))
│     │  ├─ st.session_state.search_mode = "titles"
│     │  └─ st.session_state.search_query = search_query
│     │     └─ Guarda criterio de búsqueda
│     │
│     ├─ SUB-OPCIÓN B: POR AUTOR
│     │  ├─ search_query = st.text_input(t("search_author_input", lang))
│     │  ├─ st.session_state.search_mode = "author"
│     │  └─ st.session_state.search_query = search_query
│     │
│     └─ SUB-OPCIÓN C: POR TEMA ✨ NUEVO
│        ├─ theme_query = st.text_input(t("search_theme_input", lang))
│        ├─ st.session_state.search_mode = "theme"
│        └─ st.session_state.search_query = theme_query
│
├─ 3. CONTENIDO PRINCIPAL
│  │
│  ├─ MOSTRAR LIBRO SELECCIONADO:
│  │  └─ st.info(f"📚 {selected_book.title}
│  │            ✍️ {selected_book.author}
│  │            🎯 {selected_book.theme}")
│  │
│  ├─ DETECTAR MODO DE BÚSQUEDA:
│  │  ├─ search_mode = st.session_state.get("search_mode")
│  │  ├─ search_query = st.session_state.get("search_query")
│  │  │
│  │  └─ IF NO ES BÚSQUEDA → MOSTRAR TABS
│  │     │
│  │     ├─ TAB 1: RESUMEN 📖
│  │     │  ├─ st.button(t("btn_summary", lang))
│  │     │  ├─ with st.spinner(...):
│  │     │  │  └─ summary = gemini_service.get_book_summary(selected_book)
│  │     │  │     ├─ PROMPT A GEMINI:
│  │     │  │     │  └─ "Proporciona resumen de '{title}' por {author}"
│  │     │  │     │     + Guardrails (solo libros, sin discriminación)
│  │     │  │     └─ RESPUESTA GEMINI ← Google Gemini 2.0-flash
│  │     │  │
│  │     │  └─ st.download_button(t("download_summary", lang))
│  │     │     └─ Descarga: {titulo}_resumen.txt
│  │     │
│  │     ├─ TAB 2: TEMAS Y PERSONAJES 🎭
│  │     │  ├─ gemini_service.analyze_themes_and_characters(book)
│  │     │  └─ Análisis profundo con Gemini
│  │     │
│  │     ├─ TAB 3: EXPLICAR CONCEPTO 💡
│  │     │  ├─ concept = st.text_input(t("concept_input", lang))
│  │     │  ├─ gemini_service.explain_concept(book, concept)
│  │     │  └─ Explica concepto en contexto del libro
│  │     │
│  │     ├─ TAB 4: RECOMENDACIONES ⭐
│  │     │  ├─ interests = st.text_area(t("interests_input", lang))
│  │     │  ├─ gemini_service.get_book_recommendations(book, interests)
│  │     │  └─ Sugiere 5 libros similares
│  │     │
│  │     ├─ TAB 5: PREGUNTAS DE DISCUSIÓN ❓
│  │     │  ├─ gemini_service.generate_discussion_questions(book)
│  │     │  └─ Genera 8-10 preguntas profundas
│  │     │
│  │     └─ TAB 6: COMPARAR CON OTRO LIBRO 🔄
│  │        ├─ book2_title = st.selectbox(t("compare_book", lang))
│  │        ├─ book2 = book_service.get_book_by_title(book2_title)
│  │        ├─ gemini_service.compare_books(selected_book, book2)
│  │        └─ Comparativa detallada entre 2 libros
│  │
│  └─ IF ES BÚSQUEDA → MOSTRAR RESULTADOS
│     │
│     ├─ SI search_mode == "titles"
│     │  ├─ st.info(f"🔍 Buscando similares a '{search_query}'")
│     │  ├─ st.button(t("btn_search_titles", lang))
│     │  ├─ results = gemini_service.search_similar_books(search_query)
│     │  │  └─ PROMPT A GEMINI:
│     │  │     └─ "Top 3 libros similares a '{search_query}'"
│     │  └─ Descarga: similares_a_{titulo}.txt
│     │
│     ├─ SI search_mode == "author"
│     │  ├─ st.info(f"👤 Mejores obras de '{search_query}'")
│     │  ├─ st.button(t("btn_search_author", lang))
│     │  ├─ results = gemini_service.search_author_works(search_query)
│     │  │  └─ PROMPT A GEMINI:
│     │  │     └─ "Top 3 mejores obras del autor '{search_query}'"
│     │  └─ Descarga: obras_{autor}.txt
│     │
│     └─ SI search_mode == "theme" ✨ NUEVO
│        ├─ st.info(f"🎯 Libros sobre '{search_query}'")
│        ├─ st.button(t("btn_search_theme", lang))
│        ├─ results = gemini_service.search_books_by_theme(search_query)
│        │  └─ PROMPT A GEMINI:
│        │     └─ "Top 3 libros que abordan el tema '{search_query}'"
│        └─ Descarga: libros_sobre_{tema}.txt
│
└─ 4. SETUP GEMINI (Expandible)
   └─ st.expander(t("gemini_setup", lang))
      └─ Instrucciones para obtener API key
```

---

## 🔄 FLUJO DE DATOS - Arquitectura

```
┌─────────────────────────────────────────────────────────────────┐
│                      ENTRADA DE DATOS                           │
└──────────────────────────┬──────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   ┌────▼────┐        ┌────▼────┐      ┌─────▼─────┐
   │ List of │        │  User   │      │ Gemini AI │
   │  Books  │        │  Input  │      │   Cloud   │
   │(JSON)   │        │  Form   │      │  Requests │
   └────┬────┘        └────┬────┘      └─────┬─────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                    ┌──────▼───────┐
                    │  SERVICIOS   │
                    └──────┬───────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   ┌────▼─────────┐   ┌────▼───────┐    ┌────▼──────┐
   │BookService   │   │QuestionSvc │    │GeminiSvc  │
   │- load_books()│   │- get_Q()   │    │- analyze()│
   │- get_book()  │   │- get_post()│    │- search() │
   └────┬─────────┘   └────┬───────┘    └────┬──────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                    ┌──────▼───────┐
                    │   MODELS     │
                    │   Book class │
                    └──────┬───────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   ┌────▼──────────────────┴──────┐      ┌────▼────────┐
   │    TRANSLACIÓN (i18n)        │      │ STREAMLIT   │
   │    - translations.json       │      │ Components  │
   │    - i18n_service.py         │      │ (UI/Pages)  │
   └────┬──────────────────────────┘      └────┬────────┘
        │                                      │
        └──────────────────┬───────────────────┘
                           │
                    ┌──────▼───────┐
                    │   BROWSER    │
                    │  http://     │
                    │ localhost:   │
                    │   8502       │
                    └──────────────┘
```

---

## 🌍 FLUJO DE INTERNACIONALIZACIÓN (i18n)

```
USUARIO SELECCIONA IDIOMA
        │
        ▼
┌─────────────────────────┐
│ st.button("🇪🇸 Español") │  ──┐
│  st.button("🇬🇧 English")│  ──┤
└────────────┬────────────┘    │
             │                 │
             └──────────┬──────┘
                        │
                ┌───────▼────────┐
                │ st.session_state│
                │.language = "es" │
                │    or "en"      │
                └───────┬────────┘
                        │
                ┌───────▼────────────────┐
                │ Todas las páginas:     │
                │ lang = st.session_state│
                │ .get('language','es')  │
                └───────┬────────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
    app.py          pages/*.py       src/ui/*.py
        │               │               │
        └───────────────┼───────────────┘
                        │
                ┌───────▼──────────────┐
                │ t(key, lang)         │
                │ Función de traducción│
                └───────┬──────────────┘
                        │
                ┌───────▼────────────────────┐
                │ i18n_service.py:           │
                │ i18n.get(key, lang)        │
                └───────┬────────────────────┘
                        │
                ┌───────▼────────────────────┐
                │ translations.json:         │
                │ {                          │
                │  "es": {...},              │
                │  "en": {...}               │
                │ }                          │
                └───────┬────────────────────┘
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
   "Español"                       "English"
        │                               │
        │  t("app_title", "es")         │  t("app_title", "en")
        │                               │
        ▼                               ▼
   "🤖 ThinkInk -              "🤖 ThinkInk -
    Análisis de Libros"         Book Analysis"
        │                               │
        └───────────────┬───────────────┘
                        │
                        ▼
                ┌───────────────────┐
                │ RENDERIZAR EN UI  │
                │ (Streamlit)       │
                └───────────────────┘
```

---

## 📡 FLUJO GEMINI AI

```
USUARIO SOLICITA ANÁLISIS
        │
        ▼
┌──────────────────────────────┐
│ Usuario hace click en botón  │
│ (ej: "📖 Generar resumen")   │
└──────────┬───────────────────┘
           │
    ┌──────▼────────┐
    │ st.spinner()  │
    │ ✨ Analizando │
    └──────┬────────┘
           │
   ┌───────▼─────────────┐
   │ GeminiService()     │
   │ .get_book_summary() │
   └───────┬─────────────┘
           │
   ┌───────▼──────────────────────────┐
   │ genai.GenerativeModel()          │
   │ "gemini-2.0-flash"               │
   └───────┬──────────────────────────┘
           │
   ┌───────▼────────────────────────────┐
   │ PROMPT A GEMINI:                   │
   │ ────────────────────────────────   │
   │ "Proporciona resumen de            │
   │  '{title}' de {author}             │
   │                                    │
   │  RESTRICCIONES:                    │
   │  - Solo LIBROS                     │
   │  - Sin malas palabras              │
   │  - Sin discriminación              │
   │  - Tono académico"                 │
   │                                    │
   │ + Información del libro            │
   │ + Tema principal                   │
   └───────┬────────────────────────────┘
           │
           │ HTTP Request
           │ API KEY (from .env)
           ▼
   ┌─────────────────────────┐
   │ GOOGLE GEMINI API       │
   │ Cloud Endpoint          │
   │ (generativeai.google)   │
   └────────┬────────────────┘
            │
            │ LLM Processing
            │ (Gemini 2.0-flash)
            │
            ▼
   ┌─────────────────────┐
   │ AI Response         │
   │ JSON + Text         │
   └────────┬────────────┘
            │
    ┌───────▼──────────────┐
    │ response.text        │
    └────────┬─────────────┘
             │
   ┌─────────▼──────────────────┐
   │ st.markdown(response)      │
   │ Mostrar resultado en app   │
   └─────────┬──────────────────┘
             │
   ┌─────────▼──────────────────┐
   │ st.download_button()       │
   │ Permitir descargar .txt    │
   └────────────────────────────┘
```

---

## 📊 FLUJO DE BÚSQUEDA INTELIGENTE (Top 3)

```
USUARIO SELECCIONA "BÚSQUEDA INTELIGENTE"
        │
        ▼
┌─────────────────────────────────┐
│ 3 OPCIONES:                     │
│ A) Por Título (similares)       │
│ B) Por Autor (mejores obras)    │
│ C) Por Tema (libros sobre tema) │
└─────────┬───────────────────────┘
          │
   ┌──────┴────────┬──────────────┬──────────────┐
   │               │              │              │
   ▼               ▼              ▼              ▼
OPCIÓN A      OPCIÓN B        OPCIÓN C     
"Por Título"  "Por Autor"     "Por Tema" (NEW)
   │               │              │
   ▼               ▼              ▼
search_     search_         search_
query=      query=          query=
"El         "Stephen        "Amistad"
Hobbit"     King"

   │               │              │
   └──────┬────────┴──────────────┘
          │
   ┌──────▼──────────────────────────┐
   │ gemini_service.search_*()       │
   │ (uno de 3 métodos)              │
   └──────┬──────────────────────────┘
          │
   ┌──────▼──────────────────────────┐
   │ PROMPT A GEMINI:                │
   │ "Top 3 libros similares a..."   │
   │ "Top 3 obras de..."             │
   │ "Top 3 libros sobre..."         │
   │                                 │
   │ RETORNA:                        │
   │ - Título + Autor                │
   │ - Año                           │
   │ - Género                        │
   │ - Por qué es similar/destacado  │
   │ - Sinopsis (2-3 líneas)         │
   └──────┬──────────────────────────┘
          │
   ┌──────▼──────────────────────────┐
   │ st.markdown(results)            │
   │ Mostrar Top 3                   │
   └──────┬──────────────────────────┘
          │
   ┌──────▼──────────────────────────┐
   │ st.download_button()            │
   │ Descargar: similares_a_*.txt    │
   │          obras_*.txt            │
   │          libros_sobre_*.txt     │
   └──────────────────────────────────┘
```

---

## 🔒 FLUJO DE VALIDACIÓN Y GUARDRAILS

```
USUARIO INGRESA INFORMACIÓN
        │
        ▼
┌─────────────────────────────┐
│ Es una película?            │ ─────┐
│ ¿Series? ¿Videojuego?      │ ─────┤
│ ¿Otro contenido no-libro?  │ ─────┤
└────┬────────────────────────┘      │
     │                               │
     NO                              YES
     │                               │
     ▼                               ▼
┌──────────────┐        ┌────────────────────────┐
│ Es un libro  │        │ ❌ RECHAZAR            │
│ válido       │        │ "Lo siento, solo      │
└────┬─────────┘        │ analizo LIBROS.       │
     │                  │ '{content}' no es    │
     ▼                  │ un libro"             │
┌──────────────────────┐└────────────────────────┘
│ ENVIAR A GEMINI      │
│ + GUARDRAILS         │
└────┬─────────────────┘
     │
     ▼
┌──────────────────────────────────┐
│ PROMPT CON RESTRICCIONES:        │
│                                  │
│ "IMPORTANTE:                     │
│  - Solo LIBROS (novelas,        │
│    ensayos, poesía, etc)        │
│  - NO películas                 │
│  - NO series                    │
│  - NO videojuegos               │
│                                  │
│  - NO lenguaje ofensivo         │
│  - NO discriminatorio            │
│  - NO hate speech               │
│                                  │
│  - Tono académico               │
│  - Respetuoso                   │
│  - Inclusivo"                   │
└────┬───────────────────────────┘
     │
     ▼
┌────────────────────────────┐
│ Gemini verifica y respeta  │
│ los guardrails             │
└────┬───────────────────────┘
     │
     ▼
┌────────────────────────────┐
│ RESPUESTA VÁLIDA          │
│ Mostrar análisis           │
└────────────────────────────┘
```

---

## 🗂️ ESTRUCTURA DE ARCHIVOS - Flujo de Imports

```
USUARIO ACCEDE
    │
    ▼
pages/ o app.py (ENTRY POINT)
    │
    ├─ import streamlit as st
    ├─ from dotenv import load_dotenv
    ├─ from src.i18n import t ◄─┐
    ├─ from src.services.* import * ◄─┤
    └─ from src.ui.* import * ◄─┤
                                  │
        ┌─────────────────────────┘
        │
        ├─ src/
        │  ├─ i18n/
        │  │  ├─ __init__.py ◄─ from i18n_service.py import t
        │  │  ├─ i18n_service.py ◄─ class I18nService
        │  │  └─ translations.json ◄─ 100+ claves (ES/EN)
        │  │
        │  ├─ models/
        │  │  └─ book.py ◄─ @dataclass Book
        │  │
        │  ├─ services/
        │  │  ├─ book_service.py ◄─ BookService.get_all_books()
        │  │  ├─ gemini_service.py ◄─ GeminiService.analyze_*()
        │  │  ├─ question_service.py
        │  │  └─ author_service.py
        │  │
        │  └─ ui/
        │     └─ gemini_page.py ◄─ display_gemini_page()
        │
        ├─ config/
        │  └─ settings.py ◄─ STREAMLIT_CONFIG, PATHS
        │
        ├─ data/
        │  └─ books.json ◄─ 10 libros con Q&A
        │
        └─ tests/
           └─ test_book_service.py ◄─ 3/3 tests pasadas
```

---

## ⚡ FLUJO COMPLETO DE UNA SESIÓN

```
1. USUARIO ABRE APP
   ↓ http://localhost:8502
   ↓

2. HOME PAGE (app.py)
   ├─ Carga configuración
   ├─ Init session_state.language = "es"
   ├─ Muestra selector idioma
   └─ Usuario selecciona 🇪🇸 o 🇬🇧
   ↓

3. USUARIO NAVEGA A "📚 PRINCIPAL"
   ├─ Página carga con idioma seleccionado
   ├─ BookService carga 10 libros de JSON
   ├─ Usuario selecciona libro
   └─ Muestra 4 tabs:
      - Información
      - Preguntas previas ❓
      - Preguntas finales ❓
      - Sobre el autor ✍️
   ↓

4. USUARIO RESPONDE PREGUNTAS
   ├─ Lee preguntas previas
   ├─ Escribe respuestas
   └─ Hace clic "Guardar"
   ↓

5. USUARIO NAVEGA A "🤖 GEMINI AI"
   ├─ Selecciona modo (lista/custom/búsqueda)
   ├─ Elige libro
   └─ Muestra 6 tabs de análisis IA
   ↓

6. USUARIO SOLICITA ANÁLISIS
   ├─ Hace clic en botón (ej: "Generar resumen")
   ├─ GeminiService prepara prompt
   ├─ Envía a Google Gemini API
   ├─ Gemini responde
   ├─ Muestra resultado
   └─ Usuario descarga análisis
   ↓

7. USUARIO CAMBIA IDIOMA
   ├─ Hace clic 🇬🇧 English (en sidebar)
   ├─ App recarga con st.rerun()
   ├─ TODO cambia a inglés automáticamente
   └─ Contenido dinámico sigue en inglés
   ↓

8. USUARIO CIERRA APP
   └─ Sesión termina
```

---

## 🎯 RESUMEN VISUAL

```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│                    🌍 THINKINК APP FLOW                        │
│                                                                │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │           ENTRADA                                       │ │
│  │  Usuario → http://localhost:8502                        │ │
│  │  ↓                                                       │ │
│  │  Selecciona idioma (🇪🇸/🇬🇧)                             │ │
│  └──────────────────┬──────────────────────────────────────┘ │
│                     │                                        │
│  ┌─────────────────▼──────────────────────────────────────┐ │
│  │         NAVEGACIÓN (SIDEBAR)                           │ │
│  │  • 🏠 Home                                             │ │
│  │  • 📚 Principal (Reflexión Local)                      │ │
│  │  • 🤖 Gemini AI (Análisis IA Cloud)                    │ │
│  │  • 🇪🇸/🇬🇧 Selector de Idioma                           │ │
│  └──────┬────────────────────────────────────────────────┘ │
│         │                                                   │
│  ┌──────┴──────────┬─────────────────────┬────────────┐   │
│  │                 │                     │            │   │
│  ▼                 ▼                     ▼            ▼   │
│ HOME            PRINCIPAL              GEMINI AI     INFO │
│ (Welcome)       (Reflexión)            (IA)              │
│ ────────────    ────────────            ────────────      │
│ • Docs          • 10 Libros             • 10 Libros       │
│ • Features      • Pre-Q                 • Custom          │
│ • Setup         • Post-Q                • Search Top 3    │
│ • Tips          • Author Bio            • 6 análisis      │
│                 • Comparativa           • Descargas       │
│                                                           │
│  ┌────────────────────────────────────────────────────┐  │
│  │           SERVICIOS (Backend)                      │  │
│  │  ├─ BookService (CRUD)                           │  │
│  │  ├─ QuestionService (Preguntas)                  │  │
│  │  ├─ AuthorService (Bios)                         │  │
│  │  ├─ GeminiService (IA API)                       │  │
│  │  └─ I18nService (Traducciones)                   │  │
│  └────────────────────────────────────────────────────┘  │
│                                                           │
│  ┌────────────────────────────────────────────────────┐  │
│  │           DATOS (Persistencia)                     │  │
│  │  ├─ data/books.json (10 libros)                   │  │
│  │  ├─ src/i18n/translations.json (100+ keys)        │  │
│  │  └─ session_state (idioma del usuario)            │  │
│  └────────────────────────────────────────────────────┘  │
│                                                           │
│  ┌────────────────────────────────────────────────────┐  │
│  │           APIs EXTERNAS                            │  │
│  │  └─ Google Gemini API (Cloud)                      │  │
│  │     └─ genai.GenerativeModel("gemini-2.0-flash")  │  │
│  └────────────────────────────────────────────────────┘  │
│                                                           │
└────────────────────────────────────────────────────────────┘
```

---

**Versión:** 2.0 (Final)  
**Actualizado:** Febrero 2025  
**Estado:** ✅ Documentado Completamente
