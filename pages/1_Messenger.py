import streamlit as st
import style

st.set_page_config(
    layout="wide",
    page_title="Messenger Data")

style.load_css()

leftcol, maincol, rightcol = st.columns([1, 4, 1])

with maincol:
    st.title("Messenger Data")
