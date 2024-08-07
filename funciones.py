import streamlit as st
import os 
import datetime
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import joblib
import pandas as pd


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

def normalize_input(data, scaler):
    print(f"Datos antes de la normalización: {data}")
    normalized_data = scaler.transform(data)
    print(f"Datos después de la normalización: {normalized_data}")
    return normalized_data



def predictions(data):

    model_stress = load_model('model_stress_new.keras')
    model_anxiety = load_model('model_anxiety_new.keras')
    model_depression = load_model('model_depression_new.keras')

    input_data = (data)
    normalizador = joblib.load('normalizador_stress.pkl')
    input_data_normalized = normalizador.fit_transform(input_data)

    stress_prediction = model_stress.predict(input_data_normalized)
    anxiety_prediction = model_anxiety.predict(input_data_normalized)
    depression_prediction = model_depression.predict(input_data_normalized)

    stress_class = np.argmax(stress_prediction, axis=1)
    anxiety_class = np.argmax(anxiety_prediction, axis=1)
    depression_class = np.argmax(depression_prediction, axis=1)

    st.write(f'La predicción de estrés es: {stress_class} y {stress_prediction}')
    st.write(f'La predicción de ansiedad es: {anxiety_class} y {anxiety_prediction}')
    st.write(f'La predicción de depresión es: {depression_class} y {depression_prediction}')

# def algorythm(Q):

#     Q.iloc[:, :42]
#     anxiety_list = [2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41]
#     depression_list = [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]
#     stress_list = [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]

#     ansiedad = Q[[f'Q{n}' for n in anxiety_list]]
#     estres = Q[[f'Q{n}' for n in stress_list]]
#     depresion = Q[[f'Q{n}' for n in depression_list]]

#     ansiedad = separarQ(anxiety_list, Q)
#     estres = separarQ(stress_list, Q)
#     depresion = separarQ(depression_list, Q)

#     Q['Suma Ansiedad'] = ((ansiedad.sum(axis=1)))
#     Q['Suma Depresión'] = ((depresion.sum(axis=1)))
#     Q['Suma Estrés'] = ((estres.sum(axis=1)))
           
#     df_ansiedad =  pd.concat([ansiedad, Q['Suma Ansiedad']], axis=1)
#     df_depresion =  pd.concat([depresion, Q['Suma Depresión']], axis=1)
#     df_estres =  pd.concat([estres, Q['Suma Estrés']], axis=1)   
    
#     with open('model_stress.pkl', 'rb') as f:
#         model_estres = pickle.load(f)
#     with open('model_depresion.pkl', 'rb') as f:
#         model_ansiedad = pickle.load(f)
#     with open('model_anxiety.pkl', 'rb') as f:
#         model_depresion = pickle.load(f)
                       
#     stress = model_estres.predict(df_estres)
#     anxiety = model_ansiedad.predict(df_ansiedad)
#     depression = model_depresion.predict(df_depresion)

#     return  [
#         st.write('**Predicciones de Estrés:**'),
#         st.write(stress),
#         st.write('**Predicciones de Ansiedad:**'),
#         st.write(anxiety),
#         st.write('**Predicciones de Depresión:**'),
#         st.write(depression)]


# def algorithm(df):
    
#     with open('model_str.p', 'rb') as f:
#         stress_m = pickle.load(f)
#     with open('model_depr.p', 'rb') as f:
#         depression_m = pickle.load(f)
#     with open('model_anx.p', 'rb') as f:
#         anxiety_m = pickle.load(f)
    

#     stress = stress_m.predict(np.array(df))
#     anxiety = anxiety_m.predict(np.array(df))
#     depression = depression_m.predict(np.array(df))


#     # Crear listas para almacenar los niveles
#     stress_levels = []
#     anxiety_levels = []
#     depression_levels = []

#     # Suponiendo que las predicciones son arrays, iterar sobre ellas
#     for s, a, d in zip(stress, anxiety, depression):
#         stress_levels.append(s)
#         anxiety_levels.append(a)
#         depression_levels.append(d)

#         # Predicciones de estrés
#         if s == 0:
#             st.write('Probabilidad de estar padeciendo estrés en la actualidad nula o muy baja./Ninguna')
#         elif s == 1:
#             st.write('Probabilidad de estar padeciendo estrés en la actualidad muy baja./muy leve')
#         elif s == 2:
#             st.write('Probabilidad de estar padeciendo estrés en la actualidad baja./leve')
#         elif s == 3:
#             st.write('Probabilidad de estar padeciendo estrés en la actualidad moderada.')
#         elif s == 4:
#             st.write('Probabilidad de estar padeciendo estrés en la actualidad alta.')

#         # Predicciones de ansiedad
#         if a == 0:
#             st.write('Probabilidad de estar padeciendo ansiedad en la actualidad nula o muy baja./Ninguna')
#         elif a == 1:
#             st.write('Probabilidad de estar padeciendo ansiedad en la actualidad muy baja./muy leve')
#         elif a == 2:
#             st.write('Probabilidad de estar padeciendo ansiedad en la actualidad baja./leve')
#         elif a == 3:
#             st.write('Probabilidad de estar padeciendo ansiedad en la actualidad moderada.')
#         elif a == 4:
#             st.write('Probabilidad de estar padeciendo ansiedad en la actualidad alta.')

