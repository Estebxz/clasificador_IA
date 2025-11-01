import streamlit as st
import pandas as pd
import joblib

from components.show_preview import show_preview
from components.show_graphic import show_graphic
from components.show_classify import show_classifier
from components.ui.star_github import footer_component

st.set_page_config(
    page_title="Clasificador con redes generativas",
    page_icon="public/favicon.ico",
    layout="centered",
)

model_path = ("models/model.pkl")
model = joblib.load(model_path)
vectorizer_path = ("models/vectorizer.pkl")
vectorizer = joblib.load(vectorizer_path)

# Cargar datos
@st.cache_data
def cargar_datos():
    return pd.read_csv("data/solicitudes_ciudadanas.csv")

df = cargar_datos()

st.title("CLASIFICADOR DE SOLICITUDES CIUDADANAS CON IA")
show_preview(df)
show_graphic(df)

st.write("")
st.title(f"{len(df)}")
st.caption("Total de solicitudes registradas")    

st.divider()
show_classifier(model, vectorizer)

footer_component()