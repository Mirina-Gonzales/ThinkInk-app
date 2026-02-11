# 📚 ThinkInk App

Una aplicación web interactiva para mejorar tu experiencia de lectura con preguntas reflexivas, información de autores y seguimiento de aprendizaje. Construida con Python y Streamlit.

## ✨ Características

- 📖 **Preguntas Previas** - Prepárate antes de leer cada libro
- 💭 **Preguntas Finales** - Reflexiona sobre lo que aprendiste  
- 🖊️ **Fichas de Autor** - Conoce más sobre los creadores
- 📚 **10 Libros Clásicos** - Selección inicial curada
- 🎨 **Interfaz Intuitiva** - Construida con Streamlit
- ✅ **Pruebas Unitarias** - 3/3 tests pasando
- 📊 **Coverage de 84%** - Código bien testeado

## 📁 Estructura del Proyecto

```
ThinkInk-app/
├── app.py                          # Aplicación principal Streamlit
├── config/
│   └── settings.py                # Configuración global (100% coverage)
├── data/
│   └── books.json                 # 10 libros con preguntas y bios
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   └── book.py                # Clase Book (94% coverage)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── book_service.py        # Gestión de libros (68% coverage)
│   │   ├── question_service.py    # Gestión de preguntas
│   │   └── author_service.py      # Información de autores
│   └── ui/
│       ├── __init__.py
│       └── pages.py               # Componentes UI reutilizables
├── tests/
│   ├── __init__.py
│   ├── test_book_service.py       # Tests unitarios (97% coverage)
│   └── test_question_service.py   # Tests adicionales (placeholder)
├── htmlcov/                       # Reporte HTML de coverage
├── venv/                          # Entorno virtual
├── .gitignore                     # Archivos ignorados en Git
├── requirements.txt               # Dependencias del proyecto
└── README.md                      # Esta documentación
```

---

## 📦 Módulos Creados

### 1️⃣ `config/settings.py` (100% Coverage ✅)

**Propósito:** Configuración centralizada de la aplicación

```python
# Variables exportadas:
BASE_DIR              # Ruta base del proyecto
DATA_DIR             # Ruta a carpeta de datos
BOOKS_FILE           # Ruta al archivo books.json
STREAMLIT_CONFIG     # Configuración de página Streamlit
```

**Ejemplo de uso:**
```python
from config.settings import BOOKS_FILE, STREAMLIT_CONFIG

st.set_page_config(**STREAMLIT_CONFIG)
```

---

### 2️⃣ `src/models/book.py` (94% Coverage 📈)

**Propósito:** Modelo de datos para libros

**Clase `Book`:**
```python
@dataclass
class Book:
    id: int                      # ID único del libro
    title: str                   # Título del libro
    author: str                  # Nombre del autor
    description: str             # Descripción breve
    year: int                    # Año de publicación
    genre: str                   # Género literario
    pre_questions: List[str]     # 3 preguntas antes de leer
    post_questions: List[str]    # 3 preguntas después de leer
    author_bio: str              # Biografía del autor
```

**Métodos:**
- `to_dict()` - Convierte el libro a diccionario (JSON)
- `from_dict(data)` - Crea un libro desde diccionario (desserialización)

**Ejemplo de uso:**
```python
from src.models.book import Book

# Crear instancia
book = Book(
    id=1,
    title="1984",
    author="George Orwell",
    description="Una novela distópica...",
    year=1949,
    genre="Distopía",
    pre_questions=["¿Qué entiendes por totalitarismo?"],
    post_questions=["¿Cómo cambió tu perspectiva?"],
    author_bio="George Orwell (1903-1950)..."
)

# Convertir a diccionario
book_dict = book.to_dict()

# Crear desde diccionario
new_book = Book.from_dict(book_dict)
```

---

### 3️⃣ `src/services/book_service.py` (68% Coverage 📝)

**Propósito:** Gestión completa de libros (CRUD)

**Clase `BookService`:**
```python
class BookService:
    def __init__(self, books_file: Path = BOOKS_FILE)
    def _load_books() -> List[Book]           # Carga desde JSON
    def get_all_books() -> List[Book]         # Obtiene todos
    def get_book_by_id(book_id: int) -> Book  # Busca por ID
    def get_book_by_title(title: str) -> Book # Busca por título
    def get_books_by_genre(genre: str) -> List[Book]  # Filtra por género
    def add_book(book: Book) -> bool          # Añade nuevo libro
    def save_books()                          # Persiste cambios
```

