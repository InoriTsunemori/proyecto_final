import os
import pandas as pd
import pickle 
import streamlit as st
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import pipDense, Input
# from tensorflow.keras.utils import to_categorical

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, log_loss, roc_auc_score, classification_report, r2_score, root_mean_squared_error, mean_squared_error, mean_absolute_error

# def read_data():
#     csv = os.chdir(r'C:\Users\Jesús\Documents\BOOTCAMP\BOOTCAMP\proyecto_final-main\respuestas\respuestas_cuestionario.csv')
    
#     df = pd.read_csv(csv, encoding= 'latin1', header = 1)    
#     df.columns = ['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22',
#                   'Q23','Q24','Q25','Q26','Q27','Q28','Q29','Q30','Q31','Q32','Q33','Q34','Q35','Q36','Q37','Q38','Q39','Q40','Q41','Q42',
#                   'TIPI1','TIPI2','TIPI3','TIPI4','TIPI5','TIPI6','TIPI7','TIPI8','TIPI9','TIPI10',
#                   'education','urban','gender','engant','hand','religion','orientation','race','voted','married','major','age','familysize']
    
    # df.drop_duplicates(inplace=True)
       
    
def separarQ(lista,df):
        
    lista2 = []
            
    for n in lista: 
        numero = f'Q{n}'
        lista.append(numero)
        nuevo_Q= df[lista2]
            
    return nuevo_Q

       
def valorar ():
    
    os.chdir(r'C:\Users\Jesús\Documents\BOOTCAMP\BOOTCAMP\proyecto_final-main\respuestas')
    df = pd.read_csv('respuestas_cuestionario.csv')
    Q = df.iloc[:, :42]

    anxiety_list=[ 2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41]
    depression_list=[3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]
    stress_list= [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]
        
    ansiedad = separarQ(anxiety_list, Q)
    estres = separarQ(stress_list, Q)
    depresion = separarQ(depression_list, Q)
                
    Q['Suma Estrés']=((ansiedad.sum(axis=1))-14)
    Q['Suma Depresión']=((depresion.sum(axis=1))-14)
    Q['Suma Ansiedad']=((estres.sum(axis=1))-14)
    
    valoracion=[]
    for n in Q['Suma Depresión']:

        if n <=9:
                valoracion.append('Ninguna')
        elif n in range(10,14):
                valoracion.append('Muy leve')
        elif n in range(14,21):
                valoracion.append('Leve / Moderada')
        elif n in range(21,28):
                valoracion.append('Importante')
        elif n >= 28:
                valoracion.append('Grave')
        else: valoracion.append('Error de conteo')

    Q['Valoracion Depresión']=(valoracion)


    valoracion=[]
    for n in Q['Suma Ansiedad']:

        if n <=7:
                valoracion.append('Ninguna')
        elif n in range(8,10):
                valoracion.append('Muy leve')
        elif n in range(10,15):
                valoracion.append('Leve / Moderada')
        elif n in range(15,20):
                valoracion.append('Importante')
        elif n >= 20:
                valoracion.append('Grave')
        else: valoracion.append('Error de conteo')

    Q['Valoracion Ansiedad']=(valoracion)


    valoracion=[]
    for n in Q['Suma Estrés']:

        if n <=14:
                valoracion.append('Ninguna')
        elif n in range(15,19):
                valoracion.append('Muy leve')
        elif n in range(19,26):
                valoracion.append('Leve / Moderada')
        elif n in range(26,34):
                valoracion.append('Importante')
        elif n >= 34:
                valoracion.append('Grave')
        else: valoracion.append('Error de conteo')

    Q['Valoracion Estrés']=(valoracion)
        
        #Algoritmo estrés
        
    encoder=LabelEncoder()
    normalizador = StandardScaler()

    Q['Valoracion Estrés']=encoder.fit_transform(Q['Valoracion Estrés'])

    X_estres=np.array(Q.drop('Valoracion Estrés', axis=1))
    y_estres=np.array(Q['Valoracion Estrés'])

    X_estres = normalizador.fit_transform(X_estres)
 
    X_train_estres, X_test_estres, y_train_estres, y_test_estres = train_test_split(X_estres,y_estres, 
    
    
    modelLR=LogisticRegression(solver='lbfgs',max_iter=200)

    modelLR.fit(X_train_estres,y_train_estres)

    y_pred_estres = modelLR.predict(X_test_estres)
    y_pred_prob_estres = modelLR.predict_proba(X_test_estres)

    accuracy_estres = accuracy_score(y_test_estres, y_pred_estres)
    precision_estres = precision_score(y_test_estres, y_pred_estres, average='macro')
    recall_estres = recall_score(y_test_estres, y_pred_estres, average='macro')
    f1_estres = f1_score(y_test_estres, y_pred_estres, average='macro')                                                                               test_size=0.25,random_state=42)

        #Algoritmo ansiedad

    Q['Valoracion Ansiedad']=encoder.fit_transform(Q['Valoracion Ansiedad'])

    X_ansiedad=np.array(Q.drop('Valoracion Ansiedad', axis=1))
    y_ansiedad=np.array(Q['Valoracion Ansiedad'])

    X_ansiedad = normalizador.fit_transform(X_ansiedad)

    X_train_ansiedad, X_test_ansiedad, y_train_ansiedad, y_test_ansiedad = train_test_split(X_ansiedad,y_ansiedad, 
                                                                                            test_size=0.25,random_state=42)
    
    modelLR=LogisticRegression(solver='lbfgs',max_iter=200)

    modelLR.fit(X_train_ansiedad,y_train_ansiedad)

    y_pred_ansiedad = modelLR.predict(X_test_ansiedad)
    y_pred_prob_ansiedad = modelLR.predict_proba(X_test_ansiedad)

    accuracy_ansiedad = accuracy_score(y_test_ansiedad, y_pred_ansiedad)
    precision_ansiedad = precision_score(y_test_ansiedad, y_pred_ansiedad, average='macro')
    recall_ansiedad = recall_score(y_test_ansiedad, y_pred_ansiedad, average='macro')
    f1_ansiedad = f1_score(y_test_ansiedad, y_pred_ansiedad, average='macro')
    
    