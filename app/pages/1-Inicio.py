import streamlit as st

## Titulo de Inicio ##
#st.title("Bienvenido a la Detección de Enfermedades en Maíz")
#st.markdown("# Bienvenido a ***MaizApp***")
st.markdown("<h1 style='text-align: center;'>Bienvenido a <b>AgroDisease Detector🌽</b></h1>", unsafe_allow_html=True)

# -------------------------------------------------------------------------------------------------------------------------- #
## INTRODUCCIÓN ##
st.markdown("## **Introducción**")
st.markdown("Este proyecto se centra en la clasificación de enfermedades en cultivos de maíz mediante el uso de modelos avanzados de aprendizaje profundo.")
st.markdown("El objetivo principal es desarrollar un sistema capaz de identificar, de manera precisa y automatizada, cuatro categorías de imágenes: tres correspondientes a enfermedades específicas que afectan al maíz y una adicional que indica si la planta está sana.")
st.markdown("El enfoque basado en deep learning aprovecha redes neuronales convolucionales (CNN), una arquitectura ampliamente utilizada en la clasificación de imágenes por su capacidad para extraer y aprender características visuales relevantes.\
            Este tipo de modelo no solo permite diferenciar entre plantas sanas y enfermas, sino también identificar el tipo específico de enfermedad presente, lo que resulta clave para implementar estrategias de manejo adecuadas y oportunas.\
            El desarrollo de este proyecto tiene como finalidad aportar una solución tecnológica innovadora que no solo asista a los productores en la detección y gestión de enfermedades en cultivos, sino que también promueva un uso más eficiente de los recursos agrícolas, mejorando la productividad y reduciendo las pérdidas económicas asociadas a enfermedades no controladas.\
            Este trabajo, por lo tanto, no solo tiene un impacto directo en el ámbito agrícola, sino también en la sostenibilidad y la seguridad alimentaria."
        )


# -------------------------------------------------------------------------------------------------------------------------- #
## TIPO DE ENFERMEDADES ##
st.markdown("## **Enfermedades que predice nuestro Modelo**")
st.markdown("* **Roya Común (Common Rust)**")
st.markdown("* **Mancha Gris de la Hoja (Gray Leaf Spot)**")
st.markdown("* **Tizón del Maíz (Blight)**")
st.markdown("* **Saludable (Healthy)**")


