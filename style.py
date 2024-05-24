import streamlit as st

# Load custom CSS
def load_css():
    st.markdown("""
        <style>
        @import url("https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;1,500&display=swap");

        html, body, [class*="css"] {
            font-family: 'Playfair Display', sans-serif;
        }
        </style>
        """, 
        unsafe_allow_html=True)