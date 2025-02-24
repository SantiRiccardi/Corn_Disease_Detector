import streamlit as st
from PIL import Image


# -------------------------------------------------------------------------------------------------------------------------- #
## TITULO ##
st.markdown("<h1 style='text-align: center;'>Información sobre la aplicación y el equipo desarrollador</h1>", unsafe_allow_html=True)

# -------------------------------------------------------------------------------------------------------------------------- #
## El Modelo ##
st.markdown("## **El Modelo**")
st.write("En esta aplicación utilizamos MobileNet, una arquitectura de red neuronal convolucional (CNN) optimizada para dispositivos con recursos limitados. \
        Es un modelo ligero y eficiente, diseñado para tareas de clasificación de imágenes con alto rendimiento y bajo consumo computacional."
        )

st.subheader("🔍 ¿Qué es ***MobileNet***?")
st.write(" MobileNet es un modelo de aprendizaje profundo diseñado para tareas de visión por computadora, como clasificación de imágenes y detección de objetos.\
           Sin embargo, en este caso, se ha utilizado Transfer Learning para aprovechar un modelo preentrenado en ImageNet y adaptarlo a la clasificación de enfermedades en cultivos de maíz.\
           Su principal ventaja es que logra un alto rendimiento con menor cantidad de parámetros, lo que lo hace eficiente en términos de velocidad y uso de memoria.\
           A continuación, explicamos detalladamente cada componente del modelo y su función:")

st.subheader("🧠 Arquitectura del Modelo")
st.markdown("##### **1. Creación del Modelo Secuencial**")
st.write("El modelo se construyó de manera Secuencial, es decir, agregando capas.")

st.markdown("##### **2. Importación del Modelo Base: MobileNet**")
st.write("Aquí se carga MobileNet preentrenado en ImageNet, pero sin incluir la parte final de clasificación (`include_top=False`).")
st.markdown("* `input_shape=(224, 224, 3)`: Define el tamaño de entrada de las imágenes (224x224 píxeles, con 3 canales de color RGB). ")
st.markdown("* `alpha=1.0`: Controla la cantidad de filtros en cada capa convolucional. Un valor de 1.0 significa que se usan todos los filtros estándar de MobileNet.")
st.markdown("* `depth_multiplier=1`: Controla la profundidad de cada capa convolucional. Un valor de 1 significa que no se modifica la arquitectura original.")
st.markdown("* `dropout=0.001`: Se usa una tasa de dropout muy baja para evitar sobreajuste en el modelo base.")
st.markdown("* `include_top=False`: Excluye la parte final de MobileNet (capas densas de clasificación). Esto nos permite agregar nuestra propia capa de clasificación personalizada.")
st.markdown("* `weights='imagenet'`: Se cargan los pesos preentrenados en ImageNet, lo que permite aprovechar el conocimiento previo del modelo en la identificación de características visuales.")

st.markdown("##### **3. Congelación del Modelo Base**")
st.write("Dado que el modelo ya ha sido preentrenado en millones de imágenes de ImageNet, no queremos que se entrene nuevamente para no perder su conocimiento previo.\
            Al congelar las capas, solo las nuevas capas añadidas serán entrenadas, lo que hace que el modelo aprenda rápidamente sin necesidad de un dataset extremadamente grande.")

st.markdown("##### **4. Adición de Nuevas Capas para la Clasificación**")
st.write("Después de la base de MobileNet, agregamos capas personalizadas para adaptar el modelo a la detección de enfermedades en maíz.")

st.markdown("###### ***Global Average Pooling (GAP)***")
st.write("Esta capa toma la salida de la última convolución de MobileNet y reduce su dimensión a un solo número por canal.\n")
st.write("* Reduce la cantidad de parámetros y evita el sobreajuste.\n* Permite mantener la información más importante de cada filtro convolucional.\n * Hace que el modelo sea más eficiente y ligero.")

st.markdown("###### ***Dropout (Regularización)***")
st.write("* Desactiva aleatoriamente el 20% de las neuronas durante el entrenamiento.\n* Ayuda a prevenir el sobreajuste y mejora la generalización del modelo.")