#         # Predicciones de depresión
#         if d == 0:
#             st.write('Probabilidad de estar padeciendo depresión en la actualidad nula o muy baja./Ninguna')
#         elif d == 1:
#             st.write('Probabilidad de estar padeciendo depresión en la actualidad muy baja./muy leve')
#         elif d == 2:
#             st.write('Probabilidad de estar padeciendo depresión en la actualidad baja./leve')
#         elif d == 3:
#             st.write('Probabilidad de estar padeciendo depresión en la actualidad moderada.')
#         elif d == 4:
#             st.write('Probabilidad de estar padeciendo depresión en la actualidad alta.')

#     # Graficar los niveles de estrés, ansiedad y depresión
#     fig = go.Figure()

#     fig.add_trace(go.Bar(
#         x=['Ansiedad', 'Estrés', 'Depresión'],
#         y=[anxiety_levels[0], stress_levels[0], depression_levels[0]],
#         marker_color=['blue', 'red', 'green']
#     ))

#     fig.update_layout(
#         title='Niveles de Ansiedad, Estrés y Depresión',
#         xaxis_title='Categoría',
#         yaxis_title='Nivel',
#         yaxis=dict(
#             tickvals=[0, 1, 2, 3, 4],
#             ticktext=['Nulo o Muy Bajo', 'Muy Bajo', 'Bajo', 'Moderado', 'Alto']
#         )
#     )

#     st.plotly_chart(fig)

def algorithm(df):
    # Cargar modelos
    try:
        with open('model_str.p', 'rb') as f:
            stress_m = pickle.load(f)
        with open('model_depr.p', 'rb') as f:
            depression_m = pickle.load(f)
        with open('model_anx.p', 'rb') as f:
            anxiety_m = pickle.load(f)
    except FileNotFoundError as e:
        st.error(f"Error al cargar los modelos: {e}")
        return

    # Verificar contenido del DataFrame
    st.write("Datos de entrada para predicciones:")
    st.write(df)

    # Predicciones
    try:
        stress = stress_m.predict(np.array(df))
        anxiety = anxiety_m.predict(np.array(df))
        depression = depression_m.predict(np.array(df))
    except Exception as e:
        st.error(f"Error al realizar predicciones: {e}")
        return

    # Crear listas para almacenar los niveles
    stress_levels = []
    anxiety_levels = []
    depression_levels = []

    # Suponiendo que las predicciones son arrays, iterar sobre ellas
    for s, a, d in zip(stress, anxiety, depression):
        stress_levels.append(s)
        anxiety_levels.append(a)
        depression_levels.append(d)

        # Predicciones de estrés
        if s == 0:
            st.write('Probabilidad de estar padeciendo estrés en la actualidad nula o muy baja./Ninguna')
        elif s == 1:
            st.write('Probabilidad de estar padeciendo estrés en la actualidad muy baja./muy leve')
        elif s == 2:
            st.write('Probabilidad de estar padeciendo estrés en la actualidad baja./leve')
        elif s == 3:
            st.write('Probabilidad de estar padeciendo estrés en la actualidad moderada.')
        elif s == 4:
            st.write('Probabilidad de estar padeciendo estrés en la actualidad alta.')

        # Predicciones de ansiedad
        if a == 0:
            st.write('Probabilidad de estar padeciendo ansiedad en la actualidad nula o muy baja./Ninguna')
        elif a == 1:
            st.write('Probabilidad de estar padeciendo ansiedad en la actualidad muy baja./muy leve')
        elif a == 2:
            st.write('Probabilidad de estar padeciendo ansiedad en la actualidad baja./leve')
        elif a == 3:
            st.write('Probabilidad de estar padeciendo ansiedad en la actualidad moderada.')
        elif a == 4:
            st.write('Probabilidad de estar padeciendo ansiedad en la actualidad alta.')

        # Predicciones de depresión
        if d == 0:
            st.write('Probabilidad de estar padeciendo depresión en la actualidad nula o muy baja./Ninguna')
        elif d == 1:
            st.write('Probabilidad de estar padeciendo depresión en la actualidad muy baja./muy leve')
        elif d == 2:
            st.write('Probabilidad de estar padeciendo depresión en la actualidad baja./leve')
        elif d == 3:
            st.write('Probabilidad de estar padeciendo depresión en la actualidad moderada.')
        elif d == 4:
            st.write('Probabilidad de estar padeciendo depresión en la actualidad alta.')

    # Graficar los niveles de estrés, ansiedad y depresión
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=['Ansiedad', 'Estrés', 'Depresión'],
        y=[anxiety_levels[0], stress_levels[0], depression_levels[0]],
        marker_color=['blue', 'red', 'green']
    ))

    fig.update_layout(
        title='Niveles de Ansiedad, Estrés y Depresión',
        xaxis_title='Categoría',
        yaxis_title='Nivel',
        yaxis=dict(
            tickvals=[0, 1, 2, 3, 4],
            ticktext=['Nulo o Muy Bajo', 'Muy Bajo', 'Bajo', 'Moderado', 'Alto']
        )
    )

    st.plotly_chart(fig)



if __name__=='__main__':
    save_response()
