import streamlit as st

# Load custom CSS
def load_home_style():
    st.markdown("""
     <style>    
        .main {
            background: linear-gradient(180deg, #FFFFFF, #d9dadb);
            }
        
        [data-baseweb="base-input"]{
        background: #fffbfb;
        border: 20px;
        border-radius: 3px;
        }
        
        .container-center {
            display: flex;
            justify-content: center;
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

def load_project_style():
    st.markdown("""
     <style>    
        .container-center {
            display: flex;
            justify-content: center;
            }
        
        .circle-image {
            width: 300px;
            height: 300px;
            border-radius: 5%;
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