# 📚 ThinkInk App
### *Despierta tu curiosidad, descubre tu próxima gran historia*
> **Tu compañero literario impulsado por IA** | *Your AI-powered literary companion*

Una aplicación bilingüe diseñada por una **Data Engineer** para transformar la lectura pasiva en una experiencia interactiva y reflexiva. Construida con Python, Streamlit e IA de Google Gemini.

> 📖 **Documentation in English:** [English Documentation](README.md)

---

## ✨ Características Principales

### 📚 Página Principal - Análisis Reflexivo
- ✅ **Preguntas Previas** - 3 preguntas para prepararte antes de leer
- ✅ **Preguntas Finales** - 3 preguntas reflexivas después de terminar
- ✅ **Fichas de Autor** - Biografía y contexto del escritor
- ✅ **Información del Libro** - Detalles, género y tema
- ✅ **10 Libros Clásicos** - Selección curada de literatura
- ✅ **Pensamiento Crítico** - Desarrollo de conexión personal con el texto

### 🤖 Página Gemini AI - Análisis Inteligente
- 🧠 **Resumen Analítico** - IA genera resumen detallado del libro
- 🎭 **Análisis de Temas y Personajes** - Profundización en temas centrales
- 💡 **Explicación de Conceptos** - Entiende ideas complejas del libro
- ⭐ **Recomendaciones Personalizadas** - Libros similares sugeridos
- ❓ **Preguntas de Discusión** - IA genera preguntas de debate
- 🔄 **Comparación de Libros** - Compara dos libros de la biblioteca
- 🎯 **Búsqueda Inteligente (Top 3)** ✨ NUEVA:
  - 📖 **Por Título** - Encuentra 3 libros similares
  - 👤 **Por Autor** - Ve las 3 mejores obras de un autor
  - 🎯 **Por Tema** - Descubre libros sobre un tema específico

### 🔒 Restricciones y Guardrails ✨ 
- ✅ **Solo Libros** - Rechaza películas, series, videojuegos, etc.
- ✅ **Sin Malas Palabras** - Control de contenido ofensivo
- ✅ **Sin Discriminación** - Exclusión de lenguaje discriminatorio
- ✅ **Validación Clara** - Mensajes en español cuando se rechaza contenido
- ✅ **Tono Académico** - Respuestas respetuosas e inclusivas

### 📊 Calidad del Código
- ✅ **Pruebas Unitarias** - 3/3 tests pasando (100%)
- ✅ **Coverage del 16%** - Código bien estructurado
- ✅ **Entorno Virtual** - Aislamiento de dependencias
- ✅ **Bilingüismo i18n** - 100+ traducciones (ES/EN)

---

## 📁 Estructura del Proyecto

```
ThinkInk-app/
├── app.py                          # Página de bienvenida (entry point)
├── pages/
│   ├── 01_📚_Principal.py         # Análisis reflexivo local
│   └── 02_🤖_Gemini_AI.py         # Análisis con IA Gemini
├── config/
│   └── settings.py                # Configuración global (100% coverage)
├── data/
│   └── books.json                 # 10 libros con Q&A y biografías
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   └── book.py                # Dataclass Book (88% coverage)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── book_service.py        # Gestión de libros (68% coverage)
│   │   ├── question_service.py    # Gestión de preguntas
│   │   ├── author_service.py      # Información de autores
│   │   └── gemini_service.py      # Integración Gemini AI (400+ líneas)
│   ├── ui/
│   │   ├── __init__.py
│   │   └── gemini_page.py         # Componentes UI Gemini
│   └── i18n/
│       ├── __init__.py
│       ├── i18n_service.py        # Lógica i18n
│       └── translations.json      # 100+ traducciones ES/EN
├── tests/
│   ├── __init__.py
│   └── test_book_service.py       # Tests unitarios (3/3 pasando)
├── htmlcov/                       # Reporte HTML de coverage
├── venv/                          # Entorno virtual Python
├── .env.example                   # Template para Gemini API key
├── .gitignore                     # Archivos ignorados en Git
├── requirements.txt               # Dependencias del proyecto
├── README.md                      # Documentación en Inglés (PRIMARY)
├── README_ES.md                   # Documentación en Español
└── .git/                          # Repositorio Git
```

