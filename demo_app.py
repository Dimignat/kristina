import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

with st.echo(code_location='below'):
    st.title("2021 World Happiness Report Dashboard")

    st.header("World review")

    data = pd.read_csv("dataset.csv")

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)
    chart_data = data[["Ladder score", "Logged GDP per capita", "Country name"]]
    chart_data.set_index('Country name', inplace=True)
    st.bar_chart(chart_data)
    """
    This is a test.
    """
    x = np.linspace(0, 10, 500)
    fig = plt.figure()
    plt.plot(x, np.sin(x))
    plt.ylim(-2, 2)
    st.pyplot(fig)

    st.write("Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    }))

    chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

    df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
    })

    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(map_data)

    if st.checkbox('Show dataframe'):
        chart_data = pd.DataFrame(
           np.random.randn(20, 3),
           columns=['a', 'b', 'c'])
        chart_data

    df
    
    option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

    'You selected:', option

    left_column, right_column = st.beta_columns(2)
    pressed = left_column.button('Press me?')
    if pressed:
        right_column.write("Woohoo!")

    expander = st.beta_expander("FAQ")
    expander.write("Here you could put in some really, really long explanations...")
