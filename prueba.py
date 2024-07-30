import streamlit as st 
import pandas as pd
import io
import os
from funciones import *

def tipi():

    options={
        1 : 'Muy en desacuerdo',
        2 : 'Moderadamente en desacuerdo',
        3 : 'Un poco en desacuerdo',
        4 : 'Ni de acuerdo ni en desacuerdo',
        5 : 'Un poco de acuerdo',
        6 : 'Moderadamente de acuerdo',
        7 : 'Totalmente de acuerdo'
    }

    tp = {
        "TIPI1"  : st.selectbox("Extravertido, entusiasta", options=options.values()),
        "TIPI2"  : st.selectbox("Críticón, peleón", options=options.values()),
        "TIPI3"  : st.selectbox("Confiable, con autocontrol", options=options.values()),
        "TIPI4"  : st.selectbox("Ansioso, irascible", options=options.values()),
        "TIPI5"  : st.selectbox("Abierto a nuevas experiencias, intereses variados", options=options.values()),
        "TIPI6"  : st.selectbox("Reservado, callado", options=options.values()),
        "TIPI7"  : st.selectbox("Simpático, cálido", options=options.values()),
        "TIPI8"  : st.selectbox("Desorganizado, descuidado", options=options.values()),
        "TIPI9"  : st.selectbox("Calmado, emocionalmente estable", options=options.values()),
        "TIPI10" : st.selectbox("Convencional, poco creativo", options=options.values())
    }
    
    tipi_response = reverse(options,tp)
    return tipi_response

