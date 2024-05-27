import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

import matplotlib.pyplot as plt
import seaborn as sns

from config import label_font_size, figsize

from utils.tfl_bike_sharing_utils import (
    get_tfl_data,
    clean_tfl_data,
    get_monthly_averages,
    get_weekly_deviations,
    custom_plot_month,
    custom_plot_weekly_deviation,
)

st.set_page_config(
    layout="wide",
    page_title="TFL Bike Sharing")


df = get_tfl_data()
df = clean_tfl_data(df)
full_monthly_averages = get_monthly_averages(df)
bike_pw = get_weekly_deviations(df)

leftcol, maincol, rightcol = st.columns([1, 10, 1])
with maincol:

    st.markdown("""
    <div style="text-align: left;">
        <h1>
            Excess rentals in TfL bike sharing
        </h1>
        <p>
            In this project we will focus on the TfL Dataset. The goal is to better visualize the changes on the number of Bike hired.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div style="text-align: left;">
        <p>
            First lets look at the monthly changes compared to the 2016-2023 monthly average.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    g = sns.FacetGrid(full_monthly_averages, col="year", col_wrap=4, height=4, sharey=True)
    g.map_dataframe(custom_plot_month)
    for ax in g.axes.flat:
        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=6)
        ax.grid(True)
    plt.tight_layout()
    st.pyplot(g)


    st.divider()
    
    st.markdown("""
    <div style="text-align: left;">
        <p>
            We can now visualize how big the changes can be compared to the average at weekly level.
        </p>
    </div>
    """, unsafe_allow_html=True)


    # Create the plot
    g = sns.FacetGrid(bike_pw, col="year", col_wrap=4, height=4, sharey=True)
    # Apply the custom plot function
    g.map_dataframe(custom_plot_weekly_deviation)

    # Customize the plot
    g.set_axis_labels("Week", "")
    g.set_titles("{col_name}")
    g.fig.suptitle("Monthly changes in TfL bike rentals\n% change from weekly averages calculated between 2016-2023", y=1.05)
    g.fig.subplots_adjust(top=0.9)
    g.fig.text(0.5, 0.01, "Source: TfL, London Data Store", ha='center')

    for ax in g.axes.flat:
        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=6)
        ax.set_yticklabels(['{:.0%}'.format(x) for x in ax.get_yticks()])
    plt.tight_layout()
    st.pyplot(g)


