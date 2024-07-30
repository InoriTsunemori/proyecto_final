import streamlit as st 
import pandas as pd
import io
import os

def tipi():

    options={1 : 'Muy en desacuerdo',
            2 : 'Moderadamente en desacuerdo',
            3 : 'Un poco en desacuerdo',
            4 : 'Ni de acuerdo ni en desacuerdo',
            5 : 'Un poco de acuerdo',
            6 : 'Moderadamente de acuerdo',
            7 : 'Totalmente de acuerdo'}
    
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
        "TIPI10" : st.selectbox("Convencional, poco creativo", options=options.values())}
    
    return items

def qwerys():

    options= {0 : 'Ninguna vez',
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
        "Q42": st.selectbox("42 - Me resultaba difícil reunir iniciativa o motivación para hacer las cosas", options=options.values())}
    
    qwery_response = {key: options_reverse[value] for key, value in qw.items()}

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


    dmg = {
        "education": st.selectbox("¿Qué nivel educacional tienes completo?",options=options1.values()),
        "urban": st.radio("¿En qué tipo de area te criaste de pequeño?", options=options2.values(), index=0, horizontal=True),
        "gender": st.radio("¿Con qué género te identificas?", options=options3.values(), index=0, horizontal=True),
        "engant": st.radio("¿Eres hablante de inglés nativo?", options=options4.values(), index=0, horizontal=True),
        "age": st.slider("Por favor, indique su edad:", min_value=18, max_value=100, value=25, step=1),
        "hand": st.radio("¿Cual es tu mano predominante?", options=options5.values(), index=0, horizontal=True),
        "religion": st.selectbox("¿Eres creyente?", options=options6.values()),		
        "orientation": st.selectbox('¿Cual es tu orientación sexual?', options=options7.values()),
        "race": st.selectbox("¿Cual es tu origen étnico?", options=options8.values()),
        "voted": st.radio("¿Has votado en las últimas elecciones?", options=options4.values(), index=0, horizontal=True),
        "married": st.radio("¿Cual es tu estado civil?", options=options9.values(), index=0, horizontal=True),
        "familiysize": st.slider("Incluyéndote a ti mismo, ¿cuántos hijos tuvo tu madre?", min_value=1, max_value=15, value=1, step=1),
        "major": st.text_input("Si has terminado una carrera universitaria, ¿Cuál fué tu rama? (por ejemplo: Psicología, Ingeniería, Historia, Medicina...)", max_chars=15)}
    
    return dmg

def menu():

    side=st.sidebar

def create_csv_file(data):
    # Define el directorio y el nombre del archivo
    DIRECTORIO_CSV = r'C:\Users\BORJA\OneDrive\Escritorio\HAB2\Proyecto_final\respuestas'
    NOMBRE_ARCHIVO = "respuestas_cuestionario.csv"
    
    if not os.path.exists(DIRECTORIO_CSV):
        os.makedirs(DIRECTORIO_CSV)
    

    ruta_csv = os.path.join(DIRECTORIO_CSV, NOMBRE_ARCHIVO)
    df = pd.DataFrame([data])

    if os.path.exists(ruta_csv):
        
        df.to_csv(ruta_csv, mode='a', header=False, index=False)
    else:
        
        df.to_csv(ruta_csv, mode='w', header=True, index=False)


def nueva_funcion():
    pas

