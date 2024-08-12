import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from func_segunda_app import *
import pandas as pd
import seaborn as sns 


def main():
    
    st.title(":violet[Proyecto Final: Cuestionario DASS]")
    st.markdown("""
                
    A continuación presentamos las conclusiones del estudio que hemos hecho con respuestas de conocidos:
    
    """)

    mostrar_datos()

#     st.title("Datos desde Firebase")
    
#     datos=importar_datos_firebase()

#     df = pd.DataFrame(datos)

#     st.write('Respuestas de los ususarios: ')
#     st.dataframe(df)

#     st.write(df.describe())
  
#     #Resumen de los datos demográficos principales de la gente que ha respondido
    
#     col1, col2, col3 = st.columns(3)
    
#     with col1: 
#         st.plotly_chart(plot_dmg_1(df), use_container_width=True)
        
#     with col2:
#         st.plotly_chart(plot_dmg_2(df), use_container_width=True)
    
#     with col3: 
#         st.plotly_chart(plot_dmg_3(df), use_container_width=True)
  
#     # Aplicar función palabras falsas
#     df = func_identify_false_words(df, false_words = ['VCL6', 'VCL9', 'VCL12'])
#     st.dataframe(df)
    
#     # Gráfico de barras con las palabras falsas
#     fig = barplot_vcl(df)
#     st.plotly_chart(fig)

#     # Aplicar la función incosistencia edad y educación
#     df, inconsistencies, inconsistency_counts = func_find_age_education_inconsistencies(df)
#     st.dataframe(df)
    
#     # Mostrar el gráfico de inconsistencias por edad
#     plot_inconsistencies_by_age(inconsistency_counts)
    
#     columns_questions = [f'Q{i}' for i in range(1, 43)]
#     correlation_matrix = func_plot_correlation_matrix(df, columns_questions)

#     related_pairs = func_find_related_pairs(correlation_matrix, columns_questions)
#     df, inconsistencies = func_detect_inconsistencies(df, related_pairs)
#     st.dataframe(df)
#     plot_inconsistencies_by_related_pairs(inconsistencies)
    
    
    
#     # columns_questions = [f'Q{i}A' for i in range(1, 43)]
#     # correlation_matrix = func_plot_correlation_matrix(df, columns_questions)

#     # related_pairs = func_find_related_pairs(correlation_matrix, columns_questions)
#     # df, inconsistencies = func_detect_inconsistencies(df, related_pairs)
#     # st.dataframe(df)
#     # plot_inconsistencies_by_related_pairs(inconsistencies)
    
    
    
if __name__ == "__main__":
    main()