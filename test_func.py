import plotly.graph_objects as go

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
            assessment.append('Ninguna')
        elif n in range(8,10):
            assessment.append('Muy leve')
        elif n in range(10,15):
            assessment.append('Leve / Moderada')
        elif n in range(15,20):
            assessment.append('Importante')
        elif n >= 20:
            assessment.append('Grave')
        else: assessment.append('Error de conteo')

    return assessment

def depression_assessment(Q):
    depression_list=[3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]
    Depression=separarQ(depression_list,Q)
    
    
    depression_sum=(Depression.sum(axis=1))

    assessment=[]
    for n in depression_sum:

        if n <=9:
            assessment.append('Ninguna')
        elif n in range(10,14):
            assessment.append('Muy leve')
        elif n in range(14,21):
            assessment.append('Leve / Moderada')
        elif n in range(21,28):
            assessment.append('Importante')
        elif n >= 28:
            assessment.append('Grave')
        else: assessment.append('Error de conteo')

    return assessment

def stress_assessment(Q):
    stress_list= [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]
    Stress=separarQ(stress_list,Q)
    
    
    stress_sum=(Stress.sum(axis=1))

    assessment=[]
    for n in stress_sum:

        if n <=14:
            assessment.append('Ninguna')
        elif n in range(15,19):
            assessment.append('Muy leve')
        elif n in range(19,26):
            assessment.append('Leve / Moderada')
        elif n in range(26,34):
            assessment.append('Importante')
        elif n >= 34:
            assessment.append('Grave')
        else: assessment.append('Error de conteo')

    return assessment


def personality(df):

    df['TIPI6'] = 8 - df['TIPI6']
    df['TIPI2'] = 8 - df['TIPI2']
    df['TIPI8'] = 8 - df['TIPI8']
    df['TIPI4'] = 8 - df['TIPI4']
    df['TIPI10'] = 8 - df['TIPI10']


    personality_traits = {
        'extraversion' : df[['TIPI1', 'TIPI6']].mean(axis=1),
        'amabilidad' : df[['TIPI2', 'TIPI7']].mean(axis=1),
        'responsabilidad' : df[['TIPI3', 'TIPI8']].mean(axis=1),
        'neuroticismo' : df[['TIPI4', 'TIPI9']].mean(axis=1),
        'apertura_exp' : df[['TIPI5', 'TIPI10']].mean(axis=1)}


    return personality_traits

def plot_radar_chart(personality_traits):
    categories = list(personality_traits.keys())
    values = list(personality_traits.values())
    values += values[:1]

    fig = go.Figure(
        data=[
            go.Scatterpolar(
                r=values,
                theta=categories + [categories[0]],
                fill='toself',
                name='Rasgos de personalidad',
                fillcolor='rgba(127, 127, 255, 0.5)',  # Cambiar el color de relleno
                line=dict(color='blue')  # Cambiar el color del borde
            )
        ]
    )

    fig.update_layout(
        title="Gráfico de Radar de Rasgos de Personalidad",
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 7]
            )
        ),
        showlegend=True
    )

    return fig

def personality_study(personality_traits):
    analysis = ""
    
    for trait, score in personality_traits.items():
        if trait == 'Extraversión':
            if score > 5:
                analysis += "Eres muy extrovertido. Disfrutas de la interacción social y tiendes a sentirte energizado en situaciones grupales.\n"
            elif score > 3:
                analysis += "Tienes una tendencia moderada hacia la extraversión. Te gustan las interacciones sociales, pero también valoras tu tiempo a solas.\n"
            else:
                analysis += "Tiendes a ser introvertido. Prefieres actividades solitarias y te sientes más cómodo en ambientes tranquilos.\n"

        elif trait == 'Amabilidad':
            if score > 5:
                analysis += "Eres muy amable. Tiendes a ser compasivo, cooperativo y orientado hacia los demás.\n"
            elif score > 3:
                analysis += "Eres moderadamente amable. Puedes ser amigable y empático, pero también puedes ser directo y crítico cuando es necesario.\n"
            else:
                analysis += "Tiendes a ser menos amable. Puedes ser más competitivo y crítico en tus interacciones.\n"

        elif trait == 'Responsabilidad':
            if score > 5:
                analysis += "Eres muy responsable. Eres organizado, eficiente y tienes un fuerte sentido del deber.\n"
            elif score > 3:
                analysis += "Tienes una responsabilidad moderada. Cumples con tus tareas y eres relativamente confiable.\n"
            else:
                analysis += "Tiendes a ser menos responsable. Puedes ser más desorganizado y tener dificultades para cumplir con tus tareas.\n"

        elif trait == 'Neuroticismo':
            if score > 5:
                analysis += "Tiendes a experimentar emociones negativas intensas como ansiedad y tristeza con frecuencia.\n"
            elif score > 3:
                analysis += "Tienes una tendencia moderada hacia el neuroticismo. Experimentas emociones negativas, pero generalmente puedes manejarlas bien.\n"
            else:
                analysis += "Eres emocionalmente estable. Manejas bien el estrés y rara vez experimentas emociones negativas intensas.\n"

        elif trait == 'Apertura exp':
            if score > 5:
                analysis += "Eres muy abierto a nuevas experiencias. Eres creativo, curioso y disfrutas explorando nuevas ideas.\n"
            elif score > 3:
                analysis += "Tienes una apertura moderada a la experiencia. Eres curioso y disfrutas de la variedad, pero también valoras lo familiar.\n"
            else:
                analysis += "Tiendes a ser más convencional. Prefieres lo familiar y puedes ser más resistente al cambio.\n"

    return analysis