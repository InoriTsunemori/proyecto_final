import streamlit as st 
from func import *

def qwerys():

    options = {
        0 : 'Ninguna vez',
        1 : 'En ciertas ocasiones',
        2 : 'Bastantes veces',
        3 : 'Todos o la mayoría de los días'
    }

    qw = {
        "Q1A" : st.selectbox("1 - Me he sentido molesto por cosas triviales", options=options.values()),
        "Q2A" : st.selectbox("2 - He notado la boca seca", options=options.values()),
        "Q3A" : st.selectbox("3 - Me ha costado mucho experimentar algún tipo de sentimientos positivos", options=options.values()),
        "Q4A" : st.selectbox("4 - Experimenté dificultad para respirar (por ejemplo: respiración excesivamente rápida, falta de aire en ausencia de esfuerzo físico)", options=options.values()),
        "Q5A" : st.selectbox("5 - He sentido que simplemente no podía continuar", options=options.values()),
        "Q6A" : st.selectbox("6 - Tendía a reaccionar desmesuradamente a situaciones que no lo merecían", options=options.values()),
        "Q7A" : st.selectbox("7 - He tenido sensación de temblores (por ejemplo: no me reaccionaban bien las extremidades)", options=options.values()),
        "Q8A" : st.selectbox("8 - He tenido dificultades para relajarme/desconectar", options=options.values()),
        "Q9A" : st.selectbox("9 - Me encontré en situaciones que me hacían sentir tan ansioso que he sentido alivio cuando estas han terminado", options=options.values()),
        "Q10A": st.selectbox("10 - Sentí que no tenía nada por lo cual levantarme", options=options.values()),
        "Q11A": st.selectbox("11 - Me he molestado con bastante facilidad", options=options.values()),
        "Q12A": st.selectbox("12 - Sentí que utilicé demasiada energía", options=options.values()),
        "Q13A": st.selectbox("13 - Me sentí triste y deprimido", options=options.values()),
        "Q14A": st.selectbox("14 - Me encontré impaciente cuando tuve alguna demora (por ejemplo: tráfico, citas, filas, esperas)", options=options.values()),
        "Q15A": st.selectbox("15 - Tuve momentos de debilidad", options=options.values()),
        "Q16A": st.selectbox("16 - Sentí que perdí el interés en prácticamente todo", options=options.values()),
        "Q17A": st.selectbox("17 - Sentí que no valía mucho como persona", options=options.values()),
        "Q18A": st.selectbox("18 - Me sentí bastante sensible", options=options.values()),
        "Q19A": st.selectbox("19 - Sudaba de forma notable (por ejemplo: sudor en las manos) en ausencia de temperaturas altas o desgaste físico", options=options.values()),
        "Q20A": st.selectbox("20 - Sentí miedo sin una buena razón", options=options.values()),
        "Q21A": st.selectbox("21 - Pensé que la vida no valía la pena", options=options.values()),
        "Q22A": st.selectbox("22 - Me resultó difícil relajarme", options=options.values()),
        "Q23A": st.selectbox("23 - Tuve dificultades para tragar", options=options.values()),
        "Q24A": st.selectbox("24 - No pude disfrutar de las cosas que hice", options=options.values()),
        "Q25A": st.selectbox("25 - Fui consciente del latido de mi corazón en ausencia de esfuerzo (por ejemplo, aumento de la frecuencia cardiaca)", options=options.values()),
        "Q26A": st.selectbox("26 - Me sentí afligido y desanimado", options=options.values()),
        "Q27A": st.selectbox("27 - Estaba muy irritable", options=options.values()),
        "Q28A": st.selectbox("28 - Estuve cerca de entrar en pánico", options=options.values()),
        "Q29A": st.selectbox("29 - Me resultó difícil calmarme después de molestarme por algo", options=options.values()),
        "Q30A": st.selectbox("30 - Temía que me superara alguna tarea trivial pero desconocida para mí", options=options.values()),
        "Q31A": st.selectbox("31 - Nada me generaba entusiasmo", options=options.values()),
        "Q32A": st.selectbox("32 - Me resultó difícil tolerar interrupciones en lo que estaba haciendo", options=options.values()),
        "Q33A": st.selectbox("33 - Me encontraba en un estado de tensión y nervios", options=options.values()),
        "Q34A": st.selectbox("34 - Sentí que era bastante inútil", options=options.values()),
        "Q35A": st.selectbox("35 - No toleraba nada que me impidiera continuar con lo que estaba haciendo", options=options.values()),
        "Q36A": st.selectbox("36 - Me sentí aterrorizado", options=options.values()),
        "Q37A": st.selectbox("37 - No veía nada en el futuro con lo que tener esperanza", options=options.values()),
        "Q38A": st.selectbox("38 - Sentí que la vida no tenía sentido", options=options.values()),
        "Q39A": st.selectbox("39 - Me sentí agitado", options=options.values()),
        "Q40A": st.selectbox("40 - Me preocupaban situaciones en las que podría entrar en pánico y hacer el ridículo", options=options.values()),
        "Q41A": st.selectbox("41 - Experimenté temblores (por ejemplo: en las manos)", options=options.values()),
        "Q42A": st.selectbox("42 - Me resultaba difícil reunir iniciativa o motivación para hacer las cosas", options=options.values())
    }
    
    qwery_response=reverse(options,qw)
    return qwery_response

