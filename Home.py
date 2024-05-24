import streamlit as st
import style

st.set_page_config(
    layout="wide",
    page_title="Porfolio")

style.load_css()


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

