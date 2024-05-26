import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import style
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
# plt.style.use('dark_background')

leftcol, maincol, rightcol = st.columns([1, 10, 1])

with maincol:
    st.title("Messenger Data")
    st.write("""
             In this project we will analyses my friend **Messenger group chat**. 
             I have downloaded my own **facebook data** and extracted all the messages me and my friends sent to each other on a specific group chat. 
             In this project we will focus only on messages sent in **2023**.
             """)
    
    with st.expander("Locate your own Data"):
        st.subheader("How to find your Messenger Data")
        st.write("""
                To Download you facebook Data follow these instructions:
                Request a download of your Facebook information from Accounts Centre
                - Click on your profile picture in the top right, then click Settings and privacy.
                - Click Settings.
                - Click Accounts Centre, then click Your information and permissions.
                - Click Download your information.
                - Click Request a download.
                - Select the profiles that you'd like to download information from.
                - Click Next.
                - Select the information that you want to download.
                
                Once you've selected the information that you want to download, choose your file options:
                - The date range
                - The notification email
                - The format of your download request.
                - The quality of photos, videos and other media.
                - Click Submit request.
            """)
        st.subheader("Locate the right file")
        st.write("""
                Once you have downloaded you Facebook Data, you should hace a ZIP file.
                 - First, Unzip the file
                 - Second, navigate to your_activity_across_facebook > messages > inbox
                 - Thrid, open the folder of the conversation you are intrested in
                 - Last, Upload the JSON file called message_1.json
            """)
    
    # Get the Data from the json file
    data = get_messenger_data()
    participant_full_df = get_participant_full_df(data)
    participant_message_counts = get_participant_message_counts(data)
    

    st.divider()
    print("######### Number of Messages per Person #########")
    ######### Viz Number of Messages per Person #########
    st.subheader("Number of Messages per Person")    
    df_sorted = participant_message_counts.sort_values(by='messages_count', ascending=False)
    
    fig, ax = plt.subplots(figsize=figsize)
    sns.barplot(x='messages_count', y='index', data=df_sorted, color='#017fad')
    plt.xlabel('Messages Count', fontsize=label_font_size)
    plt.ylabel('', fontsize=label_font_size)
    st.pyplot(fig)

    
    st.divider()
    print("######### Viz Number of Messages Evolution Over Time #########")
    ######### Viz Number of Messages Evolution Over Time #########
    st.subheader("Number of Messages Evolution Over Time")
    grannularity = st.selectbox('Select grannularity', ('Monthly', 'Daily'))

    if grannularity == "Monthly":
        df_messages_year_month = participant_full_df.groupby(by=["year", "month"]).count()[['index']].reset_index()
        df_messages_year_month['date'] = pd.to_datetime(df_messages_year_month[['year', 'month']].assign(day=1))
    else:
        df_messages_year_month = participant_full_df.groupby(by=["year", "month", "day"]).count()[['index']].reset_index()
        df_messages_year_month['date'] = pd.to_datetime(df_messages_year_month[["year", "month", "day"]])

    fig, ax = plt.subplots(figsize=figsize)
    sns.lineplot(x='date', y='index', data=df_messages_year_month, palette='viridis')
    plt.xlabel('Date', fontsize=label_font_size)
    plt.ylabel('Number of Messages', fontsize=label_font_size)
    st.pyplot(fig)


    st.divider()
    print("######### Viz Number of Messages Evolution Over Time #########")
    ######### Viz Number of Messages Evolution Over Time #########
    st.subheader("Number of Messages Evolution Over Time")

    users = st.multiselect(
        'Select Users',
        sorted(participant_full_df.sender_name.unique()),
        sorted(participant_full_df.sender_name.unique()))

    df_messages_year_month_sender = participant_full_df.groupby(by=["sender_name", "year", "month"]).count()[['index']].reset_index()
    df_messages_year_month_sender['date'] = pd.to_datetime(df_messages_year_month_sender[['year', 'month']].assign(day=1))

    fig, ax = plt.subplots(figsize=figsize)
    for n in users:
        sns.lineplot(x='date', y='index', data=df_messages_year_month_sender[df_messages_year_month_sender["sender_name"] == n], label=n, color='#017fad')
    plt.title('Number of messages Evolution Over Time')
    plt.xlabel('Date', fontsize=label_font_size)
    plt.ylabel('Number of Messages', fontsize=label_font_size)
    plt.legend(fontsize=label_font_size)
    st.pyplot(fig)


    st.divider()
    print("######### Viz Number of Messages #########")
    ######### Viz Number of Messages #########
    st.subheader("Number of Messages")
    grannularity = st.selectbox(
        'Select Time Grannularity',
        ["Month", "Day of Month", "Day of Week"])
    
    fig, ax = plt.subplots(figsize=figsize)
    if grannularity == "Month":
        df_messages_avg_month = participant_full_df.groupby(by=["year", "month"]).count()[['index']].reset_index()
        df_messages_avg_month = df_messages_avg_month.groupby(by=["month"]).mean()[['index']].reset_index()
        sns.barplot(x='month', y='index', data=df_messages_avg_month, color='#017fad')
        plt.title('Average Number of Messages per Month')
        plt.xlabel('Month', fontsize=label_font_size)
        plt.ylabel('Number of Messages', fontsize=label_font_size)

    elif grannularity == "Day of Month":
        df_messages_avg_month_day = participant_full_df.groupby(by=["year", "month", 'day']).count()[['index']].reset_index()
        df_messages_avg_month_day = df_messages_avg_month_day.groupby(by=["day"]).mean()[['index']].reset_index()
        sns.barplot(x='day', y='index', data=df_messages_avg_month_day, color='#017fad')
        plt.title('Average Number of Messages per Day of the Month')
        plt.xlabel('Day of the Month', fontsize=label_font_size)
        plt.ylabel('Number of Messages', fontsize=label_font_size)

    else:
        df_messages_day_week = participant_full_df.groupby(by=['day_week']).count()[['index']].reset_index()
        sns.barplot(x='day_week', y='index', data=df_messages_day_week, color='#017fad')
        plt.title('Number of Messages per Day of the Week')
        plt.xlabel('Day of the Week', fontsize=label_font_size)
        plt.ylabel('Number of Messages', fontsize=label_font_size)
    st.pyplot(fig)


    st.divider()
    print("######### Viz All Sent Messages #########")
    ######### Viz All Sent Messages #########
    st.subheader("All Sent Messages")
    grannularity = st.selectbox(
        'Select visualization',
        ["Scatter Plot + Heat Map", "Scatter Plot", "Heat Map"])

    participant_full_df_2 = participant_full_df.copy()

    # Extract date and time information
    participant_full_df_2['date'] = participant_full_df_2['timestamp'].dt.date
    participant_full_df_2['time'] = participant_full_df_2['timestamp'].dt.time
    participant_full_df_2['datetime'] = pd.to_datetime(participant_full_df_2['timestamp'], unit='s')

    # Convert time to seconds past midnight
    participant_full_df_2['seconds'] = participant_full_df_2['time'].apply(lambda time: time.hour*3600 + time.minute*60 + time.second)

    # Sorting dataframe by 'date' and 'seconds' 
    participant_full_df_2 = participant_full_df_2.sort_values(['date', 'seconds'])

    # Plotting
    fig, ax = plt.subplots(figsize=figsize)
    sns.set_style("white")
    if grannularity == "Scatter Plot":
        sns.scatterplot(x='date', y='seconds', data=participant_full_df_2, s=30, alpha=0.3, edgecolor = None, color="#017fad")
    elif grannularity == "Heat Map":
        sns.kdeplot(x='datetime', y='seconds', data=participant_full_df_2, cmap="Reds", fill=True, bw_adjust=0.75)
    else:
        sns.kdeplot(x='datetime', y='seconds', data=participant_full_df_2, cmap="Reds", fill=True, bw_adjust=0.75)
        sns.scatterplot(x='date', y='seconds', data=participant_full_df_2, s=30, alpha=0.3, edgecolor = None, color='#017fad')
    
    plt.xlabel('Date', fontsize=label_font_size)
    plt.ylabel('Time of the day', fontsize=label_font_size)
    plt.title('Messages')
    plt.xticks(rotation=45)

    # Setting the y-axis labels as time strings
    y_ticks = [f'{h}:00' for h in range(24)]
    plt.yticks(ticks=range(0, 24*3600, 3600), labels=y_ticks)

    plt.tight_layout()
    st.pyplot(fig)


    st.divider()
    print("######### Viz Number of Messages Evolution Over Time #########")
    ######### Viz Number of Messages Evolution Over Time #########
    st.subheader("Number of Messages")
    participant_full_df_3 = participant_full_df.copy()

    participant_full_df_3['Day_of_Week'] = participant_full_df_3['timestamp'].dt.day_name()
    participant_full_df_3['Hour_of_Day'] = participant_full_df_3['timestamp'].dt.hour

    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Create a pivot table for the heatmap
    heatmap_data = participant_full_df_3.pivot_table(index='Hour_of_Day', columns='Day_of_Week', values='content', aggfunc='count')

    # Reorder columns based on the specified order
    heatmap_data = heatmap_data[day_order]

    # Create the heatmap using seaborn
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=False, linewidths=0.5)
    plt.title('Message Heatmap')
    plt.xlabel('Day of the Week', fontsize=label_font_size)
    plt.ylabel('Hour of the Day', fontsize=label_font_size)
    st.pyplot(fig)