def tipi():

    options = {
        1 : 'Muy en desacuerdo',
        2 : 'Moderadamente en desacuerdo',
        3 : 'Un poco en desacuerdo',
        4 : 'Ni de acuerdo ni en desacuerdo',
        5 : 'Un poco de acuerdo',
        6 : 'Moderadamente de acuerdo',
        7 : 'Totalmente de acuerdo'
    }

    tp = {
        "TIPI1"  : st.selectbox("Soy extravertido, entusiasta", options=options.values()),
        "TIPI2"  : st.selectbox("Soy críticón, peleón", options=options.values()),
        "TIPI3"  : st.selectbox("Soy confiable, tengo autocontrol", options=options.values()),
        "TIPI4"  : st.selectbox("Soy ansioso, irascible", options=options.values()),
        "TIPI5"  : st.selectbox("Estoy abierto a nuevas experiencias, tengo intereses variados", options=options.values()),
        "TIPI6"  : st.selectbox("Soy reservado, callado", options=options.values()),
        "TIPI7"  : st.selectbox("Soy simpático, cálido", options=options.values()),
        "TIPI8"  : st.selectbox("Soy desorganizado, descuidado", options=options.values()),
        "TIPI9"  : st.selectbox("Soy calmado, emocionalmente estable", options=options.values()),
        "TIPI10" : st.selectbox("Soy convencional, poco creativo", options=options.values())
    }
    
    tipi_response = reverse(options,tp)
    return tipi_response

def vcl():

    options = {1: 'Si', 2: 'No'}

    vcl={
        'VCL1': st.radio(label='**BARCO**',options=options.values(), horizontal=True),
        'VCL2': st.radio(label='**INCOHERENTE**',options=options.values(), horizontal=True),
        'VCL3': st.radio(label='**PÁLIDO**',options=options.values(), horizontal=True),
        'VCL4': st.radio(label='**ROBOT**',options=options.values(), horizontal=True),
        'VCL5': st.radio(label='**AUDIBLE**',options=options.values(), horizontal=True),
        'VCL6': st.radio(label='**CUIVOCAL**',options=options.values(), horizontal=True),
        'VCL7': st.radio(label='**ESCASEZ**',options=options.values(), horizontal=True),
        'VCL8': st.radio(label='**EPISTEMIOLOGÍA**',options=options.values(), horizontal=True),
        'VCL9': st.radio(label='**FILTEO**',options=options.values(), horizontal=True),
        'VCL10': st.radio(label='**DECIDIR**',options=options.values(), horizontal=True),
        'VCL11': st.radio(label='**PASTICHE**',options=options.values(), horizontal=True),
        'VCL12': st.radio(label='**VERDID**',options=options.values(), horizontal=True),
        'VCL13': st.radio(label='**ABISMAL**',options=options.values(), horizontal=True),
        'VCL14': st.radio(label='**LÚCIDO**',options=options.values(), horizontal=True),
        'VCL15': st.radio(label='**TRAICIONAR**',options=options.values(), horizontal=True),
        'VCL16': st.radio(label='**DIVERTIDO**',options=options.values(), horizontal=True),
    }

    vcl_response=reverse(options,vcl)
    
    return vcl_response