---

## 📦 Módulos y Componentes

### 1️⃣ `config/settings.py` (100% Coverage ✅)

**Propósito:** Configuración centralizada

```python
# Variables principales:
BASE_DIR              # Ruta del proyecto
DATA_DIR              # Carpeta /data
BOOKS_FILE            # Ruta a books.json
STREAMLIT_CONFIG      # Config de Streamlit (tema, layout, etc.)
```

**Ejemplo:**
```python
from config.settings import BOOKS_FILE
books = json.load(open(BOOKS_FILE))
```

---

### 2️⃣ `src/models/book.py` (88% Coverage)

**Propósito:** Modelo de datos para libros

```python
@dataclass
class Book:
    id: int                       # ID único
    title: str                    # Título del libro
    author: str                   # Nombre del autor
    description: str              # Sinopsis
    year: int                     # Año de publicación
    genre: str                    # Género (Fantasía, Drama, etc.)
    theme: str = "No especificado"  # Tema principal
    pre_questions: List[str]      # 3 preguntas antes de leer
    post_questions: List[str]     # 3 preguntas después de leer
    author_bio: str               # Biografía del autor
```

**Métodos:**
```python
# Serialización
book_dict = book.to_dict()           # → Diccionario/JSON
book_obj = Book.from_dict(book_dict) # ← Desde diccionario
```

**Ejemplo de uso:**
```python
from src.models.book import Book

book = Book(
    id=1,
    title="El Hobbit",
    author="J.R.R. Tolkien",
    year=1937,
    genre="Fantasía",
    theme="Amistad y Aventura",
    description="Un viaje inesperado...",
    pre_questions=["¿Qué es el valor?", ...],
    post_questions=["¿Cómo cambió Bilbo?", ...],
    author_bio="J.R.R. Tolkien fue..."
)
```

---

### 3️⃣ `src/services/book_service.py` (68% Coverage)

**Propósito:** Gestión CRUD de libros

```python
class BookService:
    def __init__(self)
    def load_books() → List[Book]           # Carga desde JSON
    def get_all_books() → List[Book]        # Todos los libros
    def get_book_by_id(id) → Book           # Busca por ID
    def get_book_by_title(title) → Book     # Busca por título
    def add_book(book) → bool               # Agrega nuevo libro
    def save_books(books) → bool            # Guarda en JSON
```

**Ejemplo:**
```python
from src.services.book_service import BookService

service = BookService()
all_books = service.get_all_books()        # [10 libros]
hobbit = service.get_book_by_title("El Hobbit")
```

---

### 4️⃣ `src/services/gemini_service.py`

**Propósito:** Integración con Google Gemini AI 2.0 Flash

```python
class GeminiService:
    def __init__(api_key=None)
    
    # Análisis de un libro específico:
    def get_book_summary(book) → str                    # Resumen
    def analyze_themes_and_characters(book) → str       # Temas/personajes
    def explain_concept(book, concept) → str            # Explicar concepto
    def get_book_recommendations(book, interests) → str # Recomendaciones
    def generate_discussion_questions(book) → str       # Preguntas de debate
    def compare_books(book1, book2) → str               # Comparar 2 libros
    
    # ✨ Búsqueda inteligente (Top 3):
    def search_similar_books(title) → str               # Por título
    def search_author_works(author) → str               # Por autor
    def search_books_by_theme(theme) → str              # Por tema ✨ NUEVA
```

**Características:**
- ✅ Modelo: `gemini-2.0-flash` (rápido y eficiente)
- ✅ Guardrails: Rechaza contenido no literario
- ✅ Validación: Verifica que sea un libro real
- ✅ Restricciones: Sin malas palabras, sin discriminación
- ✅ Descargas: Todos los análisis se pueden descargar como .txt

**Ejemplo:**
```python
from src.services.gemini_service import GeminiService
from src.models.book import Book

gemini = GeminiService()  # Lee API_KEY de .env

book = Book(..., title="1984", author="George Orwell", theme="Totalitarismo", ...)
summary = gemini.get_book_summary(book)
print(summary)  # → Resumen detallado de 1984

themes = gemini.search_books_by_theme("Totalitarismo")
print(themes)  # → Top 3 libros sobre totalitarismo
```

