import streamlit as st
import pandas as pd
import numpy as np
from func import *

def show_abt():

    st.session_state.completed_sections = 4

    st.write('\n')
    st.subheader(':blue[Autoras y desarrolladoras del proyecto]')
    st.write('\n')
    st.write("¡Bienvenidos! Somos Nadine, Paula y Rosalía, originarias de Madrid, Vigo y Santiago, respectivamente.")
    st.write("Como apasionadas del Data Science, hemos creado este proyecto como culminación de nuestros estudios,"
    "poniendo en él todo nuestro entusiasmo y conocimientos.")
    st.write("Esperamos que disfrutes de la experiencia tanto como nosotras hemos disfrutado desarrollándola.")
    st.write("Gracias de corazón por tu apoyo y participación.")

    c1,c2,c3=st.columns(3)

    with c1:
        image_path = "images/nadine.png"
        if os.path.isfile(image_path):
            st.image(image_path, width=160)
        else:
            st.write(f"Archivo no encontrado en: {image_path}")
        st.write('Soy Nadine Poyato, una entusiasta de la salud (en concreto la salud infantil y la salud mental) que, tras desencantarse del trabajo en el campo de sanidad, se decidió por cambiar de sector.'
                 'Actualmente sigo ampliando mis conocimientos a la vez que realizo proyectos que aumentan cada día mi entusiasmo por el mundo del data science, y espero que siga en aumento.')
        if st.link_button(':blue[Linkedin de Nadine]', "https://www.linkedin.com/in/paulacalviño"):
            st.balloons()

    with c2:
        image_path = "images/paula.png"
        if os.path.isfile(image_path):
            st.image(image_path,  width=160)
        else:
            st.write(f"Archivo no encontrado en: {image_path}")
        st.write('Soy Paula Calviño. Anteriormente trabajaba en el sector de la logística pero actualmente me estoy reinventando y adentrando en el mundo del data science.'
                 'Estoy creciendo poco a poco en este nuevo sector y espero llegar a ser una profesional. '
                 'Queremos que este trabajo, en el que hemos puesto mucha ilusión y dedicación sirva para que la gente se conozca un poco más y para dar visibilidad a la importancia que tiene la salud mental.')
        if st.link_button(':blue[Linkedin de Paula]', "https://www.linkedin.com/in/paulacalviño"):
            st.balloons()

    with c3:
        image_path = "images/rosalia.png"
        if os.path.isfile(image_path):
            st.image(image_path,  width=160)
        else:
            st.write(f"Archivo no encontrado en: {image_path}")
        st.write('Soy Rosalía Reino, con experiencia en administración y gestión de bases de datos, actualmente en formación en data science. Mi interés en este campo me impulsa a expandir mis conocimientos y dedicarme plenamente a él. '
                 'Actualmente, estoy trabajando en varios proyectos para seguir ampliando mi formación y aplicar los conocimientos adquiridos. '
                 'En este proyecto, buscamos crear una herramienta para visibilizar y analizar la salud mental, contribuyendo a un tema de gran importancia en la sociedad.')
        if st.link_button(':blue[LinkedIn de Rosalía]', "https://www.linkedin.com/in/rosaliareino"):
            st.balloons()
