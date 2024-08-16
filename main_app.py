import streamlit as st 
import pandas as pd
from func import *
from home import *
from graphs import *
from survey import *
from about_this import *
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Proyecto Pinal Ropana",
    page_icon=":star:",
    layout="wide",
    initial_sidebar_state="expanded")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amatic+SC:wght@400;700&family=Dancing+Script:wght@400..700&family=Edu+VIC+WA+NT+Beginner:wght@400..700&display=swap');

    /* Fuente global */
    html, body, [class*="css"]  {
        font-family: "Amatic SC", sans-serif;
    }

    /* Fuente para títulos */
    h1, h2, h3, h4, h5, h6 {
        font-family: "Amatic SC", cursive;
    }

    /* Fuente para botones */
    .stButton > button {
        font-family: "Amatic SC", cursive;
    }

    </style>
    """, unsafe_allow_html=True)

st.markdown("""
<style>
/* Oculta el botón de fullscreen */
button[title="View fullscreen"]{
    visibility: hidden;
}

/* Ajuste de márgenes y padding del contenedor principal */
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
    padding-left: 1rem;
    padding-right: 1rem;
    margin-top: 1rem;
    margin-bottom: 1rem;
    margin-left: 1rem;
    margin-right: 1rem;
}
</style>
""",unsafe_allow_html=True)

st.markdown("""
    <style>
    .stButton > button {
        background-color: #AED6F1; /* Aguamarina-Turquesa claro */
        color: black; /* Letras negras */
        border: none; /* Quitar borde */
        padding: 15px 32px; /* Tamaño del botón */
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 8px; /* Bordes redondeados */
    }
    .stButton > button:hover {
        background-color: #66CDAA; /* Color de fondo al pasar el cursor */
        color: black; /* Letras blancas al pasar el cursor */
    }
    </style>
""", unsafe_allow_html=True)

def main():

    with st.sidebar:

        if 'completed_sections' not in st.session_state:
            st.session_state.completed_sections = 0

        completed_sections = st.session_state.completed_sections
        total_sections = 4
        progress = (completed_sections / total_sections) * 100


        image_path = "images/logo_zen.png"
        if image_path:
            st.sidebar.image(image_path, use_column_width=True)
        else:
            st.sidebar.write(f"Archivo no encontrado")

        st.write("Progreso del cuestionario:")
        st.write(progress)
        
        if progress == 0:
            st.sidebar.image('images/star_1.png')
        elif progress == 25:
            st.sidebar.image('images/star_2.png')
        elif progress == 50:
            st.sidebar.image('images/star_3.png')
        elif progress == 75:
            st.sidebar.image('images/star_4.png')
        elif progress == 100:
            st.sidebar.image('images/star_5.png')

        selected= option_menu(
            menu_title= 'Menú',
            options=['Principal','Cuestionario','Gráficos','Acerca de'],
            icons=['house-heart','clipboard2-heart','graph-down','envelope-paper-heart'],
            menu_icon='search-heart',
            default_index = 0
        )

    if selected == 'Principal':
        show_home()
    elif selected == 'Cuestionario':
        show_survey()
    elif selected == 'Gráficos':
        show_graphs()
    elif selected == 'Acerca de':
        show_abt()

if __name__ == '__main__':
    main()
