import streamlit as st


st.set_page_config(
    layout="wide",
    page_title="Porfolio")


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

load_css()


leftcol, rightcol = st.columns([2, 2])

# with rightcol:
    # st.image('images/portfolio_small.png')

with leftcol:
    multi = """
    <div style="text-align: left;">
    <p>Hello, I am</p>
    <h2>Francois Mizrahi</h2>
    <p>Let’s discover the world through Data</p>
    </div>
    """
    st.markdown(multi, unsafe_allow_html=True)

