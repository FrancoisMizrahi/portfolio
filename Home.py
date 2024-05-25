import streamlit as st
import style
from secrets import CHATGPT_API_KEY

st.set_page_config(
    layout="wide",
    page_title="Porfolio")

# style.load_css()


leftcol, rightcol = st.columns([2, 2])

# with rightcol:
    # st.image('images/portfolio_small.png')

with leftcol:
    multi = """
    <div style="text-align: left;">
    <h1>Hi, I'm Francois Mizrahi</h1>
    <p>Let’s discover the world through Data</p>
    </div>
    """
    st.markdown(multi, unsafe_allow_html=True)



