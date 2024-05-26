import streamlit as st
# import style
from utils.home_utils import ask_chatgpt

st.set_page_config(
    layout="wide",
    page_title="Porfolio")

# style.load_css()

leftcol, maincol, rightcol = st.columns([1, 10, 1])

# with rightcol:
    # st.image('images/portfolio_small.png')
st.sidebar.markdown("Use the links below to navigate:")

with maincol:
    multi = """
    <div style="text-align: left;">
    <h1>Hi, I'm Francois Mizrahi</h1>
    <p>Hey there, I'm Francois Mizrahi! I'm passionate about data and technology. My expertise covers a wide range of topics, from Data Analytics and Data Engineering to Data Science, Operation Research, Product Management and more</p>
    </div>
    """
    st.markdown(multi, unsafe_allow_html=True)

    question = st.text_input("Get to know me better by asking questions below")
    if question:
        answer = ask_chatgpt(question)
        st.write(answer)
