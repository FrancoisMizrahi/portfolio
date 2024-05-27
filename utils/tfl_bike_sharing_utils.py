import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

def get_tfl_data():
    return pd.read_csv("data/tfl_bike_sharing/tfl_bike_sharing.csv", delimiter=";")

def clean_tfl_data(df):
    df.columns = ['day', 'bikes_hired']
    df['day'] = pd.to_datetime(df['day'])
    df['year'] = df['day'].dt.year
    df['month'] = df['day'].dt.month
    df['week'] = df['day'].dt.isocalendar().week
    df = df.astype({"bikes_hired": int, "week": int})
    return df

def get_monthly_averages(df):
    general_monthly_average = (df[(df['year'] >= 2016) & (df['year'] <= 2023)]
                           .groupby('month')['bikes_hired']
                           .mean()
                           .reset_index()
                           .rename(columns={'bikes_hired': 'general_monthly_average'}))
    
    monthly_average = (df[(df['year'] >= 2016) & (df['year'] <= 2023)]
                   .groupby(['year', 'month'])['bikes_hired']
                   .mean()
                   .reset_index()
                   .rename(columns={'bikes_hired': 'monthly_average'}))
    
    return pd.merge(monthly_average, general_monthly_average, on='month')


def get_weekly_deviations(df):
    expected_bike_pw = (df[(df['year'] >= 2016) & (df['year'] <= 2023)]
                        .groupby('week')['bikes_hired']
                        .mean()
                        .reset_index()
                        .rename(columns={'bikes_hired': 'expected_rentals'}))

    # Filter data for actual rentals
    bike_pw = (df[(df['year'] >= 2016) & (df['year'] <= 2023)]
            .groupby(['year', 'week'])['bikes_hired']
            .mean()
            .reset_index()
            .rename(columns={'bikes_hired': 'actual_rentals'}))

    # Merge expected rentals with actual rentals
    bike_pw = pd.merge(bike_pw, expected_bike_pw, on='week', how='left')

    # Calculate excess rentals and excess rentals in percentage
    bike_pw['excess_rentals'] = bike_pw['actual_rentals'] - bike_pw['expected_rentals']
    bike_pw['excess_rentals_inpct'] = bike_pw['excess_rentals'] / bike_pw['expected_rentals']
    return bike_pw


def custom_plot_month(data, **kwargs):
    plt.fill_between(data['month'],
                    data['monthly_average'],
                    data['general_monthly_average'],
                    where=(data['general_monthly_average'] > data['monthly_average']),
                    color='red', alpha=0.3)
    plt.fill_between(data['month'],
                    data['monthly_average'],
                    data['general_monthly_average'],
                    where=(data['general_monthly_average'] <= data['monthly_average']),
                    color='green', alpha=0.3)
    sns.lineplot(data=data, x='month', y='monthly_average')
    sns.lineplot(data=data, x='month', y='general_monthly_average', linewidth=0.8)

def custom_plot_weekly_deviation(data, **kwargs):
    plt.fill_between(data['week'],
                    0,
                    data['excess_rentals_inpct'],
                    where=(data['excess_rentals_inpct'] >= 0),
                    color='green', alpha=0.3)
    plt.fill_between(data['week'],
                    0,
                    data['excess_rentals_inpct'],
                    where=(data['excess_rentals_inpct'] < 0),
                    color='red', alpha=0.3)
    sns.lineplot(data=data, x='week', y='excess_rentals_inpct', linewidth=0.1, **kwargs)
    
    
    plt.axvspan(13, 26, color='grey', alpha=0.3)
    plt.axvspan(39, 53, color='grey', alpha=0.3)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.xticks(ticks=np.arange(13, 54, 13))
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)