def demographic():

    options1 = {1: 'Por debajo de la E.S.O', 2: 'E.S.O completa', 3: 'Grado universitario', 4:'Postgrado'}
    options2 = {1: 'Rural', 2: 'Pueblo mediano/grande', 3: 'Ciudad'}
    options3 = {1: 'Femenino', 2: 'Masculino', 3: 'Otro'}
    options4 = {1: 'Si', 2: 'No'}
    options5 = {1: 'Diestro', 2: 'Zurdo', 3: 'Ambidiestro'}
    options6 = {1: 'Agnóstico', 2: 'Ateo', 3: 'Budista', 4: 'Cristiano católico', 5: 'Cristiano mormón', 6: 'Cristiano Protestante', 7: 'Otro tipo de cristianismo', 8: 'Hindú', 9: 'Judío', 10: 'Musulmán', 11: 'Sikh', 12: 'Otro'}
    options7 = {1: 'Heterosexual', 2:'Bisexual', 3: 'Homosexual', 4: 'Asexual', 5: 'Otros'}
    options8 = {1: 'Asiático', 2: 'Árabe', 3: 'Negro', 4: 'Indígena Australiano', 5: 'Nativo Americano', 6: 'Caucásico', 0: 'Otro'}
    options9 = {1: 'Soltero', 2: 'Casado', 3: 'Divorciado'}
    options10 = {1: 'Ciencias', 2: 'Ciencias de la salud', 3: 'Empresariales', 4: 'Ingeniería', 5: 'Humanidades y letras', 6: 'Arte', 7: 'Tecnología', 8: 'IT', 9: 'Turismo', 10: 'Otros'}

    dmg = {
        "education": st.selectbox("¿Qué nivel educacional tienes completo?",options=options1.values()),
        "urban": st.selectbox("¿En qué tipo de area te criaste de pequeño?", options=options2.values()),
        "gender": st.selectbox("¿Con qué género te identificas?", options=options3.values()),
        "engnat": st.radio("¿Eres hablante de inglés nativo?", options=options4.values(), horizontal=True),
        "age": st.slider("Por favor, indique su edad:", min_value=18, max_value=100, value=25, step=1),
        "hand": st.selectbox("¿Cual es tu mano predominante?", options=options5.values()),
        "religion": st.selectbox("¿Eres creyente?", options=options6.values()),		
        "orientation": st.selectbox('¿Cual es tu orientación sexual?', options=options7.values()),
        "race": st.selectbox("¿Cual es tu origen étnico?", options=options8.values()),
        "voted": st.radio("¿Has votado en las últimas elecciones?", options=options4.values(), horizontal=True),
        "married": st.selectbox("¿Cual es tu estado civil?", options=options9.values()),
        "familysize": st.slider("Incluyéndote a ti mismo, ¿cuántos hijos tuvo tu madre?", min_value=1, max_value=15, value=1, step=1),
        "major": st.selectbox("Si has terminado una carrera universitaria, ¿Cuál fué tu rama? (por ejemplo: Psicología, Ingeniería, Historia, Medicina...)", options=options10.values())
    }


    options1_reverse = {v: k for k, v in options1.items()}
    options2_reverse = {v: k for k, v in options2.items()}
    options3_reverse = {v: k for k, v in options3.items()}
    options4_reverse = {v: k for k, v in options4.items()}
    options5_reverse = {v: k for k, v in options5.items()}
    options6_reverse = {v: k for k, v in options6.items()}
    options7_reverse = {v: k for k, v in options7.items()}
    options8_reverse = {v: k for k, v in options8.items()}
    options9_reverse = {v: k for k, v in options9.items()}
    options10_reverse = {v: k for k, v in options10.items()}

    dmg_responses = {
        "education": options1_reverse[dmg["education"]],
        "urban": options2_reverse[dmg["urban"]],
        "gender": options3_reverse[dmg["gender"]],
        "engnat": options4_reverse[dmg["engnat"]],
        "age": dmg["age"],
        "hand": options5_reverse[dmg["hand"]],
        "religion": options6_reverse[dmg["religion"]],
        "orientation": options7_reverse[dmg["orientation"]],
        "race": options8_reverse[dmg["race"]],
        "voted": options4_reverse[dmg["voted"]],
        "married": options9_reverse[dmg["married"]],
        "familysize": dmg["familysize"],
        "major": options10_reverse[dmg["major"]]
    }

    return dmg_responses

