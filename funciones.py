import streamlit as st
import datetime
import pandas as pd
from google.cloud import firestore
from google.cloud.firestore import Client
import plotly.graph_objects as go
import json

# def create_csv_file(data):
#     # Define el directorio y el nombre del archivo
#     DIRECTORIO_CSV = 'respuestas'
#     NOMBRE_ARCHIVO = "respuestas_cuestionario.csv"
    
#     if not os.path.exists(DIRECTORIO_CSV):
#         os.makedirs(DIRECTORIO_CSV)
#     ruta_csv = os.path.join(DIRECTORIO_CSV, NOMBRE_ARCHIVO)
    

#     if os.path.exists(ruta_csv):
        
#         data.to_csv(ruta_csv, mode='a', header=False, index=False)
#     else:
#         data.to_csv(ruta_csv, mode='w', header=True, index=False)

def get_db():
    key_json = st.secrets["firebase_key"]
    db = firestore.Client.from_service_account_info(key_json)
    return db


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
    db = get_db()
    doc_ref = db.collection('responses').document()
    data['timestamp'] = datetime.datetime.now().isoformat()
    doc_ref.set(data)


def separarQ(lista,df):
    lista2 = []

    for n in lista: 
        numero = f'Q{n}A'
        lista2.append(numero)
        nuevo_Q = df[lista2]
    return nuevo_Q


def anxiety_assessment(Q):
    anxiety_list=[2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41]
    Anxiety=separarQ(anxiety_list,Q)

    anxiety_sum=(Anxiety.sum(axis=1))

    assessment=[]
    for n in anxiety_sum:

        if n <=7:
            assessment.append('Ninguna: Parece que tu nivel de ansiedad es mínimo. Estás manejando bien el estrés y te sientes tranquilo en general.')
        elif n in range(8,10):
            assessment.append('Muy leve: Parece que tienes una ligera sensación de ansiedad, pero no parece afectar tu día a día de manera significativa.')
        elif n in range(10,15):
            assessment.append('Leve / Moderada: Parece que experimentas algo de ansiedad que puede estar influyendo en tu bienestar. Considera técnicas de manejo del estrés para mejorar tu comodidad.')
        elif n in range(15,20):
            assessment.append('Importante: Parece que tu nivel de ansiedad es notable. Puede ser útil buscar apoyo o estrategias para gestionar la ansiedad en tu vida diaria.')
        elif n >= 20:
            assessment.append('Grave: Parece que estás experimentando una alta cantidad de ansiedad que puede estar afectando seriamente tu bienestar. Es recomendable buscar ayuda profesional para abordar esta situación.')
        else: assessment.append('Error de conteo')

    return assessment


def depression_assessment(Q):
    depression_list=[3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]
    Depression=separarQ(depression_list,Q)
    
    
    depression_sum=(Depression.sum(axis=1))

    assessment=[]
    for n in depression_sum:

        if n <=9:
            assessment.append('Ninguna: Parece que te sientes con un estado de ánimo positivo y estable. No parece haber señales significativas de depresión en tu vida.')
        elif n in range(10,14):
            assessment.append('Muy leve: Parece que hay algunos momentos de tristeza o desánimo, pero en general te mantienes positivo y funcional.')
        elif n in range(14,21):
            assessment.append('Leve / Moderada: Parece que estás atravesando un período de baja en tu ánimo que puede estar afectando tu día a día. Considera hablar con alguien de confianza para obtener apoyo.')
        elif n in range(21,28):
            assessment.append('Importante: Parece que tu estado de ánimo muestra signos de depresión que están teniendo un impacto significativo en tu vida. Buscar ayuda profesional podría ser una buena opción.')
        elif n >= 28:
            assessment.append('Grave: Parece que estás enfrentando una depresión profunda que está afectando gravemente tu bienestar. Es crucial buscar asistencia profesional para recibir el apoyo adecuado.')
        else: assessment.append('Error de conteo')

    return assessment


