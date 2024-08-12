import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


# cred = credentials.Certificate(r"C:\Users\Jesús\Documents\BOOTCAMP\BOOTCAMP\proyecto_final-main\firestore-json-key.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()

# def importar_datos_firebase():
    
#     collection_ref = db.collection("responses")
#     docs = collection_ref.stream()
    

#     datos = []
    
#     for doc in docs:
#         st.write(f"Documento principal encontrado: {doc.id}")
        
#         # Asumimos que la subcolección tiene el mismo ID que el documento principal
#         subcollection_ref = collection_ref.document(doc.id).collections()
        
#         for subcollection in subcollection_ref:
#             sub_docs = subcollection.stream()
#             for sub_doc in sub_docs:
#                 st.write(f"Documento en subcolección encontrado: {sub_doc.id}")
#                 datos.append(sub_doc.to_dict())
    
#     st.write(f"Total de documentos encontrados en subcolecciones: {len(datos)}")
#     return datos

filepath = r'C:\Users\Jesús\Documents\BOOTCAMP\BOOTCAMP\proyecto_final-main\respuestas\respuestas_cuestionario.csv'
def load_data(filepath):
    return pd.read_csv(filepath)

# Function to identify false words
def func_identify_false_words(df, false_words):
           
    df['False_Words_Count'] = df[false_words].apply(lambda col : (col == 1).sum(), axis=1)
    df['False_Word'] = df['False_Words_Count'].apply(lambda x: 1 if x > 0 else 0)
    
    return df

def plot_dmg_1 (df):
    fig1 = px.scatter(df, x='gender', y='orientation', title='Relación género con orientación.')
    return fig1

def plot_dmg_2 (df):
    fig2 = px.histogram(df, x='age', title='Distribución por edad.')
    return fig2    

def plot_dmg_3 (df):
    fig3 = px.scatter(df, x='orientation', y= 'major', title= 'Relación entre religión y estudios')
    return fig3

# Gráfico palabras falsas
def barplot_vcl(df):
    false_words = ['VCL6', 'VCL9', 'VCL12']
    df = func_identify_false_words(df, false_words)
    
    # Contar cuántas veces las palabras falsas han sido marcadas como 1
    false_word_counts = df[false_words].apply(lambda col: (col == 1).sum())
    
    # Crear el gráfico de barras
    fig = px.bar(
        x = false_word_counts.index,
        y = false_word_counts.values,
        labels = {'x': 'Palabras Falsas', 'y': 'Cantidad de Veces Marcadas'},
        title = 'Frecuencia de Palabras Falsas Marcadas', 
    )
    return fig

#######################################################################################################

# Función para encontrar inconsistencias entre edad y educación
def func_find_age_education_inconsistencies(df):
    df = df.copy()
    inconsistencies = df[(df['age'] < 21) & (df['education'] > 2)]
    df['Inconsistency_Age_Education'] = 0
    df.loc[inconsistencies.index, 'Inconsistency_Age_Education'] = 1
    inconsistency_counts = df[df['Inconsistency_Age_Education'] == 1]['age'].value_counts().sort_index()
    return df, inconsistencies, inconsistency_counts

# Gráfico inconsistencias edad y educación
def plot_inconsistencies_by_age(inconsistency_counts):
    inconsistency_df = pd.DataFrame({
        'Edad': inconsistency_counts.index,
        'Cantidad de Inconsistencias': inconsistency_counts.values
    })
    fig = px.bar(
        inconsistency_df,
        x = 'Edad',
        y = 'Cantidad de Inconsistencias',
        title = 'Frecuencia de Inconsistencias entre edad y educación', 
        labels = {'x': 'Edad', 'y': 'Cantidad de Inconsistencias'}
    )
    st.plotly_chart(fig)
    
#######################################################################################################

# Function to display correlation matrix
def func_plot_correlation_matrix(df, columns, figsize = (32, 28), cmap = 'coolwarm', annot = True, fmt = '.2f', linewidths = 0.5, center = 0):

    plt.figure(figsize=figsize)
    correlation_matrix = df[columns].corr()
    sns.heatmap(correlation_matrix, cmap=cmap, annot=annot, fmt=fmt, linewidths=linewidths, center=center, annot_kws={'size':9})
    plt.title('Matriz de correlación', fontsize=20)
    plt.xticks(fontsize=10, rotation=90)
    plt.yticks(fontsize=10, rotation=0)
    st.pyplot(plt.gcf())
    
    return correlation_matrix

 
# Function to find related pairs
def func_find_related_pairs(correlation_matrix, columns, threshold = 0.6):
    pairs = []
    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            if abs(correlation_matrix.iloc[i, j]) >= threshold:
                pairs.append((columns[i], columns[j]))
    return pairs

# Function to detect inconsistencies
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

def plot_inconsistencies_by_related_pairs(inconsistencies):
    data = []
    for inconsistency in inconsistencies:
        q1 = inconsistency['question1']
        q2 = inconsistency['question2']
        count = len(inconsistency['contradictions'])
        data.append({'Pares': f'{q1} & {q2}', 'Cantidad de Inconsistencias': count})
    
    inconsistency_df = pd.DataFrame(data)

    if not inconsistency_df.empty:
        fig = px.bar(
            inconsistency_df,
            x = 'Pares',
            y = 'Cantidad de Inconsistencias',
            title = 'Cantidad de Inconsistencias por Pares Relacionados',
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