def escala_beck():

    col1, col2 = st.columns([0.75,0.25])

    with col1:
        st.title("Escala de Beck sobre Ansiedad, Estrés y Depresión")
        st.subheader(":blue[Evaluación de Ansiedad, Estrés y Depresión]")
        st.markdown("En esta sección, responderás a una serie de preguntas basadas en la Escala de Beck, diseñada para medir la intensidad de tus sentimientos de ansiedad, estrés y depresión en la última semana.")
        st.markdown("""
    ### :blue[¿Qué Es la Escala de Beck?]

    La Escala de Beck es una herramienta ampliamente utilizada en la psicología para evaluar el nivel de malestar emocional. Cada pregunta se refiere a una experiencia o sentimiento que podrías haber tenido recientemente. Responde a cada afirmación de manera honesta para obtener una evaluación precisa.""")

    with col2:
        st.text('\n')
        
        image_path = "images/cabeza_universo.png"
        
        if image_path:
            st.image(image_path, use_column_width=True)
        else:
            st.write(f"Archivo no encontrado")

    st.markdown("""
    ### :blue[¿Por Qué Es Importante?]

    Comprender tus niveles de ansiedad, estrés y depresión puede ayudarte a identificar áreas donde podrías necesitar apoyo o intervención. No hay respuestas correctas o incorrectas; lo importante es tu percepción y experiencia personal.
    """)

    st.write('**Comencemos con la encuesta, responde por favor con la mayor veracidad posible.**')
    response1 = qwerys()
    st.session_state.response1 = response1
    st.success('Una vez que termine, pase a la pestaña siguiente para continuar el cuestionario')


def ten_items():
    st.header('TIPI, inventario de la personalidad de 10 ítems')
    st.subheader(":blue[Evaluación de Personalidad TIPI]")
    st.markdown("""
    En esta sección, completarás el Inventario de Personalidad de 10 ítems (TIPI), que te ayudará a identificar tus principales rasgos de personalidad.

    ### ¿Qué Es el TIPI?

    El TIPI es una herramienta breve que clasifica tu personalidad en función de diez características clave. Te pediremos que indiques cómo de acuerdo estás con varias afirmaciones para obtener un perfil general de tu personalidad.

    ### ¿Por Qué Es Importante?

    Este inventario te proporciona una visión rápida y efectiva de tus rasgos de personalidad, lo cual puede ser útil para entender cómo te relacionas con los demás y cómo te enfrentas a diferentes situaciones. Es una excelente manera de conocer mejor tus propias características y patrones de comportamiento.
    """)
    response2 = tipi()

    st.session_state.response2 = response2

    image_path = "images/Inside_out.png"
    if image_path:
        st.image(image_path, use_column_width=True)
    else:
        st.write(f"Archivo no encontrado")

    st.success('Una vez que termine, puede ir a la pestaña Vocabulary Check List para continuar el cuestionario.')

def words():
    st.header('Sección VCL - Listado de Palabras')
    st.subheader(':blue[Evaluación del conocimiento del léxico]')
    st.markdown("""
    En esta sección, se te presentará un listado de palabras para evaluar tu conocimiento de las mismas.

    ### ¿Qué Es la Evaluación VCL?

    La Evaluación VCL (Vocabulary Check List) es una herramienta diseñada para medir tu conocimiento de una variedad de palabras. Te pediremos que indiques si reconoces o no cada palabra del listado presentado.

    ### ¿Por Qué Es Importante?

    Esta evaluación nos ayuda a entender mejor tu nivel de vocabulario y tu familiaridad con diferentes términos. El conocimiento de palabras es un indicador importante de habilidades lingüísticas y puede proporcionar información valiosa para la interpretación de los resultados generales de la encuesta DASS.

    ### ¿Cómo Funciona?

    A continuación, verás una lista de palabras. Para cada palabra, marca si la conoces o no. No te preocupes si no conoces todas las palabras, simplemente selecciona las que reconoces.

    ### Instrucciones

    Por favor, revisa cada palabra en la lista y selecciona si la conoces o no. Trata de ser lo más preciso posible para obtener una evaluación exacta de tu vocabulario.
    """)
    col1, col2 = st.columns([0.10,0.90])

    with col1:
        response3 = vcl()

    with col2: 
        image_path = "images/composiocion_2.jpg"
        if image_path:
            st.image(image_path, use_column_width=True)
        else:
            st.write(f"Archivo no encontrado")



    st.session_state.response3 = response3

    st.success('Una vez que termine, puede ir a la pestaña Demográficos para continuar el cuestionario.')

