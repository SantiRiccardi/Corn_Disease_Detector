import streamlit as st

#st.markdown("Formulario de contacto para soporte y feedback.")

# Configuración de la página
st.set_page_config(
    page_title="Contacto - Detección de Enfermedades en Maíz",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Función para enviar el formulario (puedes personalizar esta función según tus necesidades)
def send_form(name, email, message):
    # Aquí puedes agregar la lógica para enviar el formulario a una base de datos o correo electrónico
    # Por ejemplo, puedes usar una API para enviar un correo electrónico
    # A continuación, solo se imprime la información como ejemplo
    st.write(f"Nombre: {name}")
    st.write(f"Correo Electrónico: {email}")
    st.write(f"Mensaje: {message}")
    st.success("Tu mensaje ha sido enviado con éxito. Gracias por tu feedback!")

# Sección de contacto
st.title("Formulario de Contacto")
st.markdown("Por favor, llena el siguiente formulario para soporte y feedback:")

# Crear el formulario
with st.form(key='contact_form'):
    name = st.text_input("Nombre")
    email = st.text_input("Correo Electrónico")
    message = st.text_area("Mensaje")

    # Botón de envío
    submit_button = st.form_submit_button(label='Enviar')

    # Procesar el formulario
    if submit_button:
        if name and email and message:
            send_form(name, email, message)
        else:
            st.error("Por favor, completa todos los campos antes de enviar el formulario.")


