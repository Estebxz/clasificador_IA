import streamlit as st
from components.ui.msg_temp import msg_temp

def show_classifier(modelo, vectorizador):
    st.subheader("Clasifica una nueva solicitud")

    with st.form("form_clasificacion"):
        entrada = st.text_area(
            "Ingresa aquí una solicitud",
            placeholder="Ejemplo: Solicito el arreglo de un poste público que no funciona en mi barrio.",
        )
        enviar = st.form_submit_button("Enviar solicitud")

    if enviar:
        if entrada.strip() == "":
            msg_temp(texto="⚠️ Por favor ingresa un texto antes de clasificar", tipo="warning", duracion=5)
        else:
            entrada_procesada = vectorizador.transform([entrada])
            prediccion = modelo.predict(entrada_procesada)[0]
            msg_temp(texto="✅ Clasificación exitosa", tipo="success", duracion=5)
            st.info(f"**Resultado del modelo:** {prediccion}")