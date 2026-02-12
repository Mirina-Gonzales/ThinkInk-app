import os
from typing import Optional
from dotenv import load_dotenv
import google.generativeai as genai
from src.models.book import Book

# Cargar variables de entorno
load_dotenv()


class GeminiService:
    """Servicio para consultar libros usando Google Gemini API"""

    def __init__(self, api_key: Optional[str] = None):
        """
        Inicializa el servicio de Gemini
        
        Args:
            api_key: Clave de API de Google Gemini (si no se proporciona, 
                     se obtiene de la variable de entorno GEMINI_API_KEY)
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel("gemini-2.0-flash")
        else:
            self.model = None

    def is_configured(self) -> bool:
        """Verifica si Gemini está configurado"""
        return self.model is not None

    def get_book_summary(self, book: Book) -> str:
        """
        Obtiene un resumen análitico del libro usando Gemini
        
        Args:
            book: Libro a resumir
            
        Returns:
            Resumen del libro generado por Gemini
        """
        if not self.is_configured():
            return "⚠️ Gemini no está configurado. Por favor, proporciona tu API_KEY."

        prompt = f"""
        IMPORTANTE: Verifica primero que "{book.title}" es UN LIBRO (novela, ensayo, poesía, etc.).
        Si NO es un libro (es película, serie, videojuego, etc.), responde:
        "❌ Lo siento, solo analizo LIBROS. '{book.title}' no es un libro. Por favor, ingresa un libro válido."
        
        Si ES un libro, proporciona un resumen detallado y analítico de "{book.title}" 
        escrito por {book.author} ({book.year}).
        
        Género: {book.genre}
        Tema principal: {book.theme}
        Descripción: {book.description}
        
        RESTRICCIONES IMPORTANTES:
        - NO utilices lenguaje ofensivo, discriminatorio o que promueva el odio
        - NO hagas referencias negativas hacia grupos de personas, razas, géneros, religiones o orientaciones sexuales
        - Mantén un tono académico y respetuoso
        
        Por favor incluye:
        - Resumen del argumento (2-3 párrafos)
        - Temas principales
        - Significancia literaria
        - Público objetivo
        
        Sé conciso pero informativo.
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error al consultar Gemini: {str(e)}"

    def analyze_themes_and_characters(self, book: Book) -> str:
        """
        Analiza temas y personajes principales del libro
        
        Args:
            book: Libro a analizar
            
        Returns:
            Análisis de temas y personajes
        """
        if not self.is_configured():
            return "⚠️ Gemini no está configurado. Por favor, proporciona tu API_KEY."

        prompt = f"""
        IMPORTANTE: Verifica que "{book.title}" es UN LIBRO. Si no lo es, rechaza el análisis.
        
        Analiza en profundidad el libro "{book.title}" de {book.author}.
        
        Tema principal: {book.theme}
        
        RESTRICCIONES IMPORTANTES:
        - NO utilices lenguaje ofensivo, discriminatorio o que promueva el odio
        - NO hagas referencias negativas hacia grupos de personas
        - Mantén un tono académico y respetuoso
        
        Por favor incluye:
        1. **Personajes Principales**: Nombres y características clave
        2. **Temas Centrales**: Ideas principales del libro
        3. **Conflictos**: Tensiones narrativas principales
        4. **Simbolismo**: Elementos simbólicos importantes
        5. **Impacto Cultural**: Influencia en la literatura
        
        Mantén el análisis estructurado y claro.
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error al consultar Gemini: {str(e)}"

    def get_book_recommendations(self, book: Book, interests: str = "") -> str:
        """
        Obtiene recomendaciones basadas en el libro actual
        
        Args:
            book: Libro de referencia
            interests: Intereses adicionales del usuario
            
        Returns:
            Recomendaciones de libros similares
        """
        if not self.is_configured():
            return "⚠️ Gemini no está configurado. Por favor, proporciona tu API_KEY."

        prompt = f"""
        Basándote en el libro "{book.title}" de {book.author} (Género: {book.genre}),
        proporciona recomendaciones de libros similares.
        
        Intereses del usuario: {interests if interests else 'No especificados'}
        
        Por favor:
        1. Recomienda 5 libros similares
        2. Explica por qué son relevantes
        3. Sugiere libros del mismo autor si existen
        4. Indica el nivel de dificultad de lectura
        
        Formatea la respuesta de manera clara y útil.
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error al consultar Gemini: {str(e)}"

    def explain_concept(self, book: Book, concept: str) -> str:
        """
        Explica un concepto específico del libro
        
        Args:
            book: Libro del cual explicar el concepto
            concept: Concepto a explicar
            
        Returns:
            Explicación detallada del concepto
        """
        if not self.is_configured():
            return "⚠️ Gemini no está configurado. Por favor, proporciona tu API_KEY."

        prompt = f"""
        IMPORTANTE: Verifica que "{book.title}" es UN LIBRO. Si no lo es, rechaza el análisis.
        
        Explica el concepto o tema "{concept}" en el contexto del libro 
        "{book.title}" de {book.author}.
        
        Tema principal del libro: {book.theme}
        
        RESTRICCIONES IMPORTANTES:
        - NO utilices lenguaje ofensivo, discriminatorio o que promueva el odio
        - Mantén un tono académico y respetuoso
        
        Por favor:
        1. Define el concepto claramente
        2. Muestra cómo aparece en el libro
        3. Explica su importancia en la trama
        4. Proporciona ejemplos específicos del texto
        5. Relaciona con el contexto histórico/cultural si es relevante
        
        Mantén la explicación accesible pero profunda.
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error al consultar Gemini: {str(e)}"

    def compare_books(self, book1: Book, book2: Book) -> str:
        """
        Compara dos libros
        
        Args:
            book1: Primer libro
            book2: Segundo libro
            
        Returns:
            Comparación detallada de los libros
        """
        if not self.is_configured():
            return "⚠️ Gemini no está configurado. Por favor, proporciona tu API_KEY."

        prompt = f"""
        Compara detalladamente los libros:
        
        Libro 1: "{book1.title}" por {book1.author} ({book1.year})
        Género: {book1.genre}
        
        Libro 2: "{book2.title}" por {book2.author} ({book2.year})
        Género: {book2.genre}
        
        Por favor:
        1. Similitudes temáticas
        2. Diferencias en estilo y narrativa
        3. Contexto histórico de cada uno
        4. Influencia mutua (si la hay)
        5. Cuál recomendar según preferencias
        
        Sé equilibrado en la comparación.
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error al consultar Gemini: {str(e)}"

    def generate_discussion_questions(self, book: Book) -> str:
        """
        Genera preguntas de discusión para el libro
        
        Args:
            book: Libro para el cual generar preguntas
            
        Returns:
            Preguntas de discusión
        """
        if not self.is_configured():
            return "⚠️ Gemini no está configurado. Por favor, proporciona tu API_KEY."

        prompt = f"""
        IMPORTANTE: Verifica que "{book.title}" es UN LIBRO. Si no lo es, rechaza el análisis.
        
        Genera preguntas de discusión profundas para el libro "{book.title}" 
        de {book.author}.
        
        Tema principal: {book.theme}
        
        RESTRICCIONES IMPORTANTES:
        - NO crees preguntas que inciten a lenguaje ofensivo o discriminatorio
        - Las preguntas deben ser inclusivas y respetuosas
        - Mantén un tono académico
        
        Las preguntas deben:
        1. Explorar temas principales
        2. Invitar a reflexión personal
        3. Conectar con experiencias del lector
        4. Ser desafiantes pero accesibles
        5. Promover debate constructivo
        
        Proporciona 8-10 preguntas bien formuladas.
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error al consultar Gemini: {str(e)}"

    def search_similar_books(self, title: str) -> str:
        """
        Busca libros similares basado en un título dado
        
        Args:
            title: Título del libro para buscar similares
            
        Returns:
            Top 3 libros similares con análisis
        """
        if not self.is_configured():
            return "⚠️ Gemini no está configurado. Por favor, proporciona tu API_KEY."

        prompt = f"""
        IMPORTANTE: Verifica que "{title}" es UN LIBRO. Si no lo es, responde:
        "❌ Lo siento, solo analizo LIBROS. '{title}' no es un libro."
        
        Si es un libro, basándote en él, proporciona un análisis de 
        los 3 LIBROS MÁS SIMILARES.
        
        RESTRICCIONES IMPORTANTES:
        - Solo menciona LIBROS (novelas, ensayos, etc.)
        - NO utilices lenguaje ofensivo o discriminatorio
        - Mantén un tono respetuoso
        
        Para cada uno de los 3 libros, incluye:
        1. **Título y Autor**
        2. **Año de publicación**
        3. **Género**
        4. **Por qué es similar** - Explicación clara de similitudes temáticas, 
           narrativas o de estilo
        5. **Sinopsis breve** (2-3 líneas)
        
        Formatea la respuesta de manera clara y estructurada.
        Usa emojis para hacer más legible.
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error al consultar Gemini: {str(e)}"

    def search_author_works(self, author: str) -> str:
        """
        Busca las mejores obras de un autor de libros
        
        Args:
            author: Nombre del autor
            
        Returns:
            Top 3 libros del autor con análisis
        """
        if not self.is_configured():
            return "⚠️ Gemini no está configurado. Por favor, proporciona tu API_KEY."

        prompt = f"""
        IMPORTANTE: Verifica que "{author}" es un AUTOR DE LIBROS. 
        Si es director de cine, compositor, músico, dramaturgo o cualquier otra cosa 
        (pero NO autor de libros), responde:
        "❌ Lo siento, solo analizo LIBROS. '{author}' no es un autor de libros. 
        Por favor, ingresa el nombre de un autor de libros válido."
        
        Si es un autor de libros, proporciona un análisis de los 3 MEJORES LIBROS de {author}.
        
        RESTRICCIONES IMPORTANTES:
        - Solo menciona LIBROS (novelas, ensayos, poesía, etc.)
        - NO utilices lenguaje ofensivo o discriminatorio
        - Mantén un tono respetuoso
        
        Para cada libro, incluye:
        1. **Título**
        2. **Año de publicación**
        3. **Género**
        4. **Por qué es destacada** - Lo que la hace especial y representativa del autor
        5. **Sinopsis breve** (2-3 líneas)
        6. **Tema principal**
        
        Formatea la respuesta de manera clara y estructurada.
        Usa emojis para hacer más legible.
        Sé preciso: solo 3 libros, ordenados por importancia/popularidad.
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error al consultar Gemini: {str(e)}"

    def search_books_by_theme(self, theme: str) -> str:
        """
        Busca libros que tratan un tema específico
        
        Args:
            theme: Tema a buscar (ej: Amistad, Justicia, Identidad)
            
        Returns:
            Top 3 libros que abordan ese tema
        """
        if not self.is_configured():
            return "⚠️ Gemini no está configurado. Por favor, proporciona tu API_KEY."

        prompt = f"""
        Proporciona recomendaciones de los 3 MEJORES LIBROS que abordan el tema: "{theme}"
        
        RESTRICCIONES IMPORTANTES:
        - Solo menciona LIBROS (novelas, ensayos, poesía, etc.)
        - NO utilices lenguaje ofensivo o discriminatorio
        - Mantén un tono respetuoso e inclusivo
        
        Para cada uno de los 3 libros, incluye:
        1. **Título y Autor**
        2. **Año de publicación**
        3. **Género**
        4. **Cómo aborda el tema** - Explicación de cómo el libro trata el tema "{theme}"
        5. **Sinopsis breve** (2-3 líneas)
        6. **Por qué recomendarlo** - Lo que lo hace especial para este tema
        
        Formatea la respuesta de manera clara y estructurada.
        Usa emojis para hacer más legible.
        Sé preciso: solo 3 libros, ordenados por relevancia al tema.
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error al consultar Gemini: {str(e)}"