# Opciones de enfermedades con síntomas y condiciones
enfermedades = {
    "Roya Común (Common Rust)": {
        "imagen": "app/images/Corn_Common_Rust (48).jpg",
        "Sintomas": "Pústulas de color marrón rojizo a anaranjado en ambas caras de la hoja, inicialmente pequeñas y dispersas.\
                     Con el tiempo, las pústulas se oscurecen y se tornan negras a medida que la enfermedad avanza.\
                     Puede causar un debilitamiento general de la planta, reducción en la fotosíntesis y menor desarrollo de las mazorcas.\
                     En infecciones severas, se observa una defoliación temprana que afecta el llenado de grano.",
        "Condiciones ambientales favorables": ["Temperaturas moderadas (15-25°C) y alta humedad (>95%).",
                                               "Presencia de períodos prolongados de rocío en las hojas (mínimo 6 horas).",
                                               "Regiones con lluvias frecuentes o condiciones nubosas favorecen la propagación.",
                                               "El hongo sobrevive en regiones cálidas y se dispersa a largas distancias con el viento."]
    },
    "Mancha Gris de la Hoja (Gray Leaf Spot)": {
        "imagen": "app/images/Corn_Gray_Spot (8).jpg",
        "Sintomas": "Aparición de manchas rectangulares de color gris a marrón en las hojas, con bordes definidos.\
                     Las lesiones pueden expandirse y unirse, causando necrosis en grandes áreas de la hoja.\
                     Reducción en la fotosíntesis, afectando el desarrollo del grano y disminuyendo el rendimiento.\
                     En infecciones severas, puede observarse marchitez y muerte prematura de la planta.",
        "Condiciones ambientales favorables": ["Alta humedad (>90%) y temperaturas cálidas (25-30°C).",
                                               "Períodos prolongados de humedad en las hojas (rocío o lluvias frecuentes).",
                                               "Residuos de cultivos infectados en la superficie del suelo que actúan como fuente de inóculo.",
                                               "Ambientes con baja circulación de aire (por alta densidad de siembra) favorecen la infección."]
    },
    "Tizón del Maíz (Blight)": {
        "imagen": "app/images/Corn_Blight (21).jpg",
        "Sintomas": "Se manifiesta como manchas necróticas alargadas en las hojas, que pueden unirse y causar una necrosis extensa.\
                    Pueden aparecer lesiones acuosas al principio, que luego se tornan marrones o grises con bordes oscuros.\
                    En infecciones avanzadas, el tejido afectado puede morir, reduciendo la capacidad fotosintética de la planta.\
                    Puede afectar hojas, tallos y mazorcas, causando una disminución del rendimiento.",
        "Condiciones ambientales favorables": ["Alta humedad relativa (>90%) y temperaturas moderadas a cálidas (20-30°C).",
                                               "Lluvias frecuentes o rocío prolongado que favorece la diseminación del hongo/bacteria causante.",
                                               "La presencia de restos de cultivos infectados en el suelo facilita la propagación en temporadas siguientes."]
    },
    "Saludable (Healthy)": {
        "imagen": "app/images/Corn_Health (1).jpg",
        "Sintomas": "Las plantas saludables tienen hojas de color verde uniforme, sin lesiones, necrosis ni signos visibles de enfermedad.",
        "Condiciones ambientales favorables": ["Crecimiento óptimo con adecuada nutrición, agua y control de plagas y enfermedades."]
    }
}

# Selectbox para elegir la enfermedad
opcion = st.selectbox("Selecciona una enfermedad:", list(enfermedades.keys()))

# Mostrar imagen e información en dos columnas
col1, col2 = st.columns([1, 2])  
with col1:
    st.image(enfermedades[opcion]["imagen"], caption=opcion, use_column_width=True)
with col2:
    st.markdown(f"#### {opcion}")  # Título de la enfermedad
    st.markdown("##### 🩺 **Síntomas**")
    st.write(enfermedades[opcion]["Sintomas"])
    st.markdown("##### 🌱 **Condiciones ambientales favorables**")
    for condicion in enfermedades[opcion]["Condiciones ambientales favorables"]:
        st.markdown(f"- {condicion}")  # Muestra cada condición como un punto en la lista
    


# -------------------------------------------------------------------------------------------------------------------------- #
## CÓMO FUNCIONA ##
st.markdown("## **¿Cómo funciona?**")
st.markdown("##### **1°) Carga una imagen de una hoja de maiz**")
st.markdown("##### **2°)** Obtendras un Diagnóstico de tu cultivo")
st.write('El modelo predecie con altos niveles de precisión entre las 4 categorías')
st.write("Nuestra app te ofrecerá un diagnóstico detallado del estado del cultivo y el tipo de tratamiento si el mismo contiene alguna de las siguientes enfermedades o si se encuentra sano:")
# imagen
st.markdown("##### **3°) RECOMENDACIONES:**")
st.markdown("**Cargar más de una imagen de la hoja para obtener más diagnósticos y una mayor precisión**")

# -------------------------------------------------------------------------------------------------------------------------- #
# PIE DE PÁGINA
st.markdown("## ***Made with***")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white", width=150, caption="Streamlit")
with col2:
    st.image("https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white", width=150, caption="Scikit-learn")
with col3:
    st.image("https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white", width=150, caption="Keras")
with col4:
    st.image("https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white", width=150, caption="TensorFlow")
    

col5, col6, col7, col8 = st.columns(4)
with col5:
    st.image("https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54", width=150, caption="Python")
with col6:
    st.image("https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white", width=150, caption="Numpy")
with col7:
    st.image("https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white", width=150, caption="Pandas")
with col8:
    st.image("https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black", width=150, caption="Matplotlib")
