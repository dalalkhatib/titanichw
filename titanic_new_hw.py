import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

st.title("New Homework with streamlit")
st.header("EXPLORING THE TITANIC DATASET")
st.header("1.Inspecting the Data")
df = pd.read_csv("titanic.csv")
df.dropna(subset = ["Age"], inplace=True)
st.write(df)




#AGE FILTER
sidebar_option = st.sidebar.beta_expander('Age Range')
min_age = 0
max_age = 80
age = sidebar_option.slider('Min age', int(min(df['Age'])), int(max(df['Age'])) - 10, value=(min_age, max_age), step=10)
cmin_age = df.Age >= age[0]
cmax_age = df.Age <= age[1]
sidebar_option.markdown(" *** ")

#VISUALIZATION
st.header("2.Visualizing the Data")
st.subheader("2.1 Histogram")

if st.checkbox('Show Age Histogram'):
    st.subheader('Age Histogram')
    fig1, ax = plt.subplots()
    df.hist(
        bins=8,
        column="Age",
        grid=False,
        figsize=(8, 8),
        color="#86bf91",
        zorder=2,
        rwidth=0.9,
        ax=ax,
      )
    st.write(fig1)



if st.checkbox('Show Fare Histogram'):
    st.subheader('Fare Histogram')
    fig2, ax = plt.subplots()
    df.hist(
        bins=8,
        column="Fare",
        grid=False,
        figsize=(7, 7),
        color="#ff2b2b",
        zorder=2,
        rwidth=0.9,
        ax=ax,
      )
    st.write(fig2)

st.subheader("2.2 Class Distribution")

if st.checkbox('Show Class Distribution Function of Age'):
    st.subheader('Class-Age Distribution')
    a = df[df['Pclass']==1]['Age']
    b = df[df['Pclass']==2]['Age']
    c= df[df['Pclass']==3]['Age']
    hist_data = [a, b, c]
    group_labels = ['1', '2', '3']
    fig3 = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
    st.plotly_chart(fig3, use_container_width=True)


if st.checkbox('Show Class Distribution Function of Fare'):
    st.subheader('Class-Fare Distribution')
    a = df[df['Pclass']==1]['Fare']
    b = df[df['Pclass']==2]['Fare']
    c= df[df['Pclass']==3]['Fare']
    hist_data = [a, b, c]
    group_labels = ['1', '2', '3']
    fig4 = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
    st.plotly_chart(fig4, use_container_width=True)

if st.checkbox('Show Class Distribution Function of Fare'):
    st.markdown('Streamlit is **_really_ cool** :sunglasses:')
    st.balloons()
