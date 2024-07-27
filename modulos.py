import streamlit as st 
import streamlit.components.v1 as components
import pandas as pd

def main():

    st.title("Proyecto Final: Cuestionario Dass")

    st.text("Este cuestionario es totalmente voluntario y anónimo.\n"
            "Los datos facilitados serán utilizados únicamente con fines didácticos,\n"
            "como parte de un proyecto de análisis de datos.\n"
            "No serán difundidos ni publicados ningún tipo de dato personal.\n"
            "\n"
            "Gracias por participar")
    
    

    tab1, tab2, tab3 = st.tabs(["Escala de Beck", "Tipi", "Datos demográficos"])
    

    #-----------------------------------ESCALA BECK---------------------------------
    with tab1:

        st.subheader("Escala de Beck sobre ansiedad, estrés y depresión")

        st.text("\n"
            "Por favor, lea atentamente y marque la respuesta,\n"
            "indicando cual de estas afirmaciones definiría mejor su última semana. \n"
            "No hay respuestas correctas o incorrectas. \n"
            "Trate de no gastar mucho tiempo en la respuesta a cada afirmación. \n"
            "\n")
    
        st.subheader("La escala de calificación es la siguiente: \n")

        st.text("0  No me aplica en lo absoluto. \n"
            "1  Me aplica en cierta medida, o algunas veces. \n"
            "2  Me aplica considerablemente, o buena parte del tiempo. \n"
            "3  Me aplica mucho, o la mayoría de las veces. \n"
            "\n")
        qwerys()
    
    #-----------------------TIPI------------------------------------
        with tab2:
        
            st.subheader('TIPI, inventario de la personalidad de 10 ítems')

            st.text("El siguiente inventario es para hacer una clasificación de personalidad.")
            st.text("Los ítems del Tipi se califican de la siguiente manera: \n"
                      "Estoy (Puntuación) en que soy:________")
    

            st.text("Puntuación:\n"
                    "1 = Muy en desacuerdo.\n"
                    "2 = Moderadamente en desacuerdo.\n"
                    "3 = Un poco en desacuerdo.\n"
                    "4 = Ni de acuerdo ni en desacuerdo.\n"
                    "5 = Un poco de acuerdo.\n"
                    "6 = Moderadamente de acuerdo.\n"
                    "7 = Muy de acuerdo.")
    
            tipi()
    
#----------------------------DEMOGRAPHIC--------------------------------------
        with tab3:
            
            st.subheader('Datos del entorno y desarrollo personal.')
            st.text('Por favor, rellena los siguientes campos con datos lo más verídicos posible.')

            demographic()

def tipi():
    st.subheader('TIPI, inventario de la personalidad de 10 ítems')

    st.text("El siguiente inventario es para hacer una clasificación de personalidad.")
    st.text("Los ítems del Tipi se califican de la siguiente manera: \n"
            "Estoy (Puntuación) en que soy:________")
    

    st.text("Puntuación:\n"
            "1 = Muy en desacuerdo.\n"
            "2 = Moderadamente en desacuerdo.\n"
            "3 = Un poco en desacuerdo.\n"
            "4 = Ni de acuerdo ni en desacuerdo.\n"
            "5 = Un poco de acuerdo.\n"
            "6 = Moderadamente de acuerdo.\n"
            "7 = Muy de acuerdo.")

    options = [1, 2, 3, 4, 5, 6, 7]
    items = {
        "TIPI1"  : st.radio("Extravertido, entusiasta", options=options, index=0, horizontal=True),
        "TIPI2"  : st.radio("Críticón, peleón", options=options, index=0, horizontal=True),
        "TIPI3"  : st.radio("Confiable, con autocontrol", options=options, index=0, horizontal=True),
        "TIPI4"  : st.radio("Ansioso, irascible", options=options, index=0, horizontal=True),
        "TIPI5"  : st.radio("Abierto a nuevas experiencias, intereses variados", options=options, index=0, horizontal=True),
        "TIPI6"  : st.radio("Reservado, callado", options=options, index=0, horizontal=True),
        "TIPI7"  : st.radio("Simpático, cálido", options=options, index=0, horizontal=True),
        "TIPI8"  : st.radio("Desorganizado, descuidado", options=options, index=0, horizontal=True),
        "TIPI9"  : st.radio("Calmado, emocionalmente estable", options=options, index=0, horizontal=True),
        "TIPI10" : st.radio("Convencional, poco creativo", options=options, index=0, horizontal=True)}
    
    return items



