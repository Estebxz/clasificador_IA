import streamlit as st

def footer_component():
    st.divider()
    st.subheader("⭐ Apoya este proyecto en GitHub")
    st.link_button(
        icon="🔗",
        label="GitHub",
        url="https://github.com/Estebxz/clasificador_IA", 
        type="secondary", 
        help="Redirigir a GitHub",
        width="content"
    )