---

### 5️⃣ `src/services/question_service.py`

**Propósito:** Gestión de preguntas reflexivas

```python
class QuestionService:
    def get_pre_questions(book_id) → List[str]         # Preguntas previas
    def get_post_questions(book_id) → List[str]        # Preguntas finales
```

**Ejemplo:**
```python
from src.services.question_service import QuestionService

service = QuestionService()
pre_q = service.get_pre_questions(book_id=1)
# ["¿Qué esperas del libro?", "¿Qué te atrae de la trama?", ...]
```

---

### 6️⃣ `src/services/author_service.py`

**Propósito:** Información de autores

```python
class AuthorService:
    def get_author_bio(book_id) → str                   # Biografía
```

**Ejemplo:**
```python
from src.services.author_service import AuthorService

service = AuthorService()
bio = service.get_author_bio(book_id=1)
# "J.R.R. Tolkien fue un escritor británico..."
```

---

### 7️⃣ `src/ui/gemini_page.py`

**Propósito:** Componentes UI para la página Gemini

```python
def display_gemini_page(book: Book)              # Interfaz principal
def display_gemini_setup_instructions()          # Instrucciones de setup
```

**Features:**
- 📖 Tab: Resumen
- 🎭 Tab: Temas y Personajes
- 💡 Tab: Explicar Concepto
- ⭐ Tab: Recomendaciones
- ❓ Tab: Preguntas de Discusión
- 🔄 Tab: Comparar Libros
- 🎯 Tab: Búsqueda Inteligente (3 modos)

---

### 8️⃣ `src/i18n/i18n_service.py`

**Propósito:** Sistema de internacionalización (Bilingüe ES/EN)

```python
class I18nService:
    def __init__(self)
    def get(key: str, language: str) → str  # Obtener traducción
    
def t(key: str, language: str) → str        # Función helper acortada
```

**Características:**
- 100+ claves de traducción
- Soporte Español e Inglés
- Fácil extensibilidad
- Persistencia de session state

**Ejemplo:**
```python
from src.i18n import t

title = t("app_title", lang)  # Obtiene título traducido
# Español: "ThinkInk - Análisis de Libros"
# Inglés: "ThinkInk - Book Analysis"
```

---

## 🚀 Instalación y Ejecución

### Requisitos
- Python 3.8+
- pip (gestor de paquetes)
- Git

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd ThinkInk-app
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
# o
venv\Scripts\activate           # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Gemini (Opcional pero recomendado)

#### Paso A: Obtener API Key
1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Haz clic en "Get API Key"
3. Copia tu clave

#### Paso B: Crear archivo .env
En la raíz del proyecto, crea un archivo `.env`:
```env
GEMINI_API_KEY=tu_clave_aqui
```

O usa el template:
```bash
cp .env.example .env
# Luego edita .env con tu clave
```

### 5. Ejecutar la aplicación
```bash
streamlit run app.py
```

La app se abrirá en `http://localhost:8502`

---

## 📊 Datos Incluidos

### 10 Libros Clásicos Precargados

Cada libro incluye:
- Información completa (título, autor, año, género, tema)
- 3 preguntas previas (para antes de leer)
- 3 preguntas finales (para después de leer)
- Biografía del autor
- Descripción/sinopsis

**Libros incluidos:**
1. El Quijote - Miguel de Cervantes
2. Orgullo y Prejuicio - Jane Austen
3. Cien Años de Soledad - Gabriel García Márquez
4. 1984 - George Orwell
5. El Hobbit - J.R.R. Tolkien
6. Mujercitas - Louisa May Alcott
7. Drácula - Bram Stoker
8. Las Aventuras de Sherlock Holmes - Arthur Conan Doyle
9. La Revolución Francesa - Libro informativo
10. Psicología del Aprendizaje - Libro educativo

---

## 🧪 Pruebas y Cobertura

### Ejecutar Tests
```bash
pytest tests/ -v
```

### Resultados de Tests ✅

```
tests/test_book_service.py::TestBookService::test_get_book_by_id PASSED          [ 33%]
tests/test_book_service.py::TestBookService::test_get_book_by_title PASSED       [ 66%]
tests/test_book_service.py::TestBookService::test_load_books PASSED              [100%]

================================ 3 passed in 0.01s ===================================
```

