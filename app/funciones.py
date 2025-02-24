## LIBRERÍAS ##
# Data Analysis
import streamlit as st
import pandas as pd
import numpy as np

# Data Preproccesing
from collections import Counter
#from skimage.transform import resize

# Data Visualization
import matplotlib.pyplot as plt
from matplotlib.image import imread
from PIL import Image
#import cv2
import seaborn as sns

# Deep Learning (TensorFlow y tf.keras)
import tensorflow as tf
#import tensorflow_hub as hub
from skimage.transform import resize
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.utils import to_categorical

# Métrics
from sklearn.metrics import (confusion_matrix, classification_report, precision_recall_curve,
                            precision_score, recall_score,
                            f1_score, accuracy_score, roc_curve, auc)



# Mapeos de las clases
clases_a_cat = {0: 'Blight',
                1: 'Common_Rust',
                2: 'Gray_Leaf_Spot',
                3: 'Healthy'}


## PREPROCESAMIENTO ##

def preprocesamiento(imagen_cargada, img_width=224, img_height=224):
    """
    1°) Cargamos la imagen
    2°) Procesamos la imagen para adaptarla al modelo.
    """
    # Carga de imagen
    imagen = Image.open(imagen_cargada)
    st.image(imagen, caption="Imagen cargada", use_column_width=True)

    # Procesamiento de la imagen
    imagen = imagen.resize((img_width, img_height))  # Redimensionamos
    imagen_array = np.array(imagen).astype('float32') / 255.0  # Normalizamos
    imagen_array = np.expand_dims(imagen_array, axis=0)  # Agregamos dimensión para batch
    
    return imagen_array


## PREDICCIÓN ##

#def model():

def prediccion_y_probabilidad(imagen, modelo):
    '''
    Predecimos la clase de la imagen usando el modelo.
    Return:
        tuple: Clase predicha (str) y su probabilidad (float).
    '''
    # Realizamos la Prediccion:
    prediccion = modelo.predict(imagen)  # Probabilidades de cada clase

    # Encontramos el índice de la clase con mayor probabilidad:
    indice_clase_predicha = np.argmax(prediccion, axis=1)[0]  

    # Obtenemos el nombre de la clase predicha:
    clase_predicha = clases_a_cat[indice_clase_predicha]

    # Obtenemos la probabilidad asociada a la clase predicha:
    probabilidad = round(prediccion[0][indice_clase_predicha]*100,2)

    return clase_predicha, f"{probabilidad}%"  # Retorna la clase y su probabilidad (en %)


def plot_probabilidades(imagen, modelo):
    """
    Genera un gráfico de barras con las probabilidades de cada clase, ordenadas de mayor a menor.
    
    Parámetros:
        imagen (numpy.array): Imagen preprocesada lista para la predicción.
        modelo (tensorflow.keras.Model): Modelo de deep learning entrenado.
    """
    # Obtener predicciones del modelo
    predicciones = modelo.predict(imagen)
    probabilidades = predicciones[0]  # Extraemos la primera fila si es batch
    
    # Diccionario de clases
    clases = ['Blight', 'Common Rust', 'Gray Leaf Spot', 'Healthy']
    
    # Crear un DataFrame con las probabilidades
    df = pd.DataFrame({'Clase': clases, 'Probabilidad': probabilidades})
    df = df.sort_values(by='Probabilidad', ascending=False)  # Ordenar de mayor a menor
    
    fig, ax = plt.subplots(figsize=(8, 5))  
    sns.barplot(x=df['Probabilidad'], y=df['Clase'], palette='crest', ax=ax)
    ax.bar_label(ax.containers[0], fmt='%.3f')
    plt.xlabel('Probabilidad')
    plt.ylabel('Clase')
    plt.title('Probabilidad de cada enfermedad')

    return fig  # Retorna la figura en lugar de solo mostrarla

## DIAGNÓSTICO ##

def diagnóstico(imagen, modelo):
    '''
    1°) Obtenemos el indice de la clase predicha
    2°) Mostramos el Diagnóstico de la clase predicha
    '''
    # Indice de la clase con mayor probabilidad
    indice_clase_predicha = np.argmax(modelo.predict(imagen), axis=1)[0]  

    # Blight #
    if indice_clase_predicha == 0:
        st.markdown('### ⚠️ Su cultivo presenta enfermedad de:')
        st.subheader('`Blight (Marchitez de Stewart)`')

        st.markdown('##### **Tratamiento y manejo:**')
        st.markdown('* Rotación de cultivos con especies no hospedantes para reducir la carga de inóculo. ')
        st.markdown('* Uso de híbridos resistentes si están disponibles en la región.')
        st.markdown('* Aplicación de fungicidas específicos, especialmente en las primeras etapas del desarrollo de la enfermedad. Productos con ingredientes activos como estrobilurinas o triazoles pueden ser eficaces.')
        st.markdown('* Manejo del riego para evitar el exceso de humedad en la superficie foliar.')
        st.markdown('* Eliminación de residuos de cultivos infectados mediante labranza profunda o incorporación al suelo para reducir la fuente de inóculo.')

    # Common_Rust #
    if indice_clase_predicha == 1:
        st.markdown('### ⚠️ Su cultivo presenta enfermedad de:')
        st.subheader('`Common_Rust (Roya Común del Maíz)`')
        
        st.markdown('##### **Tratamiento y manejo:**')
        st.markdown('* Uso de híbridos resistentes o con mayor tolerancia a la enfermedad.')
        st.markdown('* Aplicación de fungicidas preventivos y curativos, especialmente en variedades susceptibles. Se recomiendan triazoles y estrobilurinas.')
        st.markdown('* Monitoreo constante del cultivo, especialmente en estadios de crecimiento crítico como V6-VT.')
        st.markdown('* Manejo de la densidad de siembra para evitar un microclima húmedo dentro del cultivo.')
        st.markdown('* Rotación de cultivos para reducir la acumulación del inóculo en la parcela.')

    # Gray_Leaf_Spot #
    if indice_clase_predicha == 2:
        st.markdown('### ⚠️ Su cultivo presenta enfermedad de:')
        st.subheader('`Gray_Leaf_Spot (Mancha Gris de la Hoja)`')
        
        st.markdown('##### **Tratamiento y manejo:**')
        st.markdown('* Uso de híbridos con resistencia genética para minimizar la incidencia de la enfermedad.')
        st.markdown('* Aplicación de fungicidas sistémicos, especialmente en estados tempranos de infección. Se recomiendan productos con ingredientes activos como estrobilurinas y triazoles.')
        st.markdown('* Reducción de la densidad de siembra para mejorar la circulación de aire y reducir la humedad en el follaje.')
        st.markdown('* Rotación de cultivos para evitar la acumulación de inóculo en el suelo.')
        st.markdown('* Eliminación de residuos de cultivos infectados mediante labranza o incorporación al suelo.')

    # Healthy #
    if indice_clase_predicha == 3:
        st.markdown('### 🌱 Su cultivo se encuentra Sano!')
        st.subheader(' `No se detecto ninguna enfermedad`')

