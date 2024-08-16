import streamlit as st
import pandas as pd
import numpy as np
from func import *



def show_graphs():

    st.session_state.completed_sections = 3

    df=mostrar_datos()
    df=data_sum(df)
    df_personality=df_create(df)
    df_completo = pd.concat([df,df_personality], axis=1)
      
    #Mapeo para cambiar el nombre de las columnas
    
    cols_map = {'age' : 'Edad', 
                'major' : 'Licenciatura', 
                'gender' : 'Género',
                'orientation' : 'Orientación sexual', 
                'hand' : 'Mano predominante', 
                'Anxiety' : 'Ansiedad', 
                'Stress' : 'Estrés',
                'Depression' : 'Depresión'}
    
    df_completo = df_completo.rename(columns=cols_map)

    columns = ['Edad', 'Licenciatura', 'Género', 'Orientación sexual', 'Mano predominante','Extraversión', 'Amabilidad', 'Responsabilidad', 'Neuroticismo', 'Apertura_exp','Ansiedad','Estrés','Depresión']
    
    with st.sidebar:
        option = st.selectbox('**Elige una opción:**', ['Análisis de inconsistencias', 'Crea tu propio gráfico'])

        if option == 'Crea tu propio gráfico':
            chart_type = st.selectbox('**:blue[Selecciona el tipo de gráfico que deseas para la visualización]**', ['Dispersión', 'Barras'], key='chart_type')

            if chart_type == 'Dispersión':
                x_col = st.selectbox(':blue[Selecciona la variable para el eje X]', columns, key='x_col_disp')
                y_col = st.selectbox(':blue[Selecciona la variable para el eje Y]', columns, key='y_col_disp')
                colors = st.selectbox(':blue[Selecciona la variable para el color]', columns, key='color')

            elif chart_type == 'Barras':
                x_col = st.selectbox('Selecciona la variable para el eje X', columns, key='x_col_bar')
                y_col = st.selectbox('Selecciona la variable para el eje Y', columns, key='y_col_bar')
                colors = st.selectbox(':blue[Selecciona la variable para el color]', columns, key='color_bar')

    if option == 'Crea tu propio gráfico':
        if chart_type and x_col and y_col:
            example_graphs(df_completo, x_col, y_col, colors, chart_type)
        else:
            st.write('No hay gráficas que mostrar')

    elif option == 'Análisis de inconsistencias':
        st.title('Análisis de inconsistencias: ')
        tabs = st.tabs(['Matriz de correlación', 'Palabras Falsas' , 'Relación edad/educación', 'Pregustas incompatibles'])

        with tabs[0]:
            st.header('Análisis de inconsistencias a través de la matriz de correlación')
            st.markdown("""La matriz de correlación permite identificar el grado de relación entre las diferentes preguntas del cuestionario.
                        Este análisis es clave para detectar inconsistencias y respuestas contradictorias en preguntas que son similares entre sí.""")
                        
            columns_questions = [f'Q{i}A' for i in range(1, 43)]
            func_plot_correlation_matrix(df, columns_questions, show_plot = True)
                        
        with tabs[1]:
            st.header('Análisis de palabras falsas')
            st.write('En este apartado podemos ver cuánta gente ha indicado que conoce las palabras **"Cuivocal"**, **"Filteo"** y **"Verdid"**.\nEstas palabras no existen y han sido creadas con el único propósito de comprobar inconsistencias en las respuestas del cuestionario.')

            df = func_identify_false_words(df, false_words = ['VCL6', 'VCL9', 'VCL12'])
            fig = func_barplot_vcl(df)
            fig_pie = func_nested_pie_vcl(df)
            
            col1, col2 = st.columns([2, 2])
            with col1:
                st.subheader('\n')
                st.markdown("""
                ### Palabras Inexistentes en el Cuestionario \n\n

                En el cuestionario se incluyeron doce palabras, de las cuales tres son inventadas. \n
                El gráfico a continuación muestra la frecuencia con la que estas palabras inexistentes fueron marcadas como conocidas por los participantes.\n           
                """)
            with col2:
                st.plotly_chart(fig_pie, use_container_width = True)
            
            st.plotly_chart(fig)
           
        with tabs[2]:
            st.header('Análisis de inconsistencias en la edad y el nivel educativo del usuario')
            st.write('En este apartado podemos ver las respuestas de personas que no son posibles o incompatibles entre sí teniendo en cuenta la edad del usuario y su nivel educativo.')
            
            _, _, inconsistency_counts = func_find_age_education_inconsistencies(df)
            fig = func_plot_age_education_inconsistencies(inconsistency_counts)
            fig_pie = func_plot_age_education_inconsistencies_pie(df)
            
            col1, col2 = st.columns([2, 2])
            with col1:
                st.subheader('\n')
                st.markdown("""
                ### Inconsistencias entre Edad y Nivel de Estudios

                En este análisis, consideramos la relación entre la edad del individuo y su nivel educativo para evaluar la verosimilitud de los datos proporcionados.
                """)
            with col2:
                st.plotly_chart(fig_pie, use_container_width = True)
            
            st.plotly_chart(fig)

        with tabs[3]:
            st.header('Análisis de inconsistencias en las preguntas respondidas')
                       
            columns_questions = [f'Q{i}A' for i in range(1, 43)]
            correlation_matrix = func_plot_correlation_matrix(df, columns_questions, show_plot = False)
                
            related_pairs = func_find_related_pairs(correlation_matrix, columns_questions)
            df, inconsistencies = func_detect_inconsistencies(df, related_pairs)
            fig_pie = func_nested_pie_related_pairs(df, inconsistencies)
            
            col1, col2 = st.columns([2, 2])
            with col1:
                st.subheader('\n')
                st.markdown("""
                ### Pares Relacionados

                La matriz de correlación nos permite clasificar las preguntas en pares según su nivel de correlación. \n
                En el gráfico siguiente, se muestra la frecuencia con la que se han dado respuestas completamente contradictorias en pares de preguntas muy similares.
                    
                """)
                st.subheader('\n')
                        
            with col2:
                st.plotly_chart(fig_pie, use_container_width = True)
                    
            func_plot_inconsistencies_related_pairs(inconsistencies)
                           
