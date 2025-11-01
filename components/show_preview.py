import streamlit as st

def show_preview(df):    
    st.subheader("Vista previa")
    st.dataframe(df.head(50))