def main():

    st.set_page_config(
        page_title="Proyecto DASS",
        page_icon=":star:",
        layout="wide",
        initial_sidebar_state="expanded")

    st.title(":violet[Proyecto Final: Cuestionario Dass]")

    st.text("Este cuestionario es totalmente voluntario y anónimo.\n"
            "Los datos facilitados serán utilizados únicamente con fines didácticos,\n"
            "como parte de un proyecto de análisis de datos.\n"
            "No serán difundidos ni publicados ningún tipo de dato personal.\n"
            "\n"
            "Gracias por participar")
    
    
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = 0
    
    tabs = ["Escala de Beck", "Tipi", "Datos demográficos"]
    tab1, tab2, tab3 = st.tabs(tabs)

    current_tab = st.session_state.current_tab

    # st.sidebar.title("Configuración")
    # st.sidebar.markdown("Ajustes del Cuestionario")

    # # Agregar Widgets al Sidebar
    # option = st.sidebar.selectbox('Seleccione una opción:', ['Opción 1', 'Opción 2', 'Opción 3'])
    # value = st.sidebar.slider('Seleccione un rango:', min_value=0, max_value=100, value=(25, 75))
    # text_input = st.sidebar.text_input('Ingrese su nombre:')
    # button = st.sidebar.button('Enviar')

    # with st.sidebar.expander("Configuraciones Avanzadas"):
    #     advanced_option = st.selectbox('Seleccione una opción avanzada:', ['Avanzada 1', 'Avanzada 2'])
    #     st.slider('Ajuste avanzado:', 0, 100, 50)

    if current_tab == 0:
        #-----------------------------------ESCALA BECK---------------------------------
        with tab1:

            st.subheader(":blue[Escala de Beck sobre ansiedad, estrés y depresión]")
            st.markdown(
                "Por favor, lea atentamente y marque la respuesta,"
                "indicando cual de estas afirmaciones definiría mejor su **_última semana_**.  \n"
                "No hay respuestas correctas o incorrectas.  \n"
                "Trate de no gastar mucho tiempo en la respuesta a cada afirmación.  \n")
        
            response = qwerys()


            if st.button('Enviar'):
                create_csv_file((response))
                st.success('Respuestas guardadas en CSV con éxito.')


            if st.button('Siguiente página'):
                st.session_state.current_tab = 1


    elif current_tab == 1:
    #-----------------------TIPI------------------------------------
        with tab2:

            st.subheader(':blue[TIPI, inventario de la personalidad de 10 ítems]')

            st.markdown("El siguiente inventario es para hacer una clasificación de personalidad.")
            st.markdown("Los ítems del Tipi se califican de la siguiente manera:  \n"
                    "Estoy ('_selección_') en que soy:________")
            
            tipi()

            if st.button('Siguiente página'):
                st.session_state.current_tab = 2

            if st.button('Página anterior'):
                st.session_state.current_tab = 0


    elif current_tab == 2:
        
#----------------------------DEMOGRAPHIC--------------------------------------
        with tab3:
                
            st.subheader(':blue[Datos del entorno y desarrollo personal]')
            st.markdown('Por favor, rellena los siguientes campos con datos lo más verídicos posible.')

            demographic()


            if st.button('Página anterior'):
                st.session_state.current_tab = 1

    if __name__ == "__main__":
        main()




    # def formulario():
    #     st.title("Cuestionario")
        
    #     # Definir las preguntas
    #     preguntas_tab1 = [f"Pregunta {i+1}" for i in range(42)]
    #     preguntas_tab2 = [f"Pregunta {i+1}" for i in range(10)]
    #     preguntas_tab3 = [f"Pregunta {i+1}" for i in range(15)]
        
    #     respuestas = {}

    #     # Crear pestañas
    #     tab1, tab2, tab3 = st.tabs(["Pestaña 1", "Pestaña 2", "Pestaña 3"])
        
    #     # Recoger respuestas de la Pestaña 1
    #     with tab1:
    #         for pregunta in preguntas_tab1:
    #             respuestas[pregunta] = st.text_input(pregunta)
        
    #     # Recoger respuestas de la Pestaña 2
    #     with tab2:
    #         for pregunta in preguntas_tab2:
    #             respuestas[pregunta] = st.text_input(pregunta)
        
    #     # Recoger respuestas de la Pestaña 3
    #     with tab3:
    #         for pregunta in preguntas_tab3:
    #             respuestas[pregunta] = st.text_input(pregunta)
        
    #     if st.button("Enviar"):
    #         # Convertir las respuestas a un DataFrame
    #         df_respuestas = pd.DataFrame([respuestas])
            
    #         # Si el archivo ya existe, agregar las nuevas respuestas
    #         if os.path.isfile(ruta_csv):
    #             df_existente = pd.read_csv(ruta_csv)
    #             df_final = pd.concat([df_existente, df_respuestas], ignore_index=True)
    #         else:
    #             df_final = df_respuestas
            
    #         # Guardar el DataFrame en un archivo CSV
    #         df_final.to_csv(ruta_csv, index=False)
    #         st.success("Respuestas guardadas correctamente")
            
    #         # Permitir la descarga del archivo CSV
    #         st.download_button(
    #             label="Descargar respuestas",
    #             data=df_final.to_csv(index=False).encode('utf-8'),
    #             file_name='respuestas_cuestionario.csv',
    #             mime='text/csv'
    #         )

    # if __name__ == "__main__":
    #     formulario()
