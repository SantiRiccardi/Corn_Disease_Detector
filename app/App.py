## LIBRERÍAS ##
import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from PIL import Image
from funciones import (preprocesamiento, prediccion_y_probabilidad,plot_probabilidades, diagnóstico)

# -------------------------------------------------------------------------------------------------------------------------- #
## VISUALIZACION DE LA APP ##
st.set_page_config(page_title='Maiz App',
                   layout='centered',
                   page_icon='🌽')

st.sidebar.markdown('## ***Creado por*** **Santiago Riccardi 🇦🇷**')
st.sidebar.markdown("## ***Made with***")

col1, col2,  = st.sidebar.columns(2)

with col1:
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=150)
with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/2560px-Scikit_learn_logo_small.svg.png", width=130)

col3, col4 = st.sidebar.columns(2) 
with col3:
    st.image("https://keras.io/img/logo.png", width=150)
with col4:
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/11/TensorFlowLogo.svg", width=100)
    

col5, col6  = st.sidebar.columns(2)
with col5:
    st.image("https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png", width=150)
with col6:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/1024px-NumPy_logo_2020.svg.png", width=150)

col7, col8 = st.sidebar.columns(2)
with col7:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSu9xFbA6COOd9Wq-koFEoAFD7wpFgbvdz6Q&s", width=145)
with col8:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJtD77NqsHehyobngnMQaSRAQc41uDJq-OyQ&s", width=145)


col9, col10 = st.sidebar.columns(2)
with col9:
    st.image("https://seaborn.pydata.org/_images/logo-tall-lightbg.svg", width=90)
with col10:
    st.image("https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxm36iqima49zxbqsr8ma.jpg", width=140)
# -------------------------------------------------------------------------------------------------------------------------- #
## TITULO ## 
st.markdown("<h1 style='text-align: center;'>Bienvenido a <b>AgroDisease Detector🌽</b></h1>", unsafe_allow_html=True)

#st.title("Bienvenido a ***AgroDisease Detector🌽***")
st.write("Esta aplicación te ayuda a identificar enfermedades comunes en cultivos de maíz a partir de imágenes.")
st.image('app/images/maiz1.jpg')

st.markdown("## **¿Cómo funciona?**")
st.markdown("##### **1°) Carga una imagen de una hoja de maiz**")
st.markdown("##### **2°)** Obtendras un Diagnóstico de tu cultivo")
st.write("Nuestra app te ofrecerá un diagnóstico detallado del estado del cultivo y el tipo de tratamiento si el mismo contiene alguna de las siguientes enfermedades o si se encuentra sano:")
with st.expander('Enfermedades que diagnostica nuestro Modelo'):
    st.write('El modelo predecie con altos niveles de precisión entre cuatro categorías:')
    st.write('1. **Roya Común (Common Rust)**')
    st.write('2. **Mancha Gris de la Hoja (Gray Leaf Spot)**')
    st.write('3. **Tizón del Maíz (Blight)**')
    st.write('4. **Saludable (Healthy)**')

st.markdown("##### **3°) RECOMENDACIONES:**")
st.markdown("**Cargar más de una imagen de la hoja para  obtener una mayor precisión**")

# -------------------------------------------------------------------------------------------------------------------------- #
# SUBIR UNA IMAGEN
st.markdown("## **Diagnósticar cultivo de Maiz**")
uploaded_file = st.file_uploader("Carga una imagen de una hoja de maíz", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    

    # Mostrar la imagen cargada
    with st.spinner("Cargando la imagen..."): # Mostramos un spinner mientras se procesa la imagen
        imagen = Image.open(uploaded_file)
        import time # Simula un tiempo de procesamiento (opcional)
        time.sleep(2) 

    #st.image(imagen, caption="Imagen cargada", use_column_width=True)
   
    # Procesamiento de la Imagen
    imagen_procesada = preprocesamiento(uploaded_file, img_width=224, img_height=224)

    # Carga del Modelo
    model = tf.keras.models.load_model("app/model/model_v1_MobileNet.keras")

    # Prediccíon y probabilidades
    clase_predicha, probabilidad = prediccion_y_probabilidad(imagen_procesada, model)

    # Mostrar Resultados
    ## Diagnóstico:##
    diagnóstico = diagnóstico(imagen_procesada, model)

    # Mostrar el nombre de la clase y su probabilidad
    st.markdown("#### **Diagnóstico**")
    st.markdown(f"Clase: **{clase_predicha}** | Probabilidad: **{probabilidad}**")

    ## Grafico con Probabilidad de pertenencia a cada clase ##
    st.markdown('#### **Probabilidad**')
    figura_probabilidades = plot_probabilidades(imagen_procesada, model) # Obtener la figura del gráfico
    st.pyplot(figura_probabilidades) # Mostrar en la app

# -------------------------------------------------------------------------------------------------------------------------- #

