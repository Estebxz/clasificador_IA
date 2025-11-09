import streamlit as st
import pandas as pd
import joblib

from components.show_preview import show_preview
from components.show_graphic import show_graphic
from components.show_classify import show_classifier
from components.show_metrics import show_metrics
from components.ui.star_github import footer_component

model_path = ("models/model.pkl")
model = joblib.load(model_path)
vectorizer_path = ("models/vectorizer.pkl")
vectorizer = joblib.load(vectorizer_path)

# Cargar datos
@st.cache_data
def cargar_datos():
    return pd.read_csv("data/solicitudes_ciudadanas.csv")

df = cargar_datos()

st.image("public/Frame 1.svg", width="stretch")
show_classifier(model, vectorizer)
st.divider()

with st.container():
    opcion = st.radio(
        "Seleccionar vista:",
        ["Vista Previa", "Distribución por Tipo", "Metricas"],
        horizontal=True,
        index=0,
        help="Al seleccionar vista se vera reflejado los datos guardados",
    )
    if opcion == "Vista Previa":
        show_preview(df=df)
    elif opcion == "Distribución por Tipo":
        show_graphic(df=df)
    else:
        show_metrics(df=df)

footer_component()
