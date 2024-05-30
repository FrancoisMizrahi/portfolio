import pandas as pd
import numpy as np
from datetime import datetime

import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import t


def merge_data(vaccinations, election2020_results, population):
    election_data_trump = election2020_results[election2020_results['candidate'] == 'DONALD J TRUMP'] \
        .groupby('FIPS')['candidatevotes'].sum().reset_index() \
        .rename(columns={'candidatevotes': 'total_donald_votes'})

    election_data_total = election2020_results.groupby('FIPS')['candidatevotes'].sum().reset_index() \
    .rename(columns={'candidatevotes': 'total_votes'})

    election_data_trump = pd.merge(election_data_trump, election_data_total, on='FIPS')
    election_data_trump['donald_vote_rate'] = (election_data_trump['total_donald_votes'] / election_data_trump['total_votes']) * 100

    data = vaccinations[vaccinations['Date'] == '05/12/2021'].dropna(subset=["Series_Complete_Pop_Pct"])
    data = pd.merge(data, election_data_trump, on='FIPS')
    data = data[['FIPS', 'donald_vote_rate', 'Series_Complete_Pop_Pct']]
    
    data = pd.merge(data, population, on='FIPS')
    return data

def get_trump_covid_data():
    vaccinations = pd.read_csv("data/trump_covid/COVID-19_Vaccinations_in_the_United_States_County.csv", dtype={'FIPS': 'str'})
    vaccinations = vaccinations[vaccinations["FIPS"] != "UNK"]

    election2020_results = pd.read_csv("data/trump_covid/countypres_2000-2020.csv", dtype={'county_fips': 'str'})
    election2020_results = election2020_results[election2020_results["year"] == 2020]
    election2020_results.rename(columns={"county_fips": "FIPS"}, inplace=True)

    population = pd.read_csv("data/trump_covid/PopulationEstimates.csv", encoding='latin-1')
    population = population[population["Attribute"] == "POP_ESTIMATE_2020"]
    population.rename(columns={"FIPStxt": "FIPS"}, inplace=True)
    population['FIPS'] = population['FIPS'].astype(str).str.zfill(5)

    data = merge_data(vaccinations, election2020_results, population)
    return data