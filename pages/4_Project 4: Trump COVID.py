import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

import matplotlib.pyplot as plt
import seaborn as sns

from config import label_font_size, figsize


from utils.trump_covid_utils import (
    get_trump_covid_data
)

st.set_page_config(
    layout="wide",
    page_title="TRump Covid")


data = get_trump_covid_data()

leftcol, maincol, rightcol = st.columns([1, 10, 1])
with maincol:
    st.markdown("""
                <div style="text-align: left;">
                    <h1>
                        Trump and COVID-19
                    </h1>
                    <h2>
                        What is the relationship between Trump and anti-Vax ?
                    </h2>
                    <p>
                        This project is based on this article: <a href="https://acasignups.net/21/07/18/racial-factor-theres-77-counties-which-are-deep-blue-also-low-vaxx-guess-what-they-have">The Racial Factor: There’s 77 Counties Which Are Deep Blue But Also Low-Vaxx. Guess What They Have In Common?</a>
                    </p>
                    <lu>
                        <li>To get vaccination by county, we will use <a href="https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh">data from the CDC</a> </li>
                        <li>We will also need the <a href="https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/VOQCHQ">County Presidential Election Returns 2000-2020</a> </li>
                        <li>Finally, we also need an estimate of the <a href="https://www.ers.usda.gov/webdocs/DataFiles/48747/PopulationEstimates.csv?v=2232">population of each county</a> </li>
                    </lu>
                </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    # Create the plot
    fig, ax = plt.subplots(figsize=figsize)

    sns.scatterplot(data=data, x='donald_vote_rate', y='Series_Complete_Pop_Pct', size='Value', legend=False, sizes=(100, 5000), alpha=0.4)
    sns.regplot(data=data, x='donald_vote_rate', y='Series_Complete_Pop_Pct', scatter=False, color='#c5113e', order=1)

    sns.set_style("whitegrid")
    plt.title('Rate of Donald Votes to Vaccination Level', fontsize=label_font_size)
    plt.xlabel('2020 Trump Vote %', fontsize=label_font_size)
    plt.ylabel('% of Total Population Vaccinated', fontsize=label_font_size)

    # Add horizontal lines and annotations
    plt.axhline(y=50, color='#1d563f', linestyle='dotted')
    plt.text(x=10, y=50, s='50% threshold', color='#1d563f', va='top', fontsize=label_font_size)
    plt.tight_layout()
    plt.grid(True)
    # Display the plot
    st.pyplot(fig)
