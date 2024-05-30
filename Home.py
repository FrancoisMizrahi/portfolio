import streamlit as st
from utils.home_utils import ask_chatgpt
from style import load_home_style

st.set_page_config(
    layout="wide",
    page_title="Porfolio")

load_home_style()

leftcol, maincol, rightcol = st.columns([1, 10, 1])

with maincol:

    multi = """
    <div class="container-center">
        <img src="app/static/Photo_application.jpg" alt="Face photo" class="circle-image">
    </div>
    <div style="text-align: center;">
        <h1>
            Hi, I'm François Mizrahi
        </h1>
    </div>
    <div style="text-align: left;">
        <h2>
            Welcome to my portfolio!
        </h2>
        <p>
            I'm passionate about data and technology. My expertise covers a wide range of topics, from Data Analytics and Data Science to Operation Research, Product Management and more.
        </p>
        <p>
            Here, you'll find a showcase of my work, including various projects and accomplishments that highlight my skills and expertise in Data. 
            Whether you're interested in my technical prowess, creative projects, or professional achievements, this portfolio offers a first view of my capabilities and dedication.
            All the portfolio code can be found in this <a href="https://github.com/FrancoisMizrahi/portfolio">github repo</a>
        <p>
    </div>
    """
    st.markdown(multi, unsafe_allow_html=True)
    st.divider()
    
    st.markdown("""
                <div style="text-align: left;">
                <h2>
                    My chatbot
                </h2>
                </p>
                    I’m excited to introduce you to my interactive chatbot. This chatbot is designed to assist you in learning more about me, answer any questions you might have, and provide detailed insights into my work and experiences. Feel free to engage with the chatbot for a personalized tour of my professional journey!
                </p>
                </div>
            """, unsafe_allow_html=True)
    
    with st.expander("Example questions:"):
        st.markdown("""
                    <div style="text-align: left;">
                    <lu>
                        <li>Which universities did Francois Mizrahi attend for his higher education?</li>
                        <li>What was Francois Mizrahi's role at Amazon and what did he achieve there?</li>
                        <li>What programming languages does Francois Mizrahi know?</li>
                        <li>What data analytics skills does Francois Mizrahi possess?</li>
                        <li>What was the objective of the project Delphes?</li>
                        <li>What are Francois Mizrahi's hobbies?</li>
                    </lu>
                    </div>
                """, unsafe_allow_html=True)
    
    question = st.text_input("Ask me a question:")

    if question:
        answer = ask_chatgpt(question)
        st.write(answer)