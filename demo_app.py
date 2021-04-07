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

    values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
    st.write('Values:', values)

    slider = st.slider("Выберите кол-во стран:",
                       min_value=1,
                       max_value=data.shape[0],
                       value=int(data.shape[0] / 2),
                       step=1)
    st.write("#", slider)
    df = data[["Ladder score", "Logged GDP per capita", "Country name"]]
    df = df[df["Logged GDP per capita"] >= df["Logged GDP per capita"].sort_values(ascending=False).iloc[slider - 1]]
    df.set_index("Country name", inplace=True)

    fig = plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')

    for country, info in df.iterrows():
        x = info['Logged GDP per capita']
        y = info['Ladder score']
        plt.scatter(x, y, s=100)
        plt.text(x, y, country, fontsize=8)

    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.title("Logged GDP per capita / Ladder score", fontsize=22)
    plt.xlabel("Logged GDP per capita", fontsize=22)
    plt.ylabel("Happiness level", fontsize=22)
    if st.checkbox("Show regression"):
        sns.regplot(x='Logged GDP per capita', y='Ladder score', data=df, ci=None, order=2, scatter_kws={'color': 'white'},
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
