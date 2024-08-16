import streamlit as st
import pandas as pd
import numpy as np
from func import *

def show_home():

    st.session_state.completed_sections = 1
    st.title("Bienvenido a la Aplicación de Análisis Psicológico, El Proyecto Ropana")
    st.subheader(":violet[Explora y analiza datos sobre ansiedad, estrés, depresión y otros factores psicológicos]")

    # Imagen o video sobre la importancia de la salud mental
    st.markdown("Cuidemos la salud mental")

    imagenes = [
    {"nombre": ":blue-background[Tip 1]", "ruta": "images/1.png", "caption": "Importancia de la salud mental."},
    {"nombre": ":blue-background[Tip 2]", "ruta": "images/2.png", "caption": "Consejos para manejar el estrés."},
    {"nombre": ":blue-background[Tip 3]", "ruta": "images/3.png", "caption": "Claves para el bienestar emocional."},]

    col1, col2 = st.columns(2)
    
    with col1:

        opcion_seleccionada = st.radio(
        "**Échale un vistazo a estos tips para ver cómo puedes cuidar tu salud mental**",
        options=[img["nombre"] for img in imagenes],horizontal=True)


        for img in imagenes:
            if img["nombre"] == opcion_seleccionada:
                st.image(img["ruta"], caption=img["caption"], width=550)
                break

    with col2:
        
        st.markdown("¡Gracias por visitar nuestro cuestionario! Este proyecto está diseñado para evaluar diversos aspectos relacionados con la ansiedad, el estrés, y la depresión, así como para obtener una visión más completa de tu perfil personal.")
        st.markdown("Tu participación es fundamental y muy apreciada. A continuación, prodrás navegar a través de varias secciones que incluyen: una escala de Beck, un cuestionario de personalidad, y una sección de datos demográficos.")

        st.markdown("### :violet[Objetivo del Cuestionario]")

        st.markdown("El cuestionario que estás a punto de completar tiene como objetivo proporcionar una evaluación integral de tu estado emocional y psicológico. Esta información se utilizará únicamente con fines educativos y de investigación.") 
        st.markdown("Todos los datos serán tratados con la máxima confidencialidad y no se publicarán ni compartirán de ninguna manera que pueda identificarte personalmente.")

        with st.expander('### ¿Cómo Funciona?'):

            st.markdown("1. **Escala de Beck**: Evaluarás tu nivel de ansiedad, estrés y depresión en base a preguntas sobre tu experiencia en la última semana.")
            st.markdown("2. **Cuestionario de Personalidad**: Completarás un breve inventario que te ayudará a clasificar tus características de personalidad.")
            st.markdown("3. **Datos Demográficos**: Proporcionarás información sobre ti que ayudará a contextualizar tus respuestas.")

        st.markdown("Si tienes alguna pregunta o necesitas asistencia durante el cuestionario, no dudes en contactarnos. ¡Comencemos!")

    #Vídeo explicativo de cómo usar las gráficas
    st.markdown("A continuación te mostramos un vídeo explicativo para que modifiques y hagas tu propio gráfico en el apartado **Gráficos**.")
    
    video_file = open("images/explicacion_graficas.mp4", "rb")
    video_bytes = video_file.read()

    st.video(video_bytes)
      
    
    # Pie de página
    st.markdown("---")
    st.write("Aplicación desarrollada por Paula, Rosalía y Nadine.")

if __name__=='__main__':
    show_home()