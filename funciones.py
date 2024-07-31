import streamlit as st
import pandas as pd
import os 
import io

def create_csv_file(data):

    # Define el directorio y el nombre del archivo
    DIRECTORIO_CSV = 'respuestas'
    NOMBRE_ARCHIVO = "respuestas_cuestionario.csv"
    
    if not os.path.exists(DIRECTORIO_CSV):
        os.makedirs(DIRECTORIO_CSV)
    

    ruta_csv = os.path.join(DIRECTORIO_CSV, NOMBRE_ARCHIVO)
    

    if os.path.exists(ruta_csv):
        
        data.to_csv(ruta_csv, mode='a', header=False, index=False)
    else:
        
        data.to_csv(ruta_csv, mode='w', header=True, index=False)


def reverse(options,dicc):

    options_reverse = {v: k for k, v in options.items()}
    response = {key: options_reverse[value] for key, value in dicc.items()}

    return response


def reverse_demog(options):
    options = {v: k for k, v in options.items()}
    return options

def navigate_page(new_page):
    st.session_state.page = new_page

if __name__=='__main__':
    create_csv_file()