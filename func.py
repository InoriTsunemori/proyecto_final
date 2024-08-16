import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from google.cloud import firestore

def get_db():
    key_json = st.secrets["firebase_key"]
    db = firestore.Client.from_service_account_info(key_json)
    return db

def get_db_local():

    db = firestore.Client.from_service_account_json('key.json')
    return db

def importar_datos_firebase():

    db=get_db()
    documents = db.collection('responses').stream()
    data = []

    for doc in documents:
        data.append(doc.to_dict())

    return data

def mostrar_datos():
    datos = importar_datos_firebase()
    
    df=pd.DataFrame(datos)

    column_order= ['Q1A','Q2A','Q3A','Q4A','Q5A','Q6A','Q7A','Q8A','Q9A','Q10A','Q11A','Q12A','Q13A','Q14A','Q15A','Q16A','Q17A','Q18A','Q19A','Q20A','Q21A','Q22A',
                   'Q23A','Q24A','Q25A','Q26A','Q27A','Q28A','Q29A','Q30A','Q31A','Q32A','Q33A','Q34A','Q35A','Q36A','Q37A','Q38A','Q39A','Q40A','Q41A','Q42A',
                   'TIPI1','TIPI2','TIPI3','TIPI4','TIPI5','TIPI6','TIPI7','TIPI8','TIPI9','TIPI10',
                   'VCL1','VCL2','VCL3','VCL4','VCL5','VCL6','VCL7','VCL8','VCL9','VCL10','VCL11','VCL12','VCL13','VCL14','VCL15','VCL16',
                   'education','urban','gender','engant','age','hand','religion','orientation','race','voted','married','familysize','major']
    
    df = df.reindex(columns=column_order)
    return df

def separarQ(lista,df):
    lista2 = []

    for n in lista: 
        numero = f'Q{n}A'
        lista2.append(numero)
        nuevo_Q = df[lista2]
    return nuevo_Q

def data_sum(df):

    anxiety_list=[2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41]
    stress_list= [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]
    depression_list=[3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]
    Anxiety=separarQ(anxiety_list,df)
    anxiety_sum=(Anxiety.sum(axis=1))
    Depression=separarQ(depression_list,df)  
    depression_sum=(Depression.sum(axis=1))
    Stress=separarQ(stress_list,df)
    stress_sum=(Stress.sum(axis=1))

    df['Anxiety']=anxiety_sum
    df['Depression']=depression_sum
    df['Stress']=stress_sum

    return df

def df_create(df):

    df['TIPI6'] = 8 - df['TIPI6']
    df['TIPI2'] = 8 - df['TIPI2']
    df['TIPI8'] = 8 - df['TIPI8']
    df['TIPI4'] = 8 - df['TIPI4']
    df['TIPI10'] = 8 - df['TIPI10']

    personality_traits = {
        'Extraversión': df[['TIPI1', 'TIPI6']].mean(axis=1),
        'Amabilidad': df[['TIPI2', 'TIPI7']].mean(axis=1),
        'Responsabilidad': df[['TIPI3', 'TIPI8']].mean(axis=1),
        'Neuroticismo': df[['TIPI4', 'TIPI9']].mean(axis=1),
        'Apertura_exp': df[['TIPI5', 'TIPI10']].mean(axis=1)}
    new_df = pd.DataFrame(personality_traits)
    
    return new_df

def func_identify_false_words(df, false_words):
           
    df['False_Words_Count'] = df[false_words].apply(lambda col : (col == 1).sum(), axis=1)
    df['False_Word'] = df['False_Words_Count'].apply(lambda x: 1 if x > 0 else 0)
    
    return df

def func_find_age_education_inconsistencies(df):
    df = df.copy()
    inconsistencies = df[(df['age'] < 21) & (df['education'] > 2)]
    df['Inconsistency_Age_Education'] = 0
    df.loc[inconsistencies.index, 'Inconsistency_Age_Education'] = 1
    inconsistency_counts = df[df['Inconsistency_Age_Education'] == 1]['age'].value_counts().sort_index()
    
    return df, inconsistencies, inconsistency_counts

def example_graphs(df_completo, x, y, colors, chart_type):

    st.subheader(f':blue[Gráfica seleccionada: {chart_type}]')

    if chart_type == 'Dispersión':

        fig = px.scatter(df_completo, 
                         x=x,
                         y=y, 
                         color=colors, 
                         title= f'Gráfico de dispersión con las variables {x} y {y}', 
                         color_continuous_scale='tealgrn_r')
        
        fig.update_layout(xaxis_title=f'Eje X {x}',
                          yaxis_title=f'Eje Y {y}')


    elif chart_type == 'Barras':
        fig = px.bar(df_completo, x=x, y=y, title=f'Gráfico de las variables para {x} y {y}.')

    elif chart_type == 'Línea':
        fig= px.line(df_completo, x=x, y=y, title=f'Gráfico de líneas para {x} y {y}.')

    st.plotly_chart(fig)