### Ver Cobertura
```bash
pytest --cov=src --cov=config tests/ --cov-report=html
# Abre: htmlcov/index.html
```

**Métricas de Cobertura (Última ejecución):**
```
Name                               Stmts   Miss  Cover
────────────────────────────────────────────────────
config/settings.py                    6      0   100%  ✅
src/models/book.py                   24      3    88%   ✅
src/services/book_service.py          40     13    68%
src/i18n/i18n_service.py              20     20     0%   (No testeado)
src/services/gemini_service.py        96     96     0%   (No testeado)
────────────────────────────────────────────────────
TOTAL                                328    274    16%
```

**Nota:** El coverage muestra 16% en general porque solo hay tests para `book_service.py`. La funcionalidad principal se cubre mediante testing de integración a través de la UI de Streamlit.

---

## 📚 Estructura de data/books.json

```json
[
  {
    "id": 1,
    "title": "El Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937,
    "genre": "Fantasía",
    "theme": "Amistad y Aventura",
    "description": "La historia de Bilbo Bolsón...",
    "pre_questions": [
      "¿Qué es el coraje?",
      "¿Cómo definirías la amistad?",
      "¿Qué significa viajar para ti?"
    ],
    "post_questions": [
      "¿Cómo cambió Bilbo durante el viaje?",
      "¿Cuál fue la lección más importante?",
      "¿Volverías a leer este libro?"
    ],
    "author_bio": "J.R.R. Tolkien fue un escritor británico..."
  },
  ...
]
```

---

## 🔄 Flujo de Trabajo Recomendado

### Usando la App Paso a Paso:

#### **Fase 1: Preparación (Página Principal)**
1. Selecciona un libro de los 10 disponibles
2. Lee la información del libro y autor
3. Responde las **preguntas previas** reflexivamente
4. Puedes descargar o anotar tus respuestas

#### **Fase 2: Lectura**
- Lee el libro en tu tiempo
- Toma notas sobre ideas principales
- Reflexiona mientras lees

#### **Fase 3: Reflexión Manual (Página Principal)**
1. Vuelve a la app
2. Responde las **preguntas finales**
3. Compara tus respuestas previas con las finales
4. Observa tu crecimiento

#### **Fase 4: Análisis IA (Página Gemini AI)**
1. Usa "De la lista" para analizar el mismo libro con IA
2. Compara tu análisis reflexivo con el de Gemini
3. Profundiza con análisis de temas y conceptos
4. Obtén recomendaciones de libros similares
5. Descarga análisis para referencia futura

#### **Fase 5: Exploración (Búsqueda Inteligente)**
- Busca libros por tema (ej: "Amistad", "Justicia")
- Explora obras de autores favoritos
- Encuentra libros similares a los que leíste

---

## 🛠️ Tecnologías Utilizadas

| Herramienta | Versión | Propósito |
|---|---|---|
| **Python** | 3.12.8 | Lenguaje principal |
| **Streamlit** | 1.28+ | Framework web |
| **Google Gemini AI** | Gemini 2.0 Flash | Análisis con IA |
| **pytest** | 9.0.2 | Testing |
| **pytest-cov** | 7.0.0 | Cobertura de código |
| **python-dotenv** | 1.0.0 | Variables de entorno |

---

## 🛣️ Roadmap - Mejoras Futuras

- [ ] Expandir base de datos de libros (100+ libros)
- [ ] Autenticación de usuario y seguimiento de progreso
- [ ] Dashboard de estadísticas personales
- [ ] Características de comunidad (clubes de lectura, ratings)
- [ ] Exportación a PDF
- [ ] Soporte para idiomas adicionales
- [ ] Integración con Google Books API
- [ ] Versión de aplicación móvil
- [ ] Integración con podcasts

---

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver archivo `LICENSE` para más detalles.

## ⭐ ¡Si te gusta, déjanos una estrella en GitHub!

```
        📚
       /|\
        | 
       / \
     ThinkInk ⭐
```

---

**Versión:** 2.1  
**Última actualización:** 12 de Febrero de 2025  
**Estado de Tests:** ✅ Todos los tests pasando (3/3)  
**Documentación disponible en:** [English](README.md)
