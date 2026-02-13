import streamlit as st
from src.services.gemini_service import GeminiService
from src.models.book import Book
from src.i18n.i18n_service import t


def display_gemini_page(book: Book, lang: str = "es"):
    """
    Página principal para consultar libros con Gemini
    
    Args:
        book: Libro a consultar
        lang: Idioma (es/en)
    """
    
    # Inicializar servicio
    gemini_service = GeminiService()
    
    # Verificar configuración
    if not gemini_service.is_configured():
        warning_text = "⚠️ **Gemini no está configurado**\n\n"
        if lang == "es":
            warning_text += ("Para usar esta función, necesitas:\n"
                           "1. Obtener una API key de [Google AI Studio](https://makersuite.google.com/app/apikey)\n"
                           "2. Crear un archivo `.env` en la raíz del proyecto con:\n"
                           "```\n"
                           "GEMINI_API_KEY=tu_clave_aqui\n"
                           "```\n"
                           "3. Reiniciar la aplicación")
        else:
            warning_text += ("To use this feature, you need:\n"
                           "1. Get an API key from [Google AI Studio](https://makersuite.google.com/app/apikey)\n"
                           "2. Create a `.env` file in the project root with:\n"
                           "```\n"
                           "GEMINI_API_KEY=your_key\n"
                           "```\n"
                           "3. Restart the application")
        st.warning(warning_text)
        return
    
    # Header
    header_text = "🤖 " + ("Consultas con Gemini AI" if lang == "es" else "Gemini AI Queries")
    st.subheader(header_text)
    subtitle = "Obtén análisis profundos, resúmenes y recomendaciones sobre libros" if lang == "es" else "Get deep analysis, summaries and recommendations about books"
    st.markdown(subtitle)
    
    # Detectar modo de búsqueda
    search_mode = st.session_state.get("search_mode", None)
    search_query = st.session_state.get("search_query", None)
    
    # Si es búsqueda inteligente
    if search_mode and search_query:
        if search_mode == "titles":
            # Búsqueda por título similar
            searching_msg = f"🔍 **{'Buscando libros similares a:' if lang == 'es' else 'Searching for books similar to:'} {search_query}"
            st.info(searching_msg)
            
            btn_label = "🔎 " + ("Buscar libros similares" if lang == "es" else "Search for similar books")
            download_label = "⬇️ " + ("Descargar resultados" if lang == "es" else "Download results")
            spinner_msg = ("✨ Gemini está buscando libros similares..." if lang == "es" 
                          else "✨ Gemini is searching for similar books...")
            
            if st.button(btn_label, key="btn_search_titles"):
                with st.spinner(spinner_msg):
                    results = gemini_service.search_similar_books(search_query, lang)
                    st.markdown(results)
                    st.download_button(
                        label=download_label,
                        data=results,
                        file_name=f"similares_a_{search_query.replace(' ', '_')}.txt",
                        mime="text/plain"
                    )
        
        elif search_mode == "author":
            # Búsqueda por autor
            searching_msg = f"👤 **{'Mejores obras de:' if lang == 'es' else 'Best works by:'} {search_query}"
            st.info(searching_msg)
            
            btn_label = "👤 " + ("Ver mejores obras" if lang == "es" else "View best works")
            download_label = "⬇️ " + ("Descargar resultados" if lang == "es" else "Download results")
            spinner_msg = ("✨ Gemini está buscando las mejores obras..." if lang == "es"
                          else "✨ Gemini is searching for the best works...")
            
            if st.button(btn_label, key="btn_search_author"):
                with st.spinner(spinner_msg):
                    results = gemini_service.search_author_works(search_query, lang)
                    st.markdown(results)
                    st.download_button(
                        label=download_label,
                        data=results,
                        file_name=f"obras_{search_query.replace(' ', '_')}.txt",
                        mime="text/plain"
                    )
        
        elif search_mode == "theme":
            # Búsqueda por tema
            searching_msg = f"🎯 **{'Libros sobre el tema:' if lang == 'es' else 'Books about the topic:'} {search_query}"
            st.info(searching_msg)
            
            btn_label = "🎯 " + ("Buscar libros por tema" if lang == "es" else "Search books by theme")
            download_label = "⬇️ " + ("Descargar resultados" if lang == "es" else "Download results")
            spinner_msg = ("✨ Gemini está buscando libros sobre este tema..." if lang == "es"
                          else "✨ Gemini is searching for books on this topic...")
            
            if st.button(btn_label, key="btn_search_theme"):
                with st.spinner(spinner_msg):
                    results = gemini_service.search_books_by_theme(search_query, lang)
                    st.markdown(results)
                    st.download_button(
                        label=download_label,
                        data=results,
                        file_name=f"libros_sobre_{search_query.replace(' ', '_')}.txt",
                        mime="text/plain"
                    )
    
    else:
        # Modo normal: tabs para análisis de un libro específico
        # Tabs para diferentes tipos de consultas
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
            [t("gemini_tab_summary", lang), 
             t("gemini_tab_themes", lang), 
             t("gemini_tab_concept", lang), 
             t("gemini_tab_recommendations", lang), 
             t("gemini_tab_questions", lang), 
             t("gemini_tab_compare", lang)]
        )
        
        # TAB 1: RESUMEN
        with tab1:
            st.write(t("summary_desc", lang))
            if st.button(t("btn_summary", lang), key="btn_summary"):
                with st.spinner("✨ Gemini está analizando el libro..."):
                    summary = gemini_service.get_book_summary(book, lang)
                    st.markdown(summary)
                    st.download_button(
                        label=t("download_summary", lang),
                        data=summary,
                        file_name=f"{book.title}_resumen.txt",
                        mime="text/plain"
                    )
        
        # TAB 2: TEMAS Y PERSONAJES
        with tab2:
            st.write(t("themes_desc", lang))
            if st.button(t("btn_analysis", lang), key="btn_analysis"):
                with st.spinner("✨ Gemini está analizando..."):
                    analysis = gemini_service.analyze_themes_and_characters(book, lang)
                    st.markdown(analysis)
                    st.download_button(
                        label=t("download_analysis", lang),
                        data=analysis,
                        file_name=f"{book.title}_analisis.txt",
                        mime="text/plain"
                    )
        
        # TAB 3: EXPLICAR CONCEPTO
        with tab3:
            st.write(t("concept_desc", lang))
            concept = st.text_input(
                t("concept_input", lang),
                placeholder=t("concept_placeholder", lang),
                key="concept_input"
            )
            if st.button(t("btn_explain", lang), key="btn_explain"):
                if not concept.strip():
                    st.error(t("concept_error", lang))
                else:
                    with st.spinner("✨ Gemini está explicando..."):
                        explanation = gemini_service.explain_concept(book, concept, lang)
                        st.markdown(explanation)
                        st.download_button(
                            label=t("download_explanation", lang),
                            data=explanation,
                            file_name=f"{book.title}_{concept.replace(' ', '_')}.txt",
                            mime="text/plain"
                        )
        
        # TAB 4: RECOMENDACIONES
        with tab4:
            st.write(t("recommendations_desc", lang))
            interests = st.text_area(
                t("interests_input", lang),
                placeholder=t("interests_placeholder", lang),
                height=100,
                key="interests_input"
            )
            if st.button(t("btn_recommendations", lang), key="btn_recommendations"):
                with st.spinner("✨ Gemini está buscando recomendaciones..."):
                    recommendations = gemini_service.get_book_recommendations(book, interests, lang)
                    st.markdown(recommendations)
                    st.download_button(
                        label=t("download_recommendations", lang),
                        data=recommendations,
                        file_name=f"recomendaciones_para_{book.title}.txt",
                        mime="text/plain"
                    )
        
        # TAB 5: PREGUNTAS DE DISCUSIÓN
        with tab5:
            st.write(t("questions_desc", lang))
            if st.button(t("btn_questions", lang), key="btn_questions"):
                with st.spinner("✨ Gemini está generando preguntas..."):
                    questions = gemini_service.generate_discussion_questions(book, lang)
                    st.markdown(questions)
                    st.download_button(
                        label=t("download_questions", lang),
                        data=questions,
                        file_name=f"{book.title}_preguntas_discusion.txt",
                        mime="text/plain"
                    )
        
        # TAB 6: COMPARAR CON OTRO LIBRO
        with tab6:
            st.write(t("compare_desc", lang))
            from src.services.book_service import BookService
            
            service = BookService(lang=lang)
            all_books = service.get_all_books()
            book_titles = [b.title for b in all_books if b.id != book.id]
            
            selected_title = st.selectbox(
                t("compare_book", lang),
                book_titles,
                key="compare_book"
            )
            
            if st.button(t("btn_compare", lang), key="btn_compare"):
                other_book = service.get_book_by_title(selected_title)
                if other_book:
                    with st.spinner("✨ Gemini está comparando los libros..."):
                        comparison = gemini_service.compare_books(book, other_book, lang)
                        st.markdown(comparison)
                        st.download_button(
                            label=t("download_comparison", lang),
                            data=comparison,
                            file_name=f"comparacion_{book.title}_vs_{other_book.title}.txt",
                            mime="text/plain"
                        )


def display_gemini_setup_instructions(lang: str = "es"):
    """Muestra instrucciones para configurar Gemini"""
    
    expander_title = "🔧 " + ("Cómo configurar Gemini API" if lang == "es" else "How to configure Gemini API")
    
    with st.expander(expander_title):
        if lang == "es":
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
        else:
            st.markdown("""
            ### Steps to configure Google Gemini:
            
            1. **Get API Key:**
               - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
               - Click on "Get API Key"
               - Copy your API key
            
            2. **Create `.env` file:**
               - In the project root, create a `.env` file
               - Add: `GEMINI_API_KEY=your_key_here`
            
            3. **Install dependency (if not already installed):**
               ```bash
               pip install google-generativeai
               ```
            
            4. **Restart the application:**
               ```bash
               streamlit run app.py
               ```
            
            ✅ Done! Now you can use all Gemini features.
            """)