**Ejemplo de uso:**
```python
from src.services.book_service import BookService

# Instanciar servicio (carga automáticamente desde books.json)
service = BookService()

# Obtener todos los libros
all_books = service.get_all_books()  # Retorna: List[Book]

# Buscar por ID
book = service.get_book_by_id(1)  # Retorna: Book | None
# Output: Book(id=1, title="1984", author="George Orwell", ...)

# Buscar por título
book = service.get_book_by_title("1984")  # Case-insensitive
# Output: Book(id=1, title="1984", ...)

# Obtener libros por género
books = service.get_books_by_genre("Distopía")  # Retorna: List[Book]
# Output: [Book(...), Book(...)]

# Agregar nuevo libro
new_book = Book(
    id=11, title="New Book", author="Author",
    description="...", year=2025, genre="Fiction",
    pre_questions=["Q1"], post_questions=["Q2"],
    author_bio="Bio"
)
success = service.add_book(new_book)  # Retorna: bool (True si se agregó)
```

---

### 4️⃣ `src/services/question_service.py`

**Propósito:** Gestión de preguntas de lectura

**Clase `QuestionService` (métodos estáticos):**
```python
class QuestionService:
    @staticmethod
    def get_pre_questions(book: Book) -> List[str]
    # Obtiene preguntas previas

    @staticmethod
    def get_post_questions(book: Book) -> List[str]
    # Obtiene preguntas posteriores

    @staticmethod
    def format_questions_for_display(questions: List[str]) -> str
    # Formatea preguntas con bullets (•)

    @staticmethod
    def evaluate_answers(answers: Dict[str, str]) -> Dict
    # Analiza respuestas del usuario
```

**Ejemplo de uso:**
```python
from src.services.question_service import QuestionService

# Obtener preguntas
pre_q = QuestionService.get_pre_questions(book)
# Retorna: ["¿Qué entiendes por totalitarismo?", ...]

# Formatear para mostrar
formatted = QuestionService.format_questions_for_display(pre_q)
# Retorna: "• ¿Qué entiendes por totalitarismo?\n• ..."

# Evaluar respuestas
answers = {"1": "Mi respuesta...", "2": "Otra respuesta..."}
evaluation = QuestionService.evaluate_answers(answers)
# Retorna: {"total_questions": 2, "answered": 2}
```

---

### 5️⃣ `src/services/author_service.py`

**Propósito:** Información de autores

**Clase `AuthorService` (métodos estáticos):**
```python
class AuthorService:
    @staticmethod
    def get_author_bio(book: Book) -> str
    # Obtiene biografía del autor

    @staticmethod
    def format_author_info(book: Book) -> str
    # Formatea en Markdown para mostrar
```

**Ejemplo de uso:**
```python
from src.services.author_service import AuthorService

# Obtener biografía
bio = AuthorService.get_author_bio(book)
# Retorna: "George Orwell (1903-1950) fue un escritor británico..."

# Formatear para Streamlit
formatted_bio = AuthorService.format_author_info(book)
# Retorna: "### 🖊️ Sobre el Autor\n**George Orwell**\n\nGeorge Orwell..."

# Usar en app
st.markdown(formatted_bio)
```

---

### 6️⃣ `src/ui/pages.py`

**Propósito:** Componentes UI reutilizables

**Funciones:**
```python
def display_book_card(book: Book)
# Muestra tarjeta de libro con año, género, descripción

def display_author_section(book: Book)
# Muestra sección completa del autor

def display_questions(questions: list, question_type: str) -> dict
# Renderiza preguntas interactivas y retorna respuestas
```

**Ejemplo de uso:**
```python
from src.ui.pages import display_book_card, display_questions

# Mostrar tarjeta
display_book_card(book)

# Mostrar preguntas
answers = display_questions(book.pre_questions, "Preguntas Previas")
# Retorna: {"1": "respuesta1", "2": "respuesta2", ...}
```

---

### 7️⃣ `app.py` - Aplicación Streamlit

**Propósito:** Interfaz web principal

**Funcionalidades:**
- 📖 Página de información del libro (año, género, descripción)
- ❓ Pestaña de preguntas previas (antes de leer)
- ✅ Pestaña de preguntas finales (después de leer)
- 🖊️ Pestaña de autor con biografía