def stress_assessment(Q):
    stress_list= [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]
    Stress=separarQ(stress_list,Q)
    
    stress_sum=(Stress.sum(axis=1))

    assessment=[]
    for n in stress_sum:

        if n <=14:
            assessment.append('Ninguna: Parece que tu nivel de estrés es muy bajo. Estás manejando bien tus responsabilidades y te sientes relajado.')
        elif n in range(15,19):
            assessment.append('Muy leve: Parece que tienes un poco de estrés ocasional, pero en general estás manejando bien tus obligaciones y desafíos.')
        elif n in range(19,26):
            assessment.append('Leve / Moderada: Parece que experimentas un nivel moderado de estrés que podría estar influyendo en tu vida diaria. Considera estrategias para reducir el estrés y mejorar tu equilibrio.')
        elif n in range(26,34):
            assessment.append('Importante: Parece que el estrés está teniendo un impacto significativo en tu bienestar. Podrías beneficiarte de técnicas de manejo del estrés y apoyo adicional.')
        elif n >= 34:
            assessment.append('Grave: Parece que el nivel de estrés que estás experimentando es alto y puede estar afectando seriamente tu calidad de vida. Es importante buscar apoyo profesional para manejar esta situación.')
        else: assessment.append('Error de conteo')

    return assessment


def personality(df):

    df['TIPI6'] = 8 - df['TIPI6']
    df['TIPI2'] = 8 - df['TIPI2']
    df['TIPI8'] = 8 - df['TIPI8']
    df['TIPI4'] = 8 - df['TIPI4']
    df['TIPI10'] = 8 - df['TIPI10']

    personality_traits = {
    'Extraversión': df[['TIPI1', 'TIPI6']].mean(axis=1).iloc[0],
    'Amabilidad': df[['TIPI2', 'TIPI7']].mean(axis=1).iloc[0],
    'Responsabilidad': df[['TIPI3', 'TIPI8']].mean(axis=1).iloc[0],
    'Neuroticismo': df[['TIPI4', 'TIPI9']].mean(axis=1).iloc[0],
    'Apertura_exp': df[['TIPI5', 'TIPI10']].mean(axis=1).iloc[0]}

    return personality_traits


def plot_radar_chart(personality_traits):
    categories = list(personality_traits.keys())
    values = list(personality_traits.values())
    values += values[:1]

    fill_color = 'rgba(0, 123, 255, 0.5)'  # Azul con transparencia
    line_color = 'rgba(0, 123, 255, 1)'  # Azul sin transparencia
    bg_color = 'rgba(255, 255, 255, 0.9)'  # Fondo blanco semitransparente

    fig = go.Figure(
        data=[
            go.Scatterpolar(
                r = values,
                theta = categories + [categories[0]],
                fill='toself',
                name='Rasgos de personalidad',
                fillcolor=fill_color,
                line=dict(color=line_color, width=2),
                marker=dict(size=8, symbol='circle', color='rgba(8, 82, 105, 0.8)'),

            )
        ]
    )

    fig.update_layout(
        # title=dict(
        #         text="Rasgos de Personalidad según el TIPI",
        #         font=dict(size=24, color='darkblue'),  # Personalizar la fuente del título
        #         x=0.5  # Centrar el título,
        # ),
    polar=dict(
        bgcolor=bg_color,
        radialaxis=dict(
            visible=True,
            range=[0, 7],
            tickvals=[1, 2, 3, 4, 5, 6, 7],
            ticktext=['1', '2', '3', '4', '5', '6', '7'],
            tickfont=dict(size=10, color='rgba(0, 123, 255, 0.5)'),
            gridcolor='rgba(0, 123, 255, 0.3)',  # Cambiar color de las líneas radiales
            gridwidth=1.5,
        ),
        angularaxis=dict(
            tickfont=dict(size=14, color='darkblue'),  # Personalizar las etiquetas de las categorías
            gridcolor='rgba(0, 123, 255, 0.1)',  # Cambiar color de las líneas circulares
            gridwidth=1.5,
        ),
    ),
    showlegend=False,
    )


    return fig

