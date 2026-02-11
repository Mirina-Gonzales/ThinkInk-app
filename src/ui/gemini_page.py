import streamlit as st
from src.services.gemini_service import GeminiService
from src.models.book import Book


def display_gemini_page(book: Book):
    """
    Página principal para consultar libros con Gemini
    
    Args:
        book: Libro a consultar
    """
    
    # Inicializar servicio
    gemini_service = GeminiService()
    
    # Verificar configuración
    if not gemini_service.is_configured():
        st.warning(
            "⚠️ **Gemini no está configurado**\n\n"
            "Para usar esta función, necesitas:\n"
            "1. Obtener una API key de [Google AI Studio](https://makersuite.google.com/app/apikey)\n"
            "2. Crear un archivo `.env` en la raíz del proyecto con:\n"
            "```\n"
            "GEMINI_API_KEY=tu_clave_aqui\n"
            "```\n"
            "3. Reiniciar la aplicación"
        )
        return
    
    # Header
    st.subheader("🤖 Consultas con Gemini AI")
    st.markdown("Obtén análisis profundos, resúmenes y recomendaciones sobre libros")
    
    # Detectar modo de búsqueda
    search_mode = st.session_state.get("search_mode", None)
    search_query = st.session_state.get("search_query", None)
    
    # Si es búsqueda inteligente
    if search_mode and search_query:
        if search_mode == "titles":
            # Búsqueda por título similar
            st.info(f"🔍 **Buscando libros similares a:** {search_query}")
            
            if st.button("🔎 Buscar libros similares", key="btn_search_titles"):
                with st.spinner("✨ Gemini está buscando libros similares..."):
                    results = gemini_service.search_similar_books(search_query)
                    st.markdown(results)
                    st.download_button(
                        label="⬇️ Descargar resultados",
                        data=results,
                        file_name=f"similares_a_{search_query.replace(' ', '_')}.txt",
                        mime="text/plain"
                    )
        
        elif search_mode == "author":
            # Búsqueda por autor
            st.info(f"👤 **Mejores obras de:** {search_query}")
            
            if st.button("👤 Ver mejores obras", key="btn_search_author"):
                with st.spinner("✨ Gemini está buscando las mejores obras..."):
                    results = gemini_service.search_author_works(search_query)
                    st.markdown(results)
                    st.download_button(
                        label="⬇️ Descargar resultados",
                        data=results,
                        file_name=f"obras_{search_query.replace(' ', '_')}.txt",
                        mime="text/plain"
                    )
    
    else:
        # Modo normal: tabs para análisis de un libro específico
        # Tabs para diferentes tipos de consultas
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
            ["📖 Resumen", "🎭 Temas y Personajes", "💡 Explicar Concepto", 
             "⭐ Recomendaciones", "❓ Preguntas de Discusión", "🔄 Comparar"]
        )
        
        # TAB 1: RESUMEN
        with tab1:
            st.write("Obtén un resumen detallado y análitico del libro")
            if st.button("📖 Generar resumen con Gemini", key="btn_summary"):
                with st.spinner("✨ Gemini está analizando el libro..."):
                    summary = gemini_service.get_book_summary(book)
                    st.markdown(summary)
                    st.download_button(
                        label="⬇️ Descargar resumen",
                        data=summary,
                        file_name=f"{book.title}_resumen.txt",
                        mime="text/plain"
                    )
        
        # TAB 2: TEMAS Y PERSONAJES
        with tab2:
            st.write("Analiza los temas centrales y personajes principales")
            if st.button("🎭 Analizar temas y personajes", key="btn_analysis"):
                with st.spinner("✨ Gemini está analizando..."):
                    analysis = gemini_service.analyze_themes_and_characters(book)
                    st.markdown(analysis)
                    st.download_button(
                        label="⬇️ Descargar análisis",
                        data=analysis,
                        file_name=f"{book.title}_analisis.txt",
                        mime="text/plain"
                    )
        
        # TAB 3: EXPLICAR CONCEPTO
        with tab3:
            st.write("Explica un concepto específico del libro")
            concept = st.text_input(
                "¿Qué concepto deseas entender?",
                placeholder="Ej: La alienación, El totalitarismo, El amor verdadero...",
                key="concept_input"
            )
            if st.button("💡 Explicar concepto", key="btn_explain"):
                if not concept.strip():
                    st.error("❌ Por favor, introduce un concepto para explicar")
                else:
                    with st.spinner("✨ Gemini está explicando..."):
                        explanation = gemini_service.explain_concept(book, concept)
                        st.markdown(explanation)
                        st.download_button(
                            label="⬇️ Descargar explicación",
                            data=explanation,
                            file_name=f"{book.title}_{concept.replace(' ', '_')}.txt",
                            mime="text/plain"
                        )
        
        # TAB 4: RECOMENDACIONES
        with tab4:
            st.write("Obtén recomendaciones de libros similares")
            interests = st.text_area(
                "Tus intereses (opcional)",
                placeholder="Ej: Historia, filosofía, romance, misterio...",
                height=100,
                key="interests_input"
            )
            if st.button("⭐ Obtener recomendaciones", key="btn_recommendations"):
                with st.spinner("✨ Gemini está buscando recomendaciones..."):
                    recommendations = gemini_service.get_book_recommendations(book, interests)
                    st.markdown(recommendations)
                    st.download_button(
                        label="⬇️ Descargar recomendaciones",
                        data=recommendations,
                        file_name=f"recomendaciones_para_{book.title}.txt",
                        mime="text/plain"
                    )
        
        # TAB 5: PREGUNTAS DE DISCUSIÓN
        with tab5:
            st.write("Genera preguntas profundas para discutir el libro")
            if st.button("❓ Generar preguntas de discusión", key="btn_questions"):
                with st.spinner("✨ Gemini está generando preguntas..."):
                    questions = gemini_service.generate_discussion_questions(book)
                    st.markdown(questions)
                    st.download_button(
                        label="⬇️ Descargar preguntas",
                        data=questions,
                        file_name=f"{book.title}_preguntas_discusion.txt",
                        mime="text/plain"
                    )
        
        # TAB 6: COMPARAR CON OTRO LIBRO
        with tab6:
            st.write("Compara este libro con otro de la biblioteca")
            from src.services.book_service import BookService
            
            service = BookService()
            all_books = service.get_all_books()
            book_titles = [b.title for b in all_books if b.id != book.id]
            
            selected_title = st.selectbox(
                "Elige otro libro para comparar",
                book_titles,
                key="compare_book"
            )
            
            if st.button("🔄 Comparar libros", key="btn_compare"):
                other_book = service.get_book_by_title(selected_title)
                if other_book:
                    with st.spinner("✨ Gemini está comparando los libros..."):
                        comparison = gemini_service.compare_books(book, other_book)
                        st.markdown(comparison)
                        st.download_button(
                            label="⬇️ Descargar comparación",
                            data=comparison,
                            file_name=f"comparacion_{book.title}_vs_{other_book.title}.txt",
                            mime="text/plain"
                        )


def display_gemini_setup_instructions():
    """Muestra instrucciones para configurar Gemini"""
    with st.expander("🔧 Cómo configurar Gemini API"):
        st.markdown("""
        ### Pasos para configurar Google Gemini:
        
        1. **Obtener API Key:**
           - Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
           - Haz clic en "Get API Key"
           - Copia tu API key
        
        2. **Crear archivo `.env`:**
           - En la raíz del proyecto, crea un archivo `.env`
           - Añade: `GEMINI_API_KEY=tu_clave_aqui`
        
        3. **Instalar dependencia (si no está):**
           ```bash
           pip install google-generativeai
           ```
        
        4. **Reiniciar la aplicación:**
           ```bash
           streamlit run app.py
           ```
        
        ✅ ¡Listo! Ahora puedes usar todas las funciones de Gemini.
        """)
