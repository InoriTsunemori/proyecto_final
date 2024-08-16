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
        image_path1 = "images/nadine.png"
        if image_path1:
            st.image(image_path1, width=180)
        else:
            st.write(f"Archivo no encontrado")
            
        st.write('Soy Nadine Poyato. Tengo experiencia anterior tanto en sanidad, como en gestion y dirección de comercio. Ésta última, y actual experiencia laboral ha sido la que me ha impulsado a decantarme por mi desarrollo en data science.'
                'En este momento estoy ampliando mis conocimientos en éste sector, haciendo proyectos a la vez que mejoro día a día mi valor como profesional.'
                'Hemos querido crear este proyecto para aunar nuestro conocimiento en data science y salud mental, ya que nos parece una temática delicada, poco hablada y necesaria de visivilizar en la sociedad.')
        
        if st.link_button(':blue[Linkedin de Nadine]', "https://www.linkedin.com/in/nadinepmanzano/"):
            st.balloons()

    with c2:
        image_path2 = "images/paula.png"
        if image_path2:
            st.image(image_path2,  width=180)
        else:
            st.write(f"Archivo no encontrado")
            
        st.write('Soy Paula Calviño. Anteriormente trabajaba en el sector de la logística pero actualmente me estoy reinventando y adentrando en el mundo del data science.'
                 'Estoy creciendo poco a poco en este nuevo sector y espero llegar a ser una profesional. '
                 'Queremos que este trabajo, en el que hemos puesto mucha ilusión y dedicación sirva para que la gente se conozca un poco más y para dar visibilidad a la importancia que tiene la salud mental.')
        
        if st.link_button(':blue[Linkedin de Paula]', "https://www.linkedin.com/in/paulacalviño"):
            st.balloons()

    with c3:
        image_path3 = "images/rosalia.png"
        if image_path3:
            st.image(image_path3,  width=180)
        else:
            st.write(f"Archivo no encontrado")
            
        st.write('Soy Rosalía Reino, con experiencia en administración y gestión de bases de datos, actualmente en formación en data science. Mi interés en este campo me impulsa a expandir mis conocimientos y dedicarme plenamente a él. '
                 'Actualmente, estoy trabajando en varios proyectos para seguir ampliando mi formación y aplicar los conocimientos adquiridos. '
                 'En este proyecto, buscamos crear una herramienta para visibilizar y analizar la salud mental, contribuyendo a un tema de gran importancia en la sociedad.')
        
        if st.link_button(':blue[LinkedIn de Rosalía]', "https://www.linkedin.com/in/rosaliareino"):
            st.balloons()
