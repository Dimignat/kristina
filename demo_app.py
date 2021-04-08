import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

with st.echo(code_location='below'):
    st.title("2021 World Happiness Report Dashboard")

    st.header("World review")

    data = pd.read_csv("dataset.csv")

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)

    # FIRST CHART

    values = st.slider('Select a range of values', min_value=1,
                       max_value=data.shape[0],
                       value=(int(data.shape[0] / 4), int(3 * data.shape[0] / 4)),
                       step=1,
                       key="slider1")
    df = data[["Ladder score", "Logged GDP per capita", "Country name"]].copy()
    df.rename(columns={"Logged GDP per capita": "GDP per capita", "Ladder score": "Happiness level"}, inplace=True)
    df.sort_values("GDP per capita", inplace=True)
    df = df[(df["GDP per capita"] >= df["GDP per capita"].iloc[values[0] - 1]) &
            (df["GDP per capita"] <= df["GDP per capita"].iloc[values[1] - 1])]
    df.set_index("Country name", inplace=True)

    fig = plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')

    for country, info in df.iterrows():
        x = info['GDP per capita']
        y = info['Happiness level']
        plt.scatter(x, y, s=100)
        plt.text(x, y, country, fontsize=8)

    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.title("GDP per capita / Happiness level", fontsize=22)
    plt.xlabel("GDP per capita", fontsize=22)
    plt.ylabel("Happiness level", fontsize=22)
    if st.checkbox("Show regression", key="checkbox1"):
        sns.regplot(x='GDP per capita', y='Happiness level', data=df, ci=None, order=2, scatter_kws={'color': 'white'},
                    line_kws={'color': 'red'})
    st.pyplot(fig)

    # GIF
    #with open('celluloid_subplots.gif')
    st.image('celluloid_subplots.gif')


    # SECOND CHART
    options = data.columns.copy()
    options = options.drop(['Country name', 'Regional indicator', 'Logged GDP per capita', 'Ladder score',
                            'Standard error of ladder score', 'upperwhisker', 'lowerwhisker'])
    option = st.selectbox('Select criterion', tuple(options))

    values = st.slider('Select a range of values', min_value=1,
                       max_value=data.shape[0],
                       value=(int(data.shape[0] / 4), int(3 * data.shape[0] / 4)),
                       step=1,
                       key="slider2")

    df = data[["Ladder score", option, "Country name"]].copy()
    df.rename(columns={"Ladder score": "Happiness level"}, inplace=True)
    df.sort_values(option, inplace=True)
    df = df[(df[option] >= df[option].iloc[values[0] - 1]) &
            (df[option] <= df[option].iloc[values[1] - 1])]
    df.set_index("Country name", inplace=True)

    fig = plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')

    for country, info in df.iterrows():
        x = info[option]
        y = info['Happiness level']
        plt.scatter(x, y, s=100)
        plt.text(x, y, country, fontsize=8)

    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.title(f"{option} / Happiness level", fontsize=22)
    plt.xlabel(option, fontsize=22)
    plt.ylabel("Happiness level", fontsize=22)
    if st.checkbox("Show regression", key="checkbox2"):
        sns.regplot(x=option, y='Happiness level', data=df, ci=None, order=2, scatter_kws={'color': 'white'},
                    line_kws={'color': 'red'})
    st.pyplot(fig)

    # THIRD CHART
    countries = data["Country name"].copy().sort_values()
    country = st.selectbox('Select country', tuple(countries))
    total_mean = data.mean()
    country_mean = data[data["Country name"] == country].mean()
    output = pd.DataFrame([total_mean, country_mean], index=["Overall", country]).transpose()
    output.drop(["Healthy life expectancy", 'Standard error of ladder score',
                 'upperwhisker', 'lowerwhisker'], inplace=True)

    fig, axs = plt.subplots(1, len(output.index), figsize=(16, 8))
    fig.tight_layout()
    for ax, r in zip(axs, output.index):
        order = 3
        if output["Overall"][r] > output[country][r]:
            order = 1
        ax.bar(r, output["Overall"][r], zorder=order, color='xkcd:sky blue')
        ax.bar(r, output[country][r], zorder=2, color='tab:pink')
        ax.set_xticks([r])
        ax.set_xticklabels([r], rotation=90)
    ax.legend(["Overall", country])
    st.pyplot(fig)