st.markdown("###### ***Capa Densa Final (Clasificación)***")
st.write("* `Dense(len(clases))`: Define una neurona por cada clase en el dataset.\n* `activation='softmax'`: Convierte las salidas en probabilidades para cada enfermedad, asegurando que la suma de todas sea 1.")



# -------------------------------------------------------------------------------------------------------------------------- #
## Resultados y Métricas ##
st.markdown("## **Resultados y Métricas**")

st.subheader("📊 Métricas")
st.markdown("##### Modelo ***MobileNet***: ")
st.write("* ***Accuracy*** : 93%\n* ***Precision*** : 0.93\n* ***Recall*** : 0.93")
st.image('/Users/santi/Corn_Disease_Detector/app/images/modelos.png')



st.subheader("🎯 Resultados")
st.write(" ✅ Rendimiento general: El modelo muestra un buen desempeño con alta precisión en la mayoría de las clases.")
st.write("✅ ***Common Rust*** y ***Healthy*** están bien clasificadas.")
st.write("✅ El modelo clasifica correctamente los ***cultivos sanos el 100%*** de las veces.")
st.write("✅ El modelo clasifica correctamente los ***cultivos enfermos el 90.16%*** de las veces.")
st.write("✅ El modelo ***distingue entre sano y enfermo con un 92.89%*** de precisión.")


# -------------------------------------------------------------------------------------------------------------------------- #
## Tecnologías utilizadas ##
st.markdown("## **Tecnologías utilizadas**")

# -------------------------------------------------------------------------------------------------------------------------- #
## ¿Por que usar IA para detectar enfermedades en cultivos de Maiz? ##
st.markdown("## **¿Por que usar IA para detectar enfermedades en cultivos de Maiz?**")

st.write("El uso de Inteligencia Artificial (IA) en la detección de enfermedades en cultivos de maíz representa\
         un avance significativo en la agricultura de precisión, permitiendo a los productores mejorar la salud\
        de sus cultivos y optimizar la toma de decisiones.")

st.write("🔍 **Detección temprana y precisa**: Los modelos de IA, como redes neuronales convolucionales (CNN),\
        pueden identificar patrones sutiles en imágenes de hojas que serían difíciles de detectar a simple vista,\
        permitiendo un diagnóstico oportuno.")

st.write("🚀 **Eficiencia y rapidez**: La automatización del proceso de detección reduce el tiempo y los recursos necesarios para inspeccionar los cultivos manualmente, optimizando el trabajo del productor.")

st.write("📈 **Reducción de pérdidas económicas**: Al identificar enfermedades en una etapa temprana,\
             los agricultores pueden tomar medidas preventivas y minimizar pérdidas en la producción.")

st.write("🌍 **Agricultura sostenible**: Un diagnóstico más preciso permite aplicar tratamientos específicos,\
         reduciendo el uso innecesario de pesticidas y promoviendo prácticas más sostenibles.")

st.write("📡 **Accesibilidad y escalabilidad**: Con modelos implementados en aplicaciones móviles o plataformas web, \
         cualquier productor puede obtener un diagnóstico instantáneo con solo una imagen, sin necesidad de equipos costosos.")

st.write("La IA no solo mejora la productividad, sino que también transforma la agricultura en una práctica más eficiente,\
            sostenible y accesible. 🚜🌱")

# -------------------------------------------------------------------------------------------------------------------------- #
## Nuestro equipo ##
st.markdown("## **Nuestro equipo**")

# Foto de perfil
st.image("/Users/santi/Corn_Disease_Detector/app/images/Linkedin.jpg", width=550, use_column_width=False)

# Nombre y profesión centrados
st.markdown(
    "<h2 style='text-align: center; color: #4a7c59;'>Santiago Riccardi</h2>"
    "<h4 style='text-align: center; color: #6c757d;'>Data Scientist</h4>",
    unsafe_allow_html=True
)

# Iconos y enlaces a redes sociales
st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://github.com/SantiRiccardi" target="_blank">
            <img src="https://img.icons8.com/ios-glyphs/60/000000/github.png" width="40">
        </a>
        &nbsp;&nbsp;&nbsp;
        <a href="https://www.linkedin.com/in/santiriccardi/" target="_blank">
            <img src="https://img.icons8.com/ios-glyphs/60/0077b5/linkedin.png" width="40">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)



    