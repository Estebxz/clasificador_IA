import streamlit as st
import plotly.express as px

def show_graphic(df):
    st.subheader("Distribución")

    conteo = df["tipo"].value_counts().reset_index()
    conteo.columns = ["Tipo de Solicitud", "Cantidad"]
    conteo = conteo.sort_values("Cantidad", ascending=False)

    max_y = conteo["Cantidad"].max()

    fig = px.bar(
        conteo,
        x="Tipo de Solicitud",
        y="Cantidad",
        text="Cantidad",
        color="Tipo de Solicitud",
        color_discrete_sequence=["#5865F2", "#FF6B6B", "#4ECCA3"]
    )

    fig.update_traces(
        textposition="outside",
    )

    fig.update_layout(
        title=dict(
            text="Solicitudes por Tipo",
            font=dict(size=18)
        ),
        xaxis_title="Tipo de Solicitud",
        yaxis_title="Cantidad",
        bargap=0.25,
        showlegend=False,
        font=dict(color="white", size=14),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(255,255,255,0.2)",
            range=[0, max_y * 1.15]   
        ),

        margin=dict(t=90, b=40)  
    )

    st.plotly_chart(fig)
