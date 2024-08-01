import streamlit as st
import os 
import datetime
from firebase_config import db


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


def save_response(data):

    doc_ref = db.collection('responses').document()
    data['timestamp'] = datetime.datetime.now().isoformat()
    doc_ref.set(data)

def separarQ(lista,df):

    lista2 = []

    for n in lista: 
        numero = f'Q{n}'
        lista2.append(numero)
        nuevo_Q= df[lista2]

    return nuevo_Q

if __name__=='__main__':
    save_response()