def qwerys():

    options = [0, 1, 2, 3]

    qw = {
        "Q1" : st.radio("1 - Me he sentido molesto por cosas triviales", options=options, index=0, horizontal=True),
        "Q2" : st.radio("2 - He notado la boca seca", options=options, index=0, horizontal=True),
        "Q3" : st.radio("3 - Me ha costado mucho experimentar algún tipo de sentimientos positivos", options=options, index=0, horizontal=True),
        "Q4" : st.radio("4 - Experimenté dificultad para respirar (por ejemplo: respiración excesivamente rápida, falta de aire en ausencia de esfuerzo físico)", options=options, index=0, horizontal=True),
        "Q5" : st.radio("5 - He sentido que simplemente no podía continuar", options=options, index=0, horizontal=True),
        "Q6" : st.radio("6 - Tendía a reaccionar desmesuradamente a situaciones que no lo merecían", options=options, index=0, horizontal=True),
        "Q7" : st.radio("7 - He tenido sensación de temblores (por ejemplo: no me reaccionaban bien las extremidades)", options=options, index=0, horizontal=True),
        "Q8" : st.radio("8 - He tenido dificultades para relajarme/desconectar", options=options, index=0, horizontal=True),
        "Q9" : st.radio("9 - Me encontré en situaciones que me hacían sentir tan ansioso que he sentido alivio cuando estas han terminado", options=options, index=0, horizontal=True),
        "Q10": st.radio("10 - Sentí que no tenía nada por lo cual levantarme", options=options, index=0, horizontal=True),
        "Q11": st.radio("11 - Me he molestado con bastante facilidad", options=options, index=0, horizontal=True),
        "Q12": st.radio("12 - Sentí que utilicé demasiada energía", options=options, index=0, horizontal=True),
        "Q13": st.radio("13 - Me sentí triste y deprimido", options=options, index=0, horizontal=True),
        "Q14": st.radio("14 - Me encontré impaciente cuando tuve alguna demora (por ejemplo: tráfico, citas, filas, esperas)", options=options, index=0, horizontal=True),
        "Q15": st.radio("15 - Tuve momentos de debilidad", options=options, index=0, horizontal=True),
        "Q16": st.radio("16 - Sentí que perdí el interés en prácticamente todo", options=options, index=0, horizontal=True),
        "Q17": st.radio("17 - Sentí que no valía mucho como persona", options=options, index=0, horizontal=True),
        "Q18": st.radio("18 - Me sentí bastante sensible", options=options, index=0, horizontal=True),
        "Q19": st.radio("19 - Sudaba de forma notable (por ejemplo: sudor en las manos) en ausencia de temperaturas altas o desgaste físico", options=options, index=0, horizontal=True),
        "Q20": st.radio("20 - Sentí miedo sin una buena razón", options=options, index=0, horizontal=True),
        "Q21": st.radio("21 - Pensé que la vida no valía la pena", options=options, index=0, horizontal=True),
        "Q22": st.radio("22 - Me resultó difícil relajarme", options=options, index=0, horizontal=True),
        "Q23": st.radio("23 - Tuve dificultades para tragar", options=options, index=0, horizontal=True),
        "Q24": st.radio("24 - No pude disfrutar de las cosas que hice", options=options, index=0, horizontal=True),
        "Q25": st.radio("25 - Fui consciente del latido de mi corazón en ausencia de esfuerzo (por ejemplo, aumento de la frecuencia cardiaca)", options=options, index=0, horizontal=True),
        "Q26": st.radio("26 - Me sentí afligido y desanimado", options=options, index=0, horizontal=True),
        "Q27": st.radio("27 - Estaba muy irritable", options=options, index=0, horizontal=True),
        "Q28": st.radio("28 - Estuve cerca de entrar en pánico", options=options, index=0, horizontal=True),
        "Q29": st.radio("29 - Me resultó difícil calmarme después de molestarme por algo", options=options, index=0, horizontal=True),
        "Q30": st.radio("30 - Temía que me superara alguna tarea trivial pero desconocida para mí", options=options, index=0, horizontal=True),
        "Q31": st.radio("31 - Nada me generaba entusiasmo", options=options, index=0, horizontal=True),
        "Q32": st.radio("32 - Me resultó difícil tolerar interrupciones en lo que estaba haciendo", options=options, index=0, horizontal=True),
        "Q33": st.radio("33 - Me encontraba en un estado de tensión y nervios", options=options, index=0, horizontal=True),
        "Q34": st.radio("34 - Sentí que era bastante inútil", options=options, index=0, horizontal=True),
        "Q35": st.radio("35 - No toleraba nada que me impidiera continuar con lo que estaba haciendo", options=options, index=0, horizontal=True),
        "Q36": st.radio("36 - Me sentí aterrorizado", options=options, index=0, horizontal=True),
        "Q37": st.radio("37 - No veía nada en el futuro con lo que tener esperanza", options=options, index=0, horizontal=True),
        "Q38": st.radio("38 - Sentí que la vida no tenía sentido", options=options, index=0, horizontal=True),
        "Q39": st.radio("39 - Me sentí agitado", options=options, index=0, horizontal=True),
        "Q40": st.radio("40 - Me preocupaban situaciones en las que podría entrar en pánico y hacer el ridículo", options=options, index=0, horizontal=True),
        "Q41": st.radio("41 - Experimenté temblores (por ejemplo: en las manos)", options=options, index=0, horizontal=True),
        "Q42": st.radio("42 - Me resultaba difícil reunir iniciativa o motivación para hacer las cosas", options=options, index=0, horizontal=True)}

    return qw

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
        "education": st.radio("¿Qué nivel educacional tienes completo?",options=options1.values(), index=0, horizontal=True),
        "urban": st.radio("¿En qué tipo de area te criaste de pequeño?", options=options2.values(), index=0, horizontal=True),
        "gender": st.radio("¿Con qué género te identificas?", options=options3.values(), index=0, horizontal=True),
        "engant": st.radio("¿Eres hablante de inglés nativo?", options=options4.values(), index=0, horizontal=True),
        "age": st.slider("Por favor, indique su edad:", min_value=18, max_value=100, value=25, step=1),
        "hand": st.radio("¿Cual es tu mano predominante?", options=options5.values(), index=0, horizontal=True),
        "religion": st.radio("¿Eres creyente?", options=options6.values(), index=0, horizontal=True),		
        "orientation": st.radio('¿Cual es tu orientación sexual?', options=options7.values(), index=0, horizontal=True),
        "race": st.radio("¿Cual es tu origen étnico?", options=options8.values(), index=0, horizontal=True),
        "voted": st.radio("¿Has votado en las últimas elecciones?", options=options4.values(), index=0, horizontal=True),
        "married": st.radio("¿Cual es tu estado civil?", options=options9.values(), index=0, horizontal=True),
        "familiysize": st.slider("Incluyéndote a ti mismo, ¿cuántos hijos tuvo tu madre?", min_value=1, max_value=15, value=1, step=1),
        "major": st.text_input("Si has terminado una carrera universitaria, ¿Cuál fué tu rama? (por ejemplo: Psicología, Ingeniería, Historia, Medicina...)", max_chars=15)}
    
    return dmg





if __name__ == "__main__":
    main()
