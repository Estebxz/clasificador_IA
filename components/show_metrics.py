import streamlit as st

def show_metrics(df):
    n_filas = df.shape[0]
    n_columnas = df.shape[1]
    duplicados = df.duplicated().sum()
    n_nulos = df.isnull().sum().sum()

    a, b = st.columns(2)
    c, d = st.columns(2)

    a.metric("Número de filas", n_filas, delta="200 registros nuevos", border=True)
    b.metric("Número de columnas", n_columnas, delta_color="inverse", delta="5 columnas menos", border=True)
    c.metric("Número de nulos", n_nulos, delta_color="off", delta="0", border=True)
    d.metric("Número de duplicados", duplicados, delta_color="off", delta="Registros duplicados", border=True)