**Estructura:**
```
┌─────────────────────────────────────────┐
│        📚 ThinkInk - Aplicación         │
│   de Preguntas sobre Libros             │
├─────────────┬───────────────────────────┤
│ 📖 Sidebar  │   Contenido Principal     │
│             │   ┌─────────────────────┐ │
│ Selecciona  │   │ Tabs:               │ │
│ un libro    │   │ • 📘 Información    │ │
│             │   │ • ❓ Preguntas Prev │ │
│ Dropdown    │   │ • ✅ Preguntas Fin  │ │
│ con 10      │   │ • 🖊️ Autor          │ │
│ libros      │   └─────────────────────┘ │
└─────────────┴───────────────────────────┘
```

**Flujo de usuario:**
1. Selecciona libro del sidebar
2. Ve información en pestaña "Información"
3. Responde preguntas previas (tab "Preguntas Previas")
4. Lee el libro
5. Responde preguntas finales (tab "Preguntas Finales")
6. Lee biografía del autor (tab "Autor")

---

### 8️⃣ `data/books.json`

**Propósito:** Almacenamiento de 10 libros clásicos

**Estructura de cada libro:**
```json
{
  "id": 1,
  "title": "1984",
  "author": "George Orwell",
  "description": "Una novela distópica sobre un régimen totalitario...",
  "year": 1949,
  "genre": "Distopía",
  "pre_questions": [
    "¿Qué entiendes por totalitarismo?",
    "¿Cómo crees que afecta la vigilancia...",
    "¿Es posible que la verdad sea relativa?"
  ],
  "post_questions": [
    "¿Cómo cambió tu perspectiva...",
    "¿Ves similitudes entre el mundo...",
    "¿Qué personaje te impactó más..."
  ],
  "author_bio": "George Orwell (1903-1950) fue un escritor británico..."
}
```

**Libros incluidos:**
1. 1984 - George Orwell
2. El Quijote - Miguel de Cervantes
3. Orgullo y Prejuicio - Jane Austen
4. El Señor de los Anillos - J.R.R. Tolkien
5. Crimen y Castigo - Fiódor Dostoievski
6. Jane Eyre - Charlotte Brontë
7. Cien Años de Soledad - Gabriel García Márquez
8. La Metamorfosis - Franz Kafka
9. El Gran Gatsby - F. Scott Fitzgerald
10. Mujercitas - Louisa May Alcott

---

### 9️⃣ `tests/test_book_service.py` (97% Coverage ✅)

**Propósito:** Tests unitarios para BookService

**Tests implementados:**
```python
class TestBookService(unittest.TestCase):
    def setUp()              # Prepara datos de prueba
    def tearDown()           # Limpia recursos
    def test_load_books()    # ✅ Carga correcta
    def test_get_book_by_id()    # ✅ Búsqueda por ID
    def test_get_book_by_title() # ✅ Búsqueda por título
```

**Resultados:**
```
Ran 3 tests in 0.001s
OK
```

---

## 🔧 Instalación y Setup

### Requisitos previos
- Python 3.8+
- pip (gestor de paquetes)

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/TU_USUARIO/ThinkInk-app.git
cd ThinkInk-app
```

### Paso 2: Crear entorno virtual
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Paso 3: Instalar dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Dependencias instaladas:**
- streamlit==1.36.0 - Framework web
- python-dotenv==1.0.0 - Variables de entorno

---

## 🚀 Uso

### Ejecutar la aplicación
```bash
source venv/bin/activate  # Activar entorno
streamlit run app.py      # Iniciar app
```

La aplicación se abrirá en: **http://localhost:8501**

### Interfaz de usuario

#### 📖 Pestaña "Información"
Muestra:
- Título del libro
- Año de publicación
- Género literario
- Descripción completa
- Métricas adicionales

#### ❓ Pestaña "Preguntas Previas"
- 3 preguntas para responder ANTES de leer
- Área de texto expandible para cada respuesta
- Botón "Guardar respuestas previas"

#### ✅ Pestaña "Preguntas Finales"
- 3 preguntas para responder DESPUÉS de leer
- Reflexión sobre lo aprendido
- Botón "Guardar respuestas finales"

#### 🖊️ Pestaña "Autor"
- Biografía del escritor
- Datos adicionales (años de vida, país, etc.)
- Expandible con más estadísticas

---

## ✅ Pruebas y Quality Assurance

### Ejecutar todas las pruebas
```bash
source venv/bin/activate
python3 -m unittest discover -s tests -p "test_*.py" -v
```

**Output esperado:**
```
test_load_books ... ok
test_get_book_by_id ... ok
test_get_book_by_title ... ok