def example_graphs(df_completo, x_col, y_col, colors, chart_type):

    st.header(f'Gráfica seleccionada: {chart_type}')

    legend_map = {'Género' : { 1 : 'Hombre', 
                              2 : 'Mujer', 
                              3 : 'Otros'}, 
                  'Orientación sexual' : {1 : 'Heterosexual', 
                                          2 : 'Bisexual', 
                                          3 : 'Homosexual', 
                                          4 : 'Asexual', 
                                          5 : 'Otros'},
                  'Mano predominante' : {1 : 'Diestro', 
                                         2 : 'Zurdo', 
                                         3 : 'Ambidiestro'}, 
                  
                  'Licenciatura' : {1: 'Ciencias', 
                                     2: 'Ciencias de la salud', 
                                     3: 'Empresariales', 
                                     4: 'Ingeniería', 
                                     5: 'Humanidades y letras', 
                                     6: 'Arte', 
                                     7: 'Tecnología', 
                                     8: 'IT', 
                                     9: 'Turismo', 
                                     10: 'Otros'}
                }

    if colors in legend_map:
        df_completo[colors] = df_completo[colors].map(legend_map[colors])

    if chart_type == 'Dispersión':
        
        fig = px.scatter(df_completo, 
                         x=x_col,
                         y=y_col, 
                         color=colors, 
                         title= f'Gráfico de dispersión con las variables {x_col} y {y_col}.', 
                        #  labels= {x: x, y: y},
                         color_continuous_scale='tealgrn_r')
        
        fig.update_layout(xaxis_title=f'EJE X {x_col}',
                          yaxis_title=f'EJE Y {y_col}', 
                          legend_title_text=f'{colors}')


    elif chart_type == 'Barras':
        fig = px.bar(df_completo,
                     x=x_col,
                     y=y_col, 
                     color=colors,
                     title=f'Gráfico de barras con las variables {x_col} y {y_col}.',
                    #  labels={x: f'EJE X: {x}', y: f'EJE Y: {y}'},
                     color_continuous_scale='tealgrn_r')


        fig.update_layout(xaxis_title=f'EJE X {x_col}',
                          yaxis_title=f'EJE Y {y_col}', 
                          legend_title_text=f'{colors}')

    st.plotly_chart(fig)

if __name__=="__main__":
    show_graphs()