def create_df(data):
    df=pd.DataFrame(data)
    return df


def reverse(options,dicc):
    options_reverse = {v: k for k, v in options.items()}
    response = {key: options_reverse[value] for key, value in dicc.items()}
    return response

def reverse_demog(options):
    options = {v: k for k, v in options.items()}
    return options

def navigate_page(new_page):
    st.session_state.page = new_page

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
    'Extroversión': df[['TIPI1', 'TIPI6']].mean(axis=1).iloc[0],
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

        if trait == 'Extroversión':
            if score > 5:
                analysis += "Eres ***muy extrovertido***. Disfrutas de la interacción social y tiendes a sentirte energizado en situaciones grupales.""\n\n"
            elif score > 3:
                analysis += "Tienes una ***tendencia moderada hacia la extroversión***. Te gustan las interacciones sociales, pero también valoras tu tiempo a solas.""\n\n"
            else:
                analysis += "Tiendes a ser ***introvertido***. Prefieres actividades solitarias y te sientes más cómodo en ambientes tranquilos.""\n\n"

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

def func_plot_correlation_plotly(df, columns):
    correlation_matrix = df[columns].corr()
    correlation_matrix = np.round(correlation_matrix, 2)

    fig = go.Figure(data = go.Heatmap(
        z = correlation_matrix.values,
        x = correlation_matrix.columns,
        y = correlation_matrix.index,
        colorscale = "tealrose_r",
        text = correlation_matrix.values,
        texttemplate = '%{text:.2f}',
        showscale = True
    ))

    fig.update_layout(
        title = 'Correlation Matrix',
        xaxis = dict(tickangle = 90),
        yaxis = dict(autorange = 'reversed', scaleanchor = "x", scaleratio = 1),
        width = 1600,
        height = 1600
    )

    st.plotly_chart(fig, use_container_width = True)

    return correlation_matrix

#-------------funciones Rosalía------------------

########################### MATRIZ CORRELACION ###########################
def func_plot_correlation_matrix(df, columns, show_plot = True):
    correlation_matrix = df[columns].corr()
    correlation_matrix = np.round(correlation_matrix, 2)
    
    if show_plot:
        fig = go.Figure(data = go.Heatmap(
            z = correlation_matrix.values,
            x = correlation_matrix.columns,
            y = correlation_matrix.index,
            colorscale = "tealrose_r",
            text = correlation_matrix.values,
            texttemplate = '%{text:.2f}',
            showscale = False
        ))

        fig.update_layout(
            xaxis = dict(tickangle = 90),
            yaxis = dict(autorange = 'reversed', scaleanchor = "x", scaleratio = 1),
            width = 1600,
            height = 1600,
        )
        
        st.plotly_chart(fig, use_container_width = True)
    
    return correlation_matrix
    

# ------------ palabras falsas--------------
  
def func_identify_false_words(df, false_words):
    df['False_Words_Count'] = df[false_words].apply(lambda col : (col == 1).sum(), axis = 1)
    df['False_Word'] = df['False_Words_Count'].apply(lambda x: 1 if x > 0 else 0)

    return df
# Función gráfico palabras falsas
def func_barplot_vcl(df):
    false_words = ['VCL6', 'VCL9', 'VCL12']
    maping = {'VCL6': 'CUIVOCAL', 'VCL9': 'FILTEO', 'VCL12': 'VERDID'}
    
    df = func_identify_false_words(df, false_words)
    
    # Contar cuántas veces las palabras falsas han sido marcadas como 1
    false_word_counts = df[false_words].apply(lambda col: (col == 1).sum())
    
    false_word_counts.index = false_word_counts.index.map(maping)
    
    data = pd.DataFrame({
        'Palabras Falsas': false_word_counts.index,
        'Cantidad': false_word_counts.values,
        'Color': ['#005a49', '#008d76', '#00d69a']
    })
    
    # Gráfico de barras
    fig = px.bar(
        data_frame = data,
        x = 'Palabras Falsas',
        y = 'Cantidad',
        color = 'Palabras Falsas',
        color_discrete_map = {'CUIVOCAL': '#005a49', 'FILTEO': '#008d76', 'VERDID': '#00d69a'},
        labels = {'x': 'Palabras Falsas', 'y': 'Cantidad de Veces Marcadas'}
    )
    return fig

