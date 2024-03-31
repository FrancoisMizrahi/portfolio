import streamlit as st
from transformers import pipeline

st.set_page_config(layout="wide")

leftcol, maincol, rightcol = st.columns([1, 4, 1])

with maincol:
    st.title("Porfolio")

    classifier = pipeline("sentiment-analysis")
    st.write(classifier("I've been waiting for a HuggingFace course my whole life."))
