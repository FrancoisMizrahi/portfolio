import streamlit as st
import style
import matplotlib.pyplot as plt
import seaborn as sns

from utils.messenger_utils import (
    get_messenger_data,
    get_participant_message_counts,
    get_participant_full_df,
    )

from config import label_font_size, figsize

st.set_page_config(
    layout="wide",
    page_title="Messenger Data")

# style.load_css()

leftcol, maincol, rightcol = st.columns([1, 4, 1])

with maincol:
    st.title("Messenger Data")
    st.write("""
             In this project we will analyses my friend **Messenger group chat**. 
             I have downloaded my own **facebook data** and extracted all the messages me and my friends sent to each other on a specific group chat. 
             In this project we will focus only on messages sent in **2023**.
             """)
    
    data = get_messenger_data()
    
    
    st.subheader("Number of Messages per Person")    
    df = get_participant_message_counts(data)
    df_sorted = df.sort_values(by='messages_count', ascending=False)
    
    fig, ax = plt.subplots(figsize=figsize)
    sns.barplot(x='messages_count', y='index', data=df_sorted, color='#67c0fc')
    plt.xlabel('Messages Count', fontsize=label_font_size)
    plt.ylabel('', fontsize=label_font_size)
    st.pyplot(fig)