def demog():
    col1, col2 = st.columns([0.85,0.15])
    
    with col1:
        st.header('Datos del entorno y desarrollo personal')
        st.subheader(':blue[Información demográfica y contextual]')
        st.markdown('En esta última sección, te pediremos que proporciones información sobre tu entorno personal y desarrollo.')
        st.markdown('Esto incluye aspectos como tu nivel educativo, lugar de crianza, género, y otros detalles relevantes.')
        st.markdown(' ### ¿Qué información se solicita? ')
        st.markdown('Queremos conocer un poco más sobre ti para contextualizar mejor tus respuestas.')
        st.markdown('Esta información es clave para analizar los datos de manera más detallada y comprender las posibles variaciones en los resultados basadas en diferentes contextos demográficos.')
        st.markdown(' ### ¿Por qué es importante? ')
        st.markdown('Los datos demográficos ayudan a interpretar los resultados del cuestionario en función de tu trasfondo personal.')
        st.markdown('Esto permite una comprensión más rica y precisa de los resultados y puede ofrecer perspectivas adicionales sobre cómo los factores personales influyen en tus respuestas.')

    with col2:
        image_path = "images/demografico.png"
        if image_path:
            st.image(image_path, use_column_width=True)
        else:
            st.write(f"Archivo no encontrado")

    response4 = demographic()
    st.session_state.response4 = response4


    st.success('Una vez que termine, envíe el cuestionario y decida si quiere ver los resultados')

    if st.button('Enviar cuestionario'):
        if 'response1' in st.session_state and 'response2' in st.session_state and 'response3' in st.session_state and 'response4' in st.session_state:
            create_df(response())
            st.success('Respuestas enviadas con éxito.')
            st.session_state.questionnaire_submitted = True
    
        else:
            st.error('Por favor, complete las secciones anteriores antes de enviar.')


def response_q():
    if 'response1' in st.session_state and 'response2' in st.session_state and 'response3' in st.session_state and 'response4' in st.session_state:
        response_q={**st.session_state.response1}
        response_df=pd.DataFrame([response_q])
        return response_df
    return None

def response_t():
    if 'response1' in st.session_state and 'response2' in st.session_state and 'response3' in st.session_state and 'response4' in st.session_state:
        response_t={**st.session_state.response2}
        response_df=pd.DataFrame([response_t])
        return response_df
    return None

def response_firebase():
    if 'response1' in st.session_state and 'response2' in st.session_state and 'response3' in st.session_state and 'response4' in st.session_state:
        response={**st.session_state.response1, **st.session_state.response2, **st.session_state.response3, **st.session_state.response4}
        return response
    return None

def response():
    if 'response1' in st.session_state and 'response2' in st.session_state and 'response3' in st.session_state and 'response4' in st.session_state:
        r1=pd.DataFrame([st.session_state.response1])
        r2=pd.DataFrame([st.session_state.response2])
        r3=pd.DataFrame([st.session_state.response3])
        r4=pd.DataFrame([st.session_state.response4])
        response=pd.concat([r1,r2,r3,r4],axis=1)
        return response
    return None

def show_survey():

    st.session_state.completed_sections = 2
    
    if 'questionnaire_submitted' not in st.session_state:
        st.session_state.questionnaire_submitted = False
    
    tab1, tab2, tab3, tab4 = st.tabs(['**Escala de Beck**', '**Cuestionario de personalidad**','**Vocabulary Check List**', '**Datos del entorno demográfico**'])

    with tab1:
        escala_beck()

    with tab2:
        ten_items()

    with tab3:
        words()

    with tab4:
        demog()
       
    if st.session_state.questionnaire_submitted:
        visualizar_resultados = st.radio(
            '¿Ver resultados?',
            ['Sí', 'No'],
            index=1
        )
        
        if visualizar_resultados == 'Sí':

            tipi_personality=personality(response_t())
            fig = plot_radar_chart(tipi_personality)

            st.subheader(':blue[Rasgos de Personalidad según el Ten Items Personality Inventory]')

            st.plotly_chart(fig)

            analysis = personality_study(tipi_personality)
            st.markdown(analysis)
            
            st.subheader(':blue[Resultados de la encuesta Dass]')

            data= response_q()

            if data is not None:
                fig2 = conditions_plot(data)
                st.plotly_chart(fig2)

                st.markdown('La probabilidad de tener **ansiedad** es:')
                st.write(f'{anxiety_assessment(data)[0]}')
                st.markdown(f'La probabilidad de tener **estrés** es:')
                st.write(f'{stress_assessment(data)[0]}')
                st.markdown(f'La probabilidad de tener **depresión** es:')
                st.write(f'{depression_assessment(data)[0]}')
            else:
                st.error('Error al crear las respuestas, por favor, vuelve a intentarlo.')

        st.write('Muchísimas gracias por haber llegado hasta el final y haber completado el formulario.')
        st.write('Tu aportación nos ha sido de gran ayuda, esperamos que te haya sido intuitivo y fácil de rellenar')
        
        col1, col2, col3 = st.columns([0.3,0.4,0.3])

        with col2:

            image_path_ = "images/gracias.png"

            if image_path:
                st.image(image_path_, use_column_width=True)
            else:
                st.write(f"Archivo no encontrado")
                