def func_nested_pie_vcl(df):
    false_words = ['VCL6', 'VCL9', 'VCL12']
    maping = {'VCL6': 'Cuivocal', 'VCL9': 'Filteo', 'VCL12': 'Verdid'}

    df = func_identify_false_words(df, false_words)

    counts_general = df['False_Word'].value_counts().sort_index()

    false_word_counts = df[false_words].apply(lambda col: (col == 1).sum())
    
    false_word_counts.index = false_word_counts.index.map(maping)
    
    # Crear gráfico anidado
    fig = go.Figure(data = [
        # Interno
        go.Pie(
            labels = ['No ha mentido', 'Ha mentido'],
            values = counts_general.values,
            domain = {'x': [0.2, 0.8], 'y': [0.2, 0.8]},
            marker = dict(colors = ['#2bccdc', '#ee6152']),
            hole = 0.3,
            name = 'Nivel 1'
        ),
        # Externo
        go.Pie(
            labels = false_word_counts.index,
            values = false_word_counts.values,
            domain = {'x': [0, 1], 'y': [0, 1]},
            marker = dict(colors = ['#005a49', '#008d76', '#00d69a']),
            hole = 0.75,
            name = 'Nivel 2' 
        )
    ])
    # Ajuste tamaño
    fig.update_layout(
        autosize = True,
        width = 350,
        height = 350,
        margin = dict(t = 0, b = 18, l = 0, r = 0),
        showlegend = True
    )
    
    return fig

########################### EDAD - EDUCACION ###########################

# Función inconsistencias entre edad y educación
def func_find_age_education_inconsistencies(df):
    df = df.copy()
    inconsistencies = df[(df['age'] < 21) & (df['education'] > 2)]
    df['Inconsistency_Age_Education'] = 0
    df.loc[inconsistencies.index, 'Inconsistency_Age_Education'] = 1
    inconsistency_counts = df[df['Inconsistency_Age_Education'] == 1]['age'].value_counts().sort_index()
    return df, inconsistencies, inconsistency_counts

age_colors = {
    18: '#005a49',
    19: '#008d76',
    20: '#00d69a'
}

# Función gráfico inconsistencias edad y educación
def func_plot_age_education_inconsistencies(inconsistency_counts):
    all_ages = [18, 19, 20]
    
    inconsistency_df = pd.DataFrame({
        'Edad': all_ages,
        'Cantidad de Inconsistencias': [inconsistency_counts.get(age, 0) for age in all_ages]
    })

    fig = go.Figure()

    for age in all_ages:
        age_data = inconsistency_df[inconsistency_df['Edad'] == age]
        fig.add_trace(go.Bar(
            x = age_data['Edad'],
            y = age_data['Cantidad de Inconsistencias'],
            name = f'Edad {age}',
            marker_color=age_colors.get(age, '#000000')
        ))

    fig.update_layout(
        xaxis_title = 'Edad',
        yaxis_title = 'Cantidad de Inconsistencias',
        barmode = 'group',
        xaxis = dict(
            tickvals = all_ages,
            ticktext = [str(age) for age in all_ages]
        )
    )
    
    return fig

def func_plot_age_education_inconsistencies_pie(df):
    df, _, inconsistency_counts = func_find_age_education_inconsistencies(df)
    counts_general = df['Inconsistency_Age_Education'].value_counts().sort_index()
    
    # Datos para el círculo central
    no_lies = counts_general[0] if 0 in counts_general.index else 0
    lies = counts_general[1] if 1 in counts_general.index else 0
    
    # Datos para el círculo externo
    labels_outer = inconsistency_counts.index.tolist()
    values_outer = inconsistency_counts.values.tolist()
    
    outer_colors = [age_colors[int(age)] for age in labels_outer]
    
    fig = go.Figure()
    
    fig.add_trace(go.Pie(
        labels = ['No ha mentido', 'Ha mentido'],
        values = [no_lies, lies],
        domain = {'x': [0.2, 0.8], 'y': [0.2, 0.8]},
        marker = dict(colors = ['#2bccdc', '#ee6152']),
        hole = 0.3,
        name = 'Nivel 1'
    ))
    fig.add_trace(go.Pie(
        labels = [f'Edad {age}' for age in labels_outer],
        values = values_outer,
        hole = 0.75,
        domain = {'x': [0, 1], 'y': [0, 1]},
        marker = dict(colors = outer_colors),
        name = 'Nivel 2'
    ))
    
    fig.update_layout(
        autosize = True,
        width = 350,
        height = 350,
        margin = dict(t = 0, b = 18, l = 0, r = 0),
        showlegend = True
    )
    return fig

