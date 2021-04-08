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
                       step=1)
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



    # SECOND CHART
    options = data.columns.copy()
    options = options.drop(['Country name', 'Regional indicator', 'Logged GDP per capita', 'Ladder score'])
    option = st.selectbox('Select criterion', tuple(options))

    df = data[["Ladder score", option, "Country name"]].copy()
    df.rename(columns={"Ladder score": "Happiness level"}, inplace=True)
    df.sort_values(option, inplace=True)
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

    # """
    # This is a test.
    # """
  #   x = np.linspace(0, 10, 500)
  #   fig = plt.figure()
  #   plt.plot(x, np.sin(x))
  #   plt.ylim(-2, 2)
  #   st.pyplot(fig)
  #
  #   st.write("Here's our first attempt at using data to create a table:")
  #   st.write(pd.DataFrame({
  #   'first column': [1, 2, 3, 4],
  #   'second column': [10, 20, 30, 40]
  #   }))
  #
  #   chart_data = pd.DataFrame(
  #    np.random.randn(20, 3),
  #    columns=['a', 'b', 'c'])
  #
  #   st.line_chart(chart_data)
  #
  #   df = pd.DataFrame({
  # 'first column': [1, 2, 3, 4],
  # 'second column': [10, 20, 30, 40]
  #   })
  #
  #   map_data = pd.DataFrame(
  #   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
  #   columns=['lat', 'lon'])
  #
  #   st.map(map_data)
  #
  #   if st.checkbox('Show dataframe'):
  #       chart_data = pd.DataFrame(
  #          np.random.randn(20, 3),
  #          columns=['a', 'b', 'c'])
  #       chart_data
  #
  #   df
  #
  #   option = st.sidebar.selectbox(
  #   'Which number do you like best?',
  #    df['first column'])
  #
  #   'You selected:', option
  #
  #   left_column, right_column = st.beta_columns(2)
  #   pressed = left_column.button('Press me?')
  #   if pressed:
  #       right_column.write("Woohoo!")
  #
  #   expander = st.beta_expander("FAQ")
  #   expander.write("Here you could put in some really, really long explanations...")