def personality_study(personality_traits):
    
    analysis = ""

    for trait, score in personality_traits.items():
        if trait == 'Extraversión':
            if score > 5:
                analysis += "Eres ***muy extrovertido***. Disfrutas de la interacción social y tiendes a sentirte energizado en situaciones grupales.""\n\n"
            elif score > 3:
                analysis += "Tienes una ***tendencia moderada hacia la extraversión***. Te gustan las interacciones sociales, pero también valoras tu tiempo a solas.""\n\n"
            else:
                analysis += "Tiendes a ser ***introvertido***. Prefieres actividades solitarias y te sientes más cómodo en ambientes tranquilos.""\n"

        elif trait == 'Amabilidad':
            if score > 5:
                analysis += "Eres ***muy amable***. Tiendes a ser compasivo, cooperativo y orientado hacia los demás.""\n\n"
            elif score > 3:
                analysis += "Eres ***moderadamente amable***. Puedes ser amigable y empático, pero también puedes ser directo y crítico cuando es necesario.""\n\n"
            else:
                analysis += "Tiendes a ser ***menos amable***. Puedes ser más competitivo y crítico en tus interacciones.""\n\n"

        elif trait == 'Responsabilidad':
            if score > 5:
                analysis += "Eres ***muy responsable***. Puedes ser organizado, eficiente y tienes un fuerte sentido del deber.""\n\n"
            elif score > 3:
                analysis += "Tienes una ***responsabilidad moderada***. Cumples con tus tareas y eres relativamente confiable.""\n\n"
            else:
                analysis += "Tiendes a ser ***menos responsable***. Puedes ser más desorganizado y tener dificultades para cumplir con tus tareas.""\n\n"

        elif trait == 'Neuroticismo':
            if score > 5:
                analysis += "Tienes una ***tendencia más alta al neuroticismo***. Tiendes a experimentar emociones negativas intensas como ansiedad y tristeza con frecuencia.""\n\n"
            elif score > 3:
                analysis += "Tienes una ***tendencia moderada hacia el neuroticismo***. Experimentas emociones negativas, pero generalmente puedes manejarlas bien.""\n\n"
            else:
                analysis += "Eres ***emocionalmente estable***. Manejas bien el estrés y rara vez experimentas emociones negativas intensas.""\n\n"
        elif trait == 'Apertura_exp':
            if score > 5:
                analysis += "Eres muy ***abierto a nuevas experiencias***. Eres creativo, curioso y disfrutas explorando nuevas ideas.""\n\n"
            elif score > 3:
                analysis += "Tienes una ***apertura moderada a la experiencia***. Eres curioso y disfrutas de la variedad, pero también valoras lo familiar.""\n\n"
            else:
                analysis += "Tiendes a ser más ***convencional***. Prefieres lo familiar y puedes ser más resistente al cambio.""\n\n"

    return analysis


def conditions_plot(Q):

    anxiety_list=[2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41]
    Anxiety=separarQ(anxiety_list,Q)
    anxiety_suma=(Anxiety.sum(axis=1).sum())

    stress_list= [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]
    Stress=separarQ(stress_list,Q)
    stress_suma=(Stress.sum(axis=1).sum())


    depression_list=[3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]
    Depression=separarQ(depression_list,Q)
    depression_suma=(Depression.sum(axis=1).sum())

    categories = ['Ansiedad', 'Depresión', 'Estrés']
    totals = [anxiety_suma, depression_suma, stress_suma]

    print(anxiety_suma)
    print(type(anxiety_suma))

    fig2 = go.Figure(go.Bar(x=categories, 
                            y=totals, 
                            marker_color= ['#1ecdc5', '#189b95', '#0d504d']))

    fig2.update_layout(title= dict(
                                text='Probabilidad de padecer Ansiedad, Depresión y/o Estrés',
                                font=dict(size=24, color='#17B4E8')),
                       xaxis_title = 'Afecciones', 
                       yaxis_title = 'Total')

    return fig2


if __name__=='__main__':
    save_response()