########################### PARES RELACIONADOS ###########################
 
# Función pares relacionados
def func_find_related_pairs(correlation_matrix, columns, threshold = 0.8):
    pairs = []
    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            if abs(correlation_matrix.iloc[i, j]) >= threshold:
                pairs.append((columns[i], columns[j]))
    return pairs

# Función inconsistencias
def func_detect_inconsistencies(df, related_pairs):
    incoherencies_ids = []
    inconsistencies = []
    for (q1, q2) in related_pairs:
        contradictions = df[((df[q1] == 0) & (df[q2] == 3)) | ((df[q1] == 3) & (df[q2] == 0))]
        if not contradictions.empty:
            incoherencies_ids.extend(contradictions.index)
            inconsistencies.append({'question1': q1, 'question2': q2, 'contradictions': contradictions})
    df['Inconsistency_Questions'] = 0
    df.loc[incoherencies_ids, 'Inconsistency_Questions'] = 1
    df['Inconsistency_Questions_Count'] = pd.Series(incoherencies_ids).value_counts().reindex(df.index, fill_value = 0)
    return df, inconsistencies

color_palette = px.colors.qualitative.Pastel
pair_colors = {}

# Asignar colores por par
def assign_colors(inconsistencies):
    for i, inconsistency in enumerate(inconsistencies):
        q1 = inconsistency['question1']
        q2 = inconsistency['question2']
        pair_label = f'{q1} & {q2}'
        if pair_label not in pair_colors:
            pair_colors[pair_label] = color_palette[i % len(color_palette)]

# Función gráfico inconsistencias
def func_plot_inconsistencies_related_pairs(inconsistencies):
    assign_colors(inconsistencies)
    
    data = []
    for inconsistency in inconsistencies:
        q1 = inconsistency['question1']
        q2 = inconsistency['question2']
        count = len(inconsistency['contradictions'])
        data.append({'Pares': f'{q1} & {q2}',
                     'Cantidad de Inconsistencias': count,
                     'Color': pair_colors[f'{q1} & {q2}']
        })
    
    inconsistency_df = pd.DataFrame(data)

    if not inconsistency_df.empty:
        fig = px.bar(
            inconsistency_df,
            x = 'Pares',
            y = 'Cantidad de Inconsistencias',
            color = 'Pares',
            color_discrete_map = pair_colors,
            labels = {'Pares': 'Pares de Preguntas', 'Cantidad de Inconsistencias': 'Cantidad de Inconsistencias'},
            text = 'Cantidad de Inconsistencias'
        )
        fig.update_layout(
            xaxis_title = 'Pares de Preguntas',
            yaxis_title = 'Cantidad de Inconsistencias',
            xaxis_tickangle = -45
        )
        fig.update_traces(texttemplate = '%{text}', textposition = 'outside')
        st.plotly_chart(fig)
    else:
        st.write("No inconsistencies to display.")
        
def func_nested_pie_related_pairs(df, inconsistencies):
    assign_colors(inconsistencies)
    
    total_responses = len(df)
    no_lies = len(df[df['Inconsistency_Questions'] == 0])
    lies = total_responses - no_lies
    
    labels_outer = []
    values_outer = []
    outer_colors = []
    
    for inconsistency in inconsistencies:
        q1 = inconsistency['question1']
        q2 = inconsistency['question2']
        count = len(inconsistency['contradictions'])
        pair_label = f'{q1} & {q2}'
        labels_outer.append(pair_label)
        values_outer.append(count)
        outer_colors.append(pair_colors[pair_label])
        
    fig = go.Figure()
    
    fig.add_trace(go.Pie(
        labels = ['No ha mentido', 'Ha mentido'],
        values = [no_lies, lies],
        domain = {'x': [0.2, 0.8], 'y': [0.2, 0.8]},
        marker = dict(colors = ['#2bccdc', '#ee6152']),
        hole = 0.3,
        name = 'Nivel 1'
    ))
    
    fig.add_trace(go.Pie(
        labels = labels_outer,
        values = values_outer,
        domain = {'x': [0, 1], 'y': [0, 1]},
        marker = dict(colors = outer_colors),
        textinfo = 'none',
        hole = 0.75,
        name = 'Nivel 2'
    ))
    
    fig.update_layout(
        autosize = True,
        width = 350,
        height = 350,
        margin = dict(t = 0, b = 18, l = 0, r = 0),
        showlegend = True
    )
        
    return fig


    
