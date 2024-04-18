import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Page 1")

leftcol, maincol, rightcol = st.columns([1, 4, 1])

with maincol:
    st.title("Page 1")
