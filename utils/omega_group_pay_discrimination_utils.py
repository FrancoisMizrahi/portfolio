import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import t

from config import label_font_size, figsize


def get_omega_data():
    return pd.read_csv("data/omega_group_pay_discrimination_utils/omega.csv")

def get_group_stat(df, group):
    # Group by gender and calculate the statistics
    gender = df.groupby('gender')[group].agg(['mean', 'std', 'count']).reset_index()
    gender = gender.rename(columns={"mean":"mean", "std":"stdev", "count":"sample_size"})

    # Calculate standard error and critical t-value
    gender['stder'] = gender['stdev'] / np.sqrt(gender['sample_size'])
    gender['t_critical'] = t.ppf(0.975, gender['sample_size'] - 1)
    gender['SE'] = gender['stder'] / np.sqrt(gender['sample_size'])

    # Calculate margin of error and confidence interval bounds
    gender['margin_of_error'] = gender['t_critical'] * gender['SE']
    gender['lower_bound_CI'] = gender['mean'] - (1.96 * gender['stder'])
    gender['upper_bound_CI'] = gender['mean'] + (1.96 * gender['stder'])

    return gender