def qwerys():

    options = {
        0 : 'Ninguna vez',
        1 : 'En ciertas ocasiones',
        2 : 'Bastantes veces',
        3 : 'Todos o la mayoría de los días'
    }

    qw = {
        "Q1" : st.selectbox("1 - Me he sentido molesto por cosas triviales", options=options.values()),
        "Q2" : st.selectbox("2 - He notado la boca seca", options=options.values()),
        "Q3" : st.selectbox("3 - Me ha costado mucho experimentar algún tipo de sentimientos positivos", options=options.values()),
        "Q4" : st.selectbox("4 - Experimenté dificultad para respirar (por ejemplo: respiración excesivamente rápida, falta de aire en ausencia de esfuerzo físico)", options=options.values()),
        "Q5" : st.selectbox("5 - He sentido que simplemente no podía continuar", options=options.values()),
        "Q6" : st.selectbox("6 - Tendía a reaccionar desmesuradamente a situaciones que no lo merecían", options=options.values()),
        "Q7" : st.selectbox("7 - He tenido sensación de temblores (por ejemplo: no me reaccionaban bien las extremidades)", options=options.values()),
        "Q8" : st.selectbox("8 - He tenido dificultades para relajarme/desconectar", options=options.values()),
        "Q9" : st.selectbox("9 - Me encontré en situaciones que me hacían sentir tan ansioso que he sentido alivio cuando estas han terminado", options=options.values()),
        "Q10": st.selectbox("10 - Sentí que no tenía nada por lo cual levantarme", options=options.values()),
        "Q11": st.selectbox("11 - Me he molestado con bastante facilidad", options=options.values()),
        "Q12": st.selectbox("12 - Sentí que utilicé demasiada energía", options=options.values()),
        "Q13": st.selectbox("13 - Me sentí triste y deprimido", options=options.values()),
        "Q14": st.selectbox("14 - Me encontré impaciente cuando tuve alguna demora (por ejemplo: tráfico, citas, filas, esperas)", options=options.values()),
        "Q15": st.selectbox("15 - Tuve momentos de debilidad", options=options.values()),
        "Q16": st.selectbox("16 - Sentí que perdí el interés en prácticamente todo", options=options.values()),
        "Q17": st.selectbox("17 - Sentí que no valía mucho como persona", options=options.values()),
        "Q18": st.selectbox("18 - Me sentí bastante sensible", options=options.values()),
        "Q19": st.selectbox("19 - Sudaba de forma notable (por ejemplo: sudor en las manos) en ausencia de temperaturas altas o desgaste físico", options=options.values()),
        "Q20": st.selectbox("20 - Sentí miedo sin una buena razón", options=options.values()),
        "Q21": st.selectbox("21 - Pensé que la vida no valía la pena", options=options.values()),
        "Q22": st.selectbox("22 - Me resultó difícil relajarme", options=options.values()),
        "Q23": st.selectbox("23 - Tuve dificultades para tragar", options=options.values()),
        "Q24": st.selectbox("24 - No pude disfrutar de las cosas que hice", options=options.values()),
        "Q25": st.selectbox("25 - Fui consciente del latido de mi corazón en ausencia de esfuerzo (por ejemplo, aumento de la frecuencia cardiaca)", options=options.values()),
        "Q26": st.selectbox("26 - Me sentí afligido y desanimado", options=options.values()),
        "Q27": st.selectbox("27 - Estaba muy irritable", options=options.values()),
        "Q28": st.selectbox("28 - Estuve cerca de entrar en pánico", options=options.values()),
        "Q29": st.selectbox("29 - Me resultó difícil calmarme después de molestarme por algo", options=options.values()),
        "Q30": st.selectbox("30 - Temía que me superara alguna tarea trivial pero desconocida para mí", options=options.values()),
        "Q31": st.selectbox("31 - Nada me generaba entusiasmo", options=options.values()),
        "Q32": st.selectbox("32 - Me resultó difícil tolerar interrupciones en lo que estaba haciendo", options=options.values()),
        "Q33": st.selectbox("33 - Me encontraba en un estado de tensión y nervios", options=options.values()),
        "Q34": st.selectbox("34 - Sentí que era bastante inútil", options=options.values()),
        "Q35": st.selectbox("35 - No toleraba nada que me impidiera continuar con lo que estaba haciendo", options=options.values()),
        "Q36": st.selectbox("36 - Me sentí aterrorizado", options=options.values()),
        "Q37": st.selectbox("37 - No veía nada en el futuro con lo que tener esperanza", options=options.values()),
        "Q38": st.selectbox("38 - Sentí que la vida no tenía sentido", options=options.values()),
        "Q39": st.selectbox("39 - Me sentí agitado", options=options.values()),
        "Q40": st.selectbox("40 - Me preocupaban situaciones en las que podría entrar en pánico y hacer el ridículo", options=options.values()),
        "Q41": st.selectbox("41 - Experimenté temblores (por ejemplo: en las manos)", options=options.values()),
        "Q42": st.selectbox("42 - Me resultaba difícil reunir iniciativa o motivación para hacer las cosas", options=options.values())
    }
    
    qwery_response=reverse(options,qw)
    print(qwery_response)
    return qwery_response

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
        "engant": st.selectbox("¿Eres hablante de inglés nativo?", options=options4.values()),
        "age": st.slider("Por favor, indique su edad:", min_value=18, max_value=100, value=25, step=1),
        "hand": st.selectbox("¿Cual es tu mano predominante?", options=options5.values()),
        "religion": st.selectbox("¿Eres creyente?", options=options6.values()),		
        "orientation": st.selectbox('¿Cual es tu orientación sexual?', options=options7.values()),
        "race": st.selectbox("¿Cual es tu origen étnico?", options=options8.values()),
        "voted": st.selectbox("¿Has votado en las últimas elecciones?", options=options4.values()),
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
        "engant": options4_reverse[dmg["engant"]],
        "hand": options5_reverse[dmg["hand"]],
        "religion": options6_reverse[dmg["religion"]],
        "orientation": options7_reverse[dmg["orientation"]],
        "race": options8_reverse[dmg["race"]],
        "voted": options4_reverse[dmg["voted"]],
        "married": options9_reverse[dmg["married"]],
        "major": options10_reverse[dmg["major"]],
        "age": dmg["age"],
        "familysize": dmg["familysize"]
    }

    return dmg_responses

