import streamlit as st

# Load custom CSS
def load_css():
    st.markdown("""
        <style>
        body {
            background: linear-gradient(135deg, #FFD4DD, #000395);
            height: 100vh;
            margin: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
                'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
                sans-serif;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
        </style>
        """, 
        unsafe_allow_html=True)