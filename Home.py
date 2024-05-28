import streamlit as st
# import style
from utils.home_utils import ask_chatgpt

st.set_page_config(
    layout="wide",
    page_title="Porfolio")

# style.load_css()
st.markdown("""
     <style>    
        .main {
            background: linear-gradient(180deg, #FFFFFF, #edf5ff);
            }
        
        [data-baseweb="base-input"]{
        background: #fffbfb;
        border: 20px;
        box-shadow: 10px 5px 5px red !important;
        border-radius: 3px;
        }
            
        .circle-image {
              width: 200px;
              height: 200px;
              border-radius: 50%;
              overflow: hidden;
              box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
          }
          
          .circle-image img {
              width: 100%;
              height: 100%;
              object-fit: cover;
          }
    </style>

    """, unsafe_allow_html=True)

leftcol, maincol, rightcol = st.columns([1, 10, 1])

with maincol:

    multi = """
    <div class="circle-image">
        <img src="app/static/Photo_application.jpg" alt="Face photo">
    </div>
    <div style="text-align: left;">
        <h1>
            Hi, I'm Francois Mizrahi
        </h1>
        <p>
            Hey there, welcome to my portfolio! 
            I'm passionate about data and technology. My expertise covers a wide range of topics, from Data Analytics and Data Science to Operation Research, Product Management and more.
        </p>
        <p>
            Here, you'll find a showcase of my work, including various projects and accomplishments that highlight my skills and expertise in Data. Whether you're interested in my technical prowess, creative projects, or professional achievements, this portfolio offers a first view of my capabilities and dedication.
        <p>
    </div>
    """
    st.markdown(multi, unsafe_allow_html=True)
    st.divider()
    
    st.markdown("""
                <div style="text-align: left;">
                <h3>
                    Get to know me better with my chatbot
                </h3>
                </p>
                    I’m excited to introduce you to my interactive chatbot. This chatbot is designed to assist you in learning more about me, answer any questions you might have, and provide detailed insights into my work and experiences. Feel free to engage with the chatbot for a personalized tour of my professional journey!
                </p>
                <b>
                    Example questions:
                </b>
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