def escala_beck():
    st.subheader(":blue[Escala de Beck sobre ansiedad, estrés y depresión]")
    st.markdown(
        "Por favor, lea atentamente y marque la respuesta,"
        "indicando cual de estas afirmaciones definiría mejor su **_última semana_**.\n"
        "No hay respuestas correctas o incorrectas.\n"
        "Trate de no gastar mucho tiempo en la respuesta a cada afirmación.\n"
    )

    responses = qwerys()
    st.session_state.response1 = pd.DataFrame([responses])
    st.success('Una vez que termine, pase a la pestaña TIPI para continuar el cuestionario')

    if st.button('Ir a TIPI'):
        st.session_state.page = 'TIPI'

def ten_items():
    st.subheader(':blue[TIPI, inventario de la personalidad de 10 ítems]')
    st.markdown("El siguiente inventario es para hacer una clasificación de personalidad.")
    st.markdown("Los ítems del Tipi se califican de la siguiente manera:\n"
                "Estoy ('_selección_') en que soy:________")
    
    responses = tipi()
    st.session_state.response2 = pd.DataFrame([responses])
    st.success('Una vez que termine, puede ir a la pestaña Demográficos para continuar el cuestionario.')

    if st.button('Ir a Demográficos'):
        st.session_state.page = 'Demográficos'

def demog():
    st.subheader(':blue[Datos del entorno y desarrollo personal]')
    st.markdown('Por favor, rellena los siguientes campos con datos lo más verídicos posible.')

    responses = demographic()
    st.session_state.response3 = pd.DataFrame([responses])
    st.success('Una vez que termine, envíe el cuestionario con el botón situado en el lateral')

    # VER RESULTADOS UNA VEZ SE ENVIA EL CUESTIONARIO
    if st.session_state.questionnaire_submitted:
        visualizar_resultados = st.radio(
            '¿Ver resultados?',
            ['Sí', 'No'],
            index = 1  # POR DEFECTO QUE NO SE VEAN LOS RESULTADOS
        )
        
        if visualizar_resultados == 'Sí':
            st.subheader('Resultados del Cuestionario')
            combined_response = pd.concat([st.session_state.response1, st.session_state.response2, st.session_state.response3], axis = 1)
            st.write(combined_response)

def principal():
    st.title(":violet[Proyecto Final: Cuestionario Dass]")
    st.text("Este cuestionario es totalmente voluntario y anónimo.\n"
            "Los datos facilitados serán utilizados únicamente con fines didácticos,\n"
            "como parte de un proyecto de análisis de datos.\n"
            "No serán difundidos ni publicados ningún tipo de dato personal.\n"
            "\n"
            "Gracias por participar")
    
def main():
    st.set_page_config(
        page_title="Proyecto DASS",
        page_icon=":star:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.sidebar.title('Menu')

    if 'page' not in st.session_state:
        st.session_state.page = 'Principal'
    
    if 'questionnaire_submitted' not in st.session_state:
        st.session_state.questionnaire_submitted = False

    # ACTUALIZAR EL SIDEBAR CUANDO SE CAMBIA DE PAGINA EN LOS BOTONES
    pagina = st.sidebar.selectbox(
        'Páginas',
        ['Principal', 'Escala de Beck', 'TIPI', 'Demográficos'],
        index = ['Principal', 'Escala de Beck', 'TIPI', 'Demográficos'].index(st.session_state.page)
    )
    
    # ACTUALIZAR LA PAGINA CUANDO SE CAMBIA DESDE EL SIDEBAR
    if pagina != st.session_state.page:
        st.session_state.page = pagina

    if st.session_state.page == 'Principal':
        principal()
    elif st.session_state.page == 'TIPI':
        ten_items()
    elif st.session_state.page == 'Demográficos':
        demog()
    elif st.session_state.page == 'Escala de Beck':
        escala_beck()

    if st.sidebar.button('Enviar cuestionario completo'):
        if 'response1' in st.session_state and 'response2' in st.session_state and 'response3' in st.session_state:
            combined_response = pd.concat([st.session_state.response1, st.session_state.response2, st.session_state.response3], axis=1)
            create_csv_file(combined_response)
            st.success('Respuestas enviadas con éxito.')
            st.session_state.questionnaire_submitted = True
        else:
            st.error('Por favor, complete las secciones anteriores antes de enviar.')

if __name__ == "__main__":
    main()