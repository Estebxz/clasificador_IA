import streamlit as st

st.set_page_config(
    page_title="Clasificador AI",
    page_icon="public/favicon.ico", 
    layout="centered",
    initial_sidebar_state="expanded"
)

pg = st.navigation(
    [
        st.Page("pages/summary.py"),
    ]
)

pg.run()
