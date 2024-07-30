import streamlit as st 
import pandas as pd
import io
import os

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
    
    items = {
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
    
    return items

def qwerys():
    options = {0 : 'Ninguna vez',
              1 : 'En ciertas ocasiones',
              2 : 'Bastantes veces',
              3 : 'Todos o la mayoría de los días'}
    
    options_reverse = {v: k for k, v in options.items()}
    
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
    
    qwery_response = {key: options_reverse[value] for key, value in qw.items()}
    
    return qwery_response

def demographic():
    options1 = {1: 'Por debajo de la E.S.O', 2: 'E.S.O completa', 3: 'Grado universitario', 4:'Postgrado'}
    options2 = {1: 'Rural', 2: 'Pueblo mediano/grande', 3: 'Ciudad'}
    options3 = {1: 'Femenino', 2: 'Masculino', 3: 'Otro'}
    options4 = {1: 'Si', 2: 'No'}
    options5 = {1: 'Diestro', 2: 'Zurdo', 3: 'Ambidiestro'}
    options6 = {1: 'Agnóstico', 2: 'Ateo', 3: 'Budista', 4: 'Cristiano católico', 5: 'Cristiano mormón', 6: 'Cristiano Protestante', 7: 'Otro tipo de cristianismo', 8: 'Hindú', 9: 'Judío', 10: 'Musulmán', 11: 'Otro tipo de religión'}

    # Datos demográficos
    st.selectbox("Nivel educativo", options=list(options1.values()), index=0)
    st.selectbox("Ubicación de residencia", options=list(options2.values()), index=0)
    st.selectbox("Sexo", options=list(options3.values()), index=0)
    st.selectbox("Tienes alguna discapacidad?", options=list(options4.values()), index=0)
    st.selectbox("Mano dominante", options=list(options5.values()), index=0)
    st.selectbox("Religión", options=list(options6.values()), index=0)

def create_csv_file(data):
    df = pd.DataFrame(data, index=[0])
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)
    
    file_path = "resultados.csv"
    with open(file_path, "w") as f:
        f.write(buffer.getvalue())

    st.success("Archivo CSV creado exitosamente")

def main():
    st.set_page_config(
        page_title="Proyecto DASS",
        page_icon=":star:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title(":violet[Proyecto Final: Cuestionario Dass]")

    st.text("Este cuestionario es totalmente voluntario y anónimo.\n"
            "Los datos facilitados serán utilizados únicamente con fines didácticos,\n"
            "como parte de un proyecto de análisis de datos.\n"
            "No serán difundidos ni publicados ningún tipo de dato personal.\n"
            "\n"
            "Gracias por participar")

    # Inicializa el estado de la pestaña si no está ya en el estado de la sesión
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = "Escala de Beck"

    # Crea el selector de pestañas
    tabs = ["Escala de Beck", "Tipi", "Datos demográficos"]
    st.session_state.current_tab = st.selectbox("Selecciona una pestaña", tabs, index=tabs.index(st.session_state.current_tab))

    if st.session_state.current_tab == "Escala de Beck":
        st.subheader(":blue[Escala de Beck sobre ansiedad, estrés y depresión]")
        st.markdown(
            "Por favor, lea atentamente y marque la respuesta,"
            "indicando cual de estas afirmaciones definiría mejor su **_última semana_**.  \n"
            "No hay respuestas correctas o incorrectas.  \n"
            "Trate de no gastar mucho tiempo en la respuesta a cada afirmación.  \n")
        
        response = qwerys()
        if st.button('Enviar'):
            create_csv_file(response)
            st.success('Respuestas guardadas en CSV con éxito.')

    elif st.session_state.current_tab == "Tipi":
        st.subheader(':blue[TIPI, inventario de la personalidad de 10 ítems]')
        st.markdown("El siguiente inventario es para hacer una clasificación de personalidad.")
        st.markdown("Los ítems del Tipi se califican de la siguiente manera:  \n"
                   "Estoy ('_selección_') en que soy:________")
        tipi()

    elif st.session_state.current_tab == "Datos demográficos":
        st.subheader(':blue[Datos del entorno y desarrollo personal]')
        st.markdown('Por favor, rellena los siguientes campos con datos lo más verídicos posible.')
        demographic()

if __name__ == "__main__":
    main()


# def main():

    
#     st.set_page_config(
#         page_title="Proyecto DASS",
#         page_icon=":star:",
#         layout="wide",
#         initial_sidebar_state="expanded")

#     st.title(":violet[Proyecto Final: Cuestionario Dass]")

#     st.text("Este cuestionario es totalmente voluntario y anónimo.\n"
#             "Los datos facilitados serán utilizados únicamente con fines didácticos,\n"
#             "como parte de un proyecto de análisis de datos.\n"
#             "No serán difundidos ni publicados ningún tipo de dato personal.\n"
#             "\n"
#             "Gracias por participar")
    

#     # Inicializa el estado de la pestaña si no está ya en el estado de la sesión
#     if 'current_tab' not in st.session_state:
#         st.session_state.current_tab = 0

#     # Crea las pestañas
#     tabs = ["Escala de Beck", "Tipi", "Datos demográficos"]
#     tab1, tab2, tab3 = st.tabs(tabs)

#     st.write(st.session_state)
#     # Controla qué pestaña se muestra
#     with [tab1, tab2, tab3][st.session_state.current_tab]:
#         if st.session_state.current_tab == 0:
#             st.subheader(":blue[Escala de Beck sobre ansiedad, estrés y depresión]")
#             st.markdown(
#                 "Por favor, lea atentamente y marque la respuesta,"
#                 "indicando cual de estas afirmaciones definiría mejor su **_última semana_**.  \n"
#                 "No hay respuestas correctas o incorrectas.  \n"
#                 "Trate de no gastar mucho tiempo en la respuesta a cada afirmación.  \n")
            
#             response = qwerys()
#             if st.button('Enviar'):
#                 create_csv_file(response)
#                 st.success('Respuestas guardadas en CSV con éxito.')

#             if st.button('Siguiente página'):
#                 st.session_state.current_tab = 1
#                 st.rerun()
#                 st.write(st.session_state)

#         elif st.session_state.current_tab == 1:
#             st.subheader(':blue[TIPI, inventario de la personalidad de 10 ítems]')
#             st.markdown("El siguiente inventario es para hacer una clasificación de personalidad.")
#             st.markdown("Los ítems del Tipi se califican de la siguiente manera:  \n"
#                        "Estoy ('_selección_') en que soy:________")
#             tipi()

#             if st.button('Siguiente página'):
#                 st.session_state.current_tab = 2
#                 st.rerun()
#                 st.write(st.session_state)

#             if st.button('Página anterior'):
#                 st.session_state.current_tab = 0
#                 st.rerun()
#                 st.write(st.session_state)

#         elif st.session_state.current_tab == 2:
#             st.subheader(':blue[Datos del entorno y desarrollo personal]')
#             st.markdown('Por favor, rellena los siguientes campos con datos lo más verídicos posible.')
#             demographic()

#             if st.button('Página anterior'):
#                 st.session_state.current_tab = 1
#                 st.rerun()

# if __name__ == "__main__":
#     main()
