import streamlit as st
import plotly.express as px

def show_graphic(df):
    st.subheader("Distribución por Tipo")
    conteo = df["tipo"].value_counts().reset_index()
    conteo.columns = ["Tipo de Solicitud", "Cantidad"]
    conteo = conteo.sort_values("Cantidad", ascending=False)

    fig = px.bar(
        conteo,
        x="Tipo de Solicitud",
        y="Cantidad",
        color="Tipo de Solicitud",
        text="Cantidad",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )

    fig.update_layout(
        title=dict(text="Solicitudes por Tipo", x=0.5, font=dict(size=18)),
        xaxis_title="Tipo de Solicitud",
        yaxis_title="Cantidad",
        bargap=0.3,
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(size=14),
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig)