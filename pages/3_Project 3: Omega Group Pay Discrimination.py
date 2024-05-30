import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

import matplotlib.pyplot as plt
import seaborn as sns

from config import label_font_size, figsize

from style import load_project_style
from utils.omega_group_pay_discrimination_utils import (
    get_omega_data,
    get_group_stat,
)

st.set_page_config(
    layout="wide",
    page_title="Omega group pay discrimination")


omega = get_omega_data()

load_project_style()


leftcol, maincol, rightcol = st.columns([1, 10, 1])
with maincol:

    st.markdown("""
                 <div class="container-center">
                    <img src="app/static/pay_gap.jpg" alt="Face photo" class="circle-image">
                </div>
                <div style="text-align: center;">
                    <h1>
                        Omega group pay discrimination
                    </h1>
                </div>
                <div style="text-align: left;">
                    <p>
                        At the last board meeting of Omega Group Plc., the headquarters of a large multinational company, the issue was raised that women were being discriminated in the company, in the sense that the salaries were not the same for male and female executives. A quick analysis of a sample of 50 employees (of which 24 men and 26 women) revealed that the average salary for men was about 8,700 higher than for women. This seemed like a considerable difference, so it was decided that a further analysis of the company salaries was warranted.
                    </p>
                    <p>
                        The objective is to find out whether there is indeed a significant difference between the salaries of men and women, and whether the difference is due to discrimination or whether it is based on another, possibly valid, determining factor.
                    </p>
                </div>
                """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div style="text-align: left;">
        <h2>
            Relationship Salary - Gender ?
        </h2>
        <p>
            The data frame omega contains the salaries for the sample of 50 executives in the company. Can we conclude that there is a significant difference between the salaries of the male and female executives?
            Note that we can perform different types of analyses, and check whether they all lead to the same conclusion. (Confidence intervals . Hypothesis testing . Correlation analysis . Regression)
            We calculate summary statistics on salary by gender. Also, create and print a dataframe where, for each gender, we show the mean, SD, sample size, the t-critical, the SE, the margin of error, and the low/high endpoints of a 95% condifence interval
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.dataframe(get_group_stat(omega, "salary"), hide_index=True)

    st.markdown("""
    <div style="text-align: left;">
        <p>
            From the analysis above, we can conclude that the difference between the relationships of salary and gender is at least 95% statistically significant. The confidence intervals of salaries of men and women do not overlap and there is an observed difference of about £10 000, leading us to an initial observation that there is gender discrimination happening.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("""
    <div style="text-align: left;">
        <h2>
            Relationship Experience - Gender ?
        </h2>
        <p>
            At the board meeting, someone raised the issue that there was indeed a substantial difference between male and female salaries, but that this was attributable to other reasons such as differences in experience. A questionnaire send out to the 50 executives in the sample reveals that the average experience of the men is approximately 21 years, whereas the women only have about 7 years experience on average (see table below).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.dataframe(get_group_stat(omega, "experience"), hide_index=True)

    st.markdown("""
    <div style="text-align: left;">
        <p>
            Based on this evidence, can we conclude that there is a significant difference between the experience of the male and female executives? Let’s perform similar analyses as in the previous section. Does our conclusion validate or endanger our conclusion about the difference in male and female salaries?
            From the analysis above, we can conclude that the difference between experience levels of males and females is at least 95% statistically signifcant. This endangers our initial conclusion that the difference in salaries between genders is solely due to discrimination. However, more analysis needs to be conducted before we can form a final conclusion.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("""
    <div style="text-align: left;">
        <h2>
            Relationship Salary - Experience ?
        </h2>
        <p>
            Someone at the meeting argues that clearly, a more thorough analysis of the relationship between salary and experience is required before any conclusion can be drawn about whether there is any gender-based salary discrimination in the company.
            We analyse the relationship between salary and experience and draw a scatterplot to visually inspect the data.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Create the plot
    fig, ax = plt.subplots(figsize=figsize)
    sns.scatterplot(x='salary', y='experience', data=omega)
    sns.regplot(x='salary', y='experience', data=omega, order=2, scatter=False, color='red')

    # Customize the plot
    plt.title('Salary by Experience', fontsize=label_font_size)
    plt.xlabel('Salary', fontsize=label_font_size)
    plt.ylabel('Experience', fontsize=label_font_size)
    plt.grid(True)
    st.pyplot(fig)

    st.markdown("""
    <div style="text-align: left;">
        <p>
            From the scatterplot above, we can see a clear correlation between salary and experience. This would confirm the argument that salary is related to experience, and reject the argument that salary is related to gender. At this point of the analysis, we could say that there is just insufficient information to tell whether there is any gender-based salary discrimination, as it seems to be more related to experience.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("""
    <div style="text-align: left;">
        <h2>
            Check correlations between the data
        </h2>
    </div>
    """, unsafe_allow_html=True)


    # Create the PairGrid
    g = sns.PairGrid(omega[['gender', 'experience', 'salary']], hue='gender', palette='Set1', diag_sharey=False)
    g.map_lower(sns.scatterplot, alpha=0.5)
    g.map_upper(sns.kdeplot)
    g.map_diag(sns.kdeplot, lw=2)

    # Add a legend
    g.add_legend()

    # Customize the plot
    g.fig.suptitle('Pairplot by Gender', y=1.02)  # Adjust the title position
    sns.set_style("whitegrid")
    sns.color_palette("muted")
    g.fig.set_size_inches(figsize[0],figsize[1])
    g.fig.suptitle('Correlations between the experience and salary')
    plt.grid(True)

    st.pyplot(g)

    st.markdown("""
    <div style="text-align: left;">
        <p>
            This salary-experience plot, organized by gender, tells us a lot. From the bottom-left of the plot, which concern employees with minimum experience, we can infer that women actually have higher salaries than men. However, as we move towards the upper-middle part of the plot, we can see that women with 15-30 years of experience are paid less than their male peers. Additionally, employees witht the most experience in the company (30-45 years), are solely male, and thus there is no way to tell whether there is any gender-based salary discrimination going on. However, it may be possible that for these senior roles, only males have been considered, as there is no woman with this much experience in this company. This would introduce another gender-based discrimination into the mix.
        </p>
    </div>
    """, unsafe_allow_html=True)

