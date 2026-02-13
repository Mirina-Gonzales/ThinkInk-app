import streamlit as st
from src.services.book_service import BookService
from src.ui.pages import display_book_card, display_author_section, display_questions
from src.i18n.i18n_service import t

# Obtener idioma
lang = st.session_state.get('language', 'es')

# Header
st.title(t("principal_title", lang))
st.markdown(
    t("app_subtitle", lang)
)
st.divider()

# Inicializar sesión
if "book_service" not in st.session_state or st.session_state.get("last_lang") != lang:
    st.session_state.book_service = BookService(lang=lang)
    st.session_state.last_lang = lang

book_service = st.session_state.book_service

# Sidebar - Selección de libro
with st.sidebar:
    st.header(t("sidebar_select_book", lang))
    books = book_service.get_all_books()
    book_titles = [book.title for book in books]
    
    selected_title = st.selectbox(t("choose_book", lang), book_titles)
    selected_book = book_service.get_book_by_title(selected_title)

# Tabs principales (SIN GEMINI)
if selected_book:
    tab1, tab2, tab3, tab4 = st.tabs(
        [t("principal_info_section", lang), t("principal_pre_questions", lang), t("principal_post_questions", lang), t("principal_author_bio", lang)]
    )
    
    with tab1:
        st.subheader(f"{selected_book.title}")
        display_book_card(selected_book, lang)
    
    with tab2:
        st.subheader(t("principal_pre_questions", lang))
        st.info(
            t("principal_pre_questions_desc", lang)
        )
        pre_answers = display_questions(
            selected_book.pre_questions, t("principal_pre_questions", lang), lang
        )
        
        if st.button(t("btn_save_pre_answers", lang), key="save_pre"):
            st.success(t("success_pre_answers", lang))
    
    with tab3:
        st.subheader(t("principal_post_questions", lang))
        st.info(
            t("principal_post_questions_desc", lang)
        )
        post_answers = display_questions(
            selected_book.post_questions, t("principal_post_questions", lang), lang
        )
        
        if st.button(t("btn_save_post_answers", lang), key="save_post"):
            st.success(t("success_post_answers", lang))
    
    with tab4:
        display_author_section(selected_book, lang)
        
        with st.expander(t("more_author_stats", lang)):
            col1, col2 = st.columns(2)
            with col1:
                st.metric(t("book_label", lang), selected_book.title)
                st.metric(t("book_genre", lang), selected_book.genre)
            with col2:
                st.metric(t("book_year", lang), selected_book.year)
                st.metric(t("book_author", lang), selected_book.author)

else:
    st.warning(t("book_not_selected_list", lang))

# Footer
st.divider()
st.markdown(
    "<div style='text-align: center'><small>📚 ThinkInk App - " + t("app_subtitle", lang) + "</small></div>",
    unsafe_allow_html=True,
)