Ran 3 tests in 0.001s
OK
```

### Ver reporte de cobertura

#### Opción 1: Reporte en terminal
```bash
python3 -m coverage run -m unittest discover -s tests
python3 -m coverage report
```

**Output:**
```
Name                              Stmts   Miss  Cover
─────────────────────────────────────────────────────
config/settings.py                   6      0   100%  ✅
src/models/book.py                  18      1    94%   📈
src/services/book_service.py        40     13    68%   📝
tests/test_book_service.py          30      1    97%   ✅
─────────────────────────────────────────────────────
TOTAL                               94     15    84%
```

#### Opción 2: Reporte HTML
```bash
python3 -m coverage html
open htmlcov/index.html  # macOS
# o abre htmlcov/index.html en tu navegador
```

### Métricas actuales
- ✅ **100%** - config/settings.py
- 📈 **97%** - tests/test_book_service.py
- 📈 **94%** - src/models/book.py
- 📝 **68%** - src/services/book_service.py
- 📊 **84%** - TOTAL

---

## 📝 Ejemplos de uso en código

### Cargar y mostrar un libro
```python
from src.services.book_service import BookService
from src.ui.pages import display_book_card

service = BookService()
book = service.get_book_by_id(1)

if book:
    display_book_card(book)
```

### Obtener preguntas y formatearlas
```python
from src.services.question_service import QuestionService

questions = QuestionService.get_pre_questions(book)
formatted = QuestionService.format_questions_for_display(questions)
print(formatted)
```

### Procesar respuestas
```python
answers = {"1": "Respuesta 1", "2": "Respuesta 2", "3": ""}
evaluation = QuestionService.evaluate_answers(answers)
print(f"Respondidas: {evaluation['answered']}/{evaluation['total_questions']}")
```

---

## 🎯 Roadmap (Próximas Fases)

- [ ] **Fase 2:** Guardar respuestas en base de datos (SQLite/PostgreSQL)
- [ ] **Fase 3:** Panel de progreso de lectura
- [ ] **Fase 4:** Sistema de recomendaciones basado en géneros favoritos
- [ ] **Fase 5:** Rankings de usuarios y tablero de líderes
- [ ] **Fase 6:** Integración con APIs de libros (Google Books, Open Library)
- [ ] **Fase 7:** Exportar respuestas en PDF
- [ ] **Fase 8:** Múltiples idiomas
- [ ] **Fase 9:** Notas y subrayados dentro de la app
- [ ] **Fase 10:** Compartir resúmenes con otros usuarios

---

## 📂 Archivos de configuración

### `requirements.txt`
```
streamlit==1.36.0
python-dotenv==1.0.0
```

### `.gitignore`
```
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.vscode/
.DS_Store
*.pyc
.streamlit/
```

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. **Fork** el proyecto
2. **Crea una rama** para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre un Pull Request**

### Convenciones de código
- Usa PEP 8 para Python
- Comenta código complejo
- Mantén la cobertura de tests >= 80%
- Actualiza el README con nuevas features

---

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver `LICENSE` para más detalles.

---

## 💬 Soporte y Contacto

- 📧 **Email:** contacto@thinkink-app.com
- 🐙 **GitHub Issues:** Para reportar bugs o sugerencias
- 💡 **Discussions:** Para preguntas y sugerencias generales

---

## 📊 Estadísticas del Proyecto

| Métrica | Valor |
|---------|-------|
| **Archivos Python** | 12 |
| **Líneas de código** | ~500 |
| **Tests** | 3 |
| **Coverage** | 84% |
| **Dependencias** | 2 directas |
| **Libros** | 10 |
| **Preguntas totales** | 60 |
| **Biografías** | 10 |

---

## 🎓 Conceptos utilizados

- **Dataclasses** - Modelos de datos con `@dataclass`
- **Servicios** - Capa de lógica de negocio
- **CRUD Operations** - Create, Read, Update, Delete
- **Unittest** - Testing framework de Python
- **Coverage** - Análisis de cobertura de tests
- **JSON** - Persistencia de datos
- **Streamlit** - Framework web interactivo
- **Pathlib** - Manejo de rutas multiplataforma

---

**ThinkInk - Hecho con ❤️ para amantes de la lectura**

Última actualización: Febrero 2026
