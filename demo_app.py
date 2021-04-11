import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import json

seen = False

region_color = {'Western Europe': 'xkcd:sky blue', 'North America and ANZ': 'xkcd:purple',
       'Middle East and North Africa': 'xkcd:royal blue', 'Latin America and Caribbean': 'xkcd:burnt orange',
       'Central and Eastern Europe': 'xkcd:gold', 'East Asia': 'xkcd:pastel green', 'Southeast Asia': 'xkcd:cerulean',
       'Commonwealth of Independent States': 'xkcd:light red', 'Sub-Saharan Africa': 'xkcd:greenish yellow',
       'South Asia': 'xkcd:pink purple'}

lan_lon = {'Finland': (63.2467777, 25.9209164),
             'Denmark': (55.670249, 10.3333283),
             'Switzerland': (46.813331250000005, 8.444947437939408),
             'Iceland': (64.9841821, -18.1059013),
             'Netherlands': (52.5001698, 5.7480821),
             'Norway': (60.5000209, 9.0999715),
             'Sweden': (59.6749712, 14.5208584),
             'Luxembourg': (49.8158683, 6.1296751),
             'New Zealand': (-41.5000831, 172.8344077),
             'Austria': (47.2, 13.2),
             'Australia': (-24.7761086, 134.755),
             'Israel': (31.5313113, 34.8667654),
             'Germany': (51.0834196, 10.4234469),
             'Canada': (61.0666922, -107.991707),
             'Ireland': (52.865196, -7.9794599),
             'Costa Rica': (9.5773243, -83.82371114343024),
             'United Kingdom': (54.7023545, -3.2765753),
             'Czech Republic': (49.8167003, 15.4749544),
             'United States': (39.7837304, -100.4458825),
             'Belgium': (50.6402809, 4.6667145),
             'France': (46.603354, 1.8883335),
             'Bahrain': (26.1551249, 50.5344606),
             'Malta': (35.9446731, 14.383630615858262),
             'Taiwan Province of China': (17.4955454, -88.18157111304902),
             'United Arab Emirates': (24.0002488, 53.9994829),
             'Saudi Arabia': (25.6242618, 42.3528328),
             'Spain': (39.3260685, -4.8379791),
             'Italy': (42.6384261, 12.674297),
             'Slovenia': (45.8133113, 14.4808369),
             'Guatemala': (15.6356088, -89.8988087),
             'Uruguay': (-32.8755548, -56.0201525),
             'Singapore': (1.357107, 103.8194992),
             'Kosovo': (42.5869578, 20.9021231),
             'Slovakia': (48.6726975, 19.63679421037233),
             'Brazil': (-10.3333333, -53.2),
             'Mexico': (22.5000485, -100.0000375),
             'Jamaica': (18.1850507, -77.3947693),
             'Lithuania': (55.3500003, 23.7499997),
             'Cyprus': (34.9823018, 33.1451285),
             'Estonia': (58.7523778, 25.3319078),
             'Panama': (8.559559, -81.1308434),
             'Uzbekistan': (41.32373, 63.9528098),
             'Chile': (-31.7613365, -71.3187697),
             'Poland': (52.215933, 19.134422),
             'Kazakhstan': (47.2286086, 65.2093197),
             'Romania': (45.9852129, 24.6859225),
             'Kuwait': (29.2733964, 47.4979476),
             'Serbia': (44.1534121, 20.55144),
             'El Salvador': (13.8000382, -88.9140683),
             'Mauritius': (-20.2759451, 57.5703566),
             'Latvia': (56.8406494, 24.7537645),
             'Colombia': (2.8894434, -73.783892),
             'Hungary': (47.1817585, 19.5060937),
             'Thailand': (14.8971921, 100.83273),
             'Nicaragua': (12.6090157, -85.2936911),
             'Japan': (36.5748441, 139.2394179),
             'Argentina': (-34.9964963, -64.9672817),
             'Portugal': (40.0332629, -7.8896263),
             'Honduras': (15.2572432, -86.0755145),
             'Croatia': (45.5643442, 17.0118954),
             'Philippines': (12.7503486, 122.7312101),
             'South Korea': (36.638392, 127.6961188),
             'Peru': (-6.8699697, -75.0458515),
             'Bosnia and Herzegovina': (44.3053476, 17.5961467),
             'Moldova': (47.2879608, 28.5670941),
             'Ecuador': (-1.3397668, -79.3666965),
             'Kyrgyzstan': (41.5089324, 74.724091),
             'Greece': (38.9953683, 21.9877132),
             'Bolivia': (-17.0568696, -64.9912286),
             'Mongolia': (46.8250388, 103.8499736),
             'Paraguay': (-23.3165935, -58.1693445),
             'Montenegro': (42.9868853, 19.5180992),
             'Dominican Republic': (19.28131815, -70.035906834967),
             'North Cyprus': (35.2244296, 33.0695987),
             'Belarus': (53.4250605, 27.6971358),
             'Russia': (64.6863136, 97.7453061),
             'Hong Kong S.A.R. of China': (22.2793278, 114.1628131),
             'Tajikistan': (38.6281733, 70.8156541),
             'Vietnam': (13.2904027, 108.4265113),
             'Libya': (26.8234472, 18.1236723),
             'Malaysia': (4.5693754, 102.2656823),
             'Indonesia': (-2.4833826, 117.8902853),
             'Congo (Brazzaville)': (-0.7179165000000001, 16.018048574081842),
             'China': (35.000074, 104.999927),
             'Ivory Coast': (7.9897371, -5.5679458),
             'Armenia': (40.7696272, 44.6736646),
             'Nepal': (28.1083929, 84.0917139),
             'Bulgaria': (42.6073975, 25.4856617),
             'Maldives': (4.7064352, 73.3287853),
             'Azerbaijan': (40.3936294, 47.7872508),
             'Cameroon': (4.6125522, 13.1535811),
             'Senegal': (14.46517725, -14.765340959100413),
             'Albania': (41.000028, 19.9999619),
             'North Macedonia': (41.6171214, 21.7168387),
             'Ghana': (7.8573710000000005, -1.0840975468820433),
             'Niger': (17.7356214, 9.3238432),
             'Turkmenistan': (39.3763807, 59.3924609),
             'Gambia': (13.44294275, -16.118732162564726),
             'Benin': (9.2231105, 2.31006719638123),
             'Laos': (20.0171109, 103.378253),
             'Bangladesh': (24.4768783, 90.2932426),
             'Guinea': (10.7226226, -10.7083587),
             'South Africa': (-28.8166236, 24.991639),
             'Turkey': (38.9597594, 34.9249653),
             'Pakistan': (30.3308401, 71.247499),
             'Morocco': (31.1728205, -7.3362482),
             'Venezuela': (8.0018709, -66.1109318),
             'Georgia': (32.3293809, -83.1137366),
             'Algeria': (28.0000272, 2.9999825),
             'Ukraine': (49.4871968, 31.2718321),
             'Iraq': (33.0955793, 44.1749775),
             'Gabon': (-0.8999695, 11.6899699),
             'Burkina Faso': (12.0753083, -1.6880314),
             'Cambodia': (13.5066394, 104.869423),
             'Mozambique': (-19.302233, 34.9144977),
             'Nigeria': (9.6000359, 7.9999721),
             'Mali': (16.3700359, -2.2900239),
             'Iran': (32.6475314, 54.5643516),
             'Uganda': (1.5333554, 32.2166578),
             'Liberia': (5.7499721, -9.3658524),
             'Kenya': (1.4419683, 38.4313975),
             'Tunisia': (33.8439408, 9.400138),
             'Lebanon': (33.8750629, 35.843409),
             'Namibia': (-23.2335499, 17.3231107),
             'Palestinian Territories': (31.94696655, 35.27386547291496),
             'Myanmar': (17.1750495, 95.9999652),
             'Jordan': (31.1667049, 36.941628),
             'Chad': (15.6134137, 19.0156172),
             'Sri Lanka': (7.5554942, 80.7137847),
             'Swaziland': (-26.5624806, 31.3991317),
             'Comoros': (-12.2045176, 44.2832964),
             'Egypt': (26.2540493, 29.2675469),
             'Ethiopia': (10.2116702, 38.6521203),
             'Mauritania': (20.2540382, -9.2399263),
             'Madagascar': (-18.9249604, 46.4416422),
             'Togo': (8.7800265, 1.0199765),
             'Zambia': (-14.5189121, 27.5589884),
             'Sierra Leone': (8.6400349, -11.8400269),
             'India': (22.3511148, 78.6677428),
             'Burundi': (-3.3634357, 29.8870575),
             'Yemen': (16.3471243, 47.8915271),
             'Tanzania': (-6.5247123, 35.7878438),
             'Haiti': (19.1399952, -72.3570972),
             'Malawi': (-13.2687204, 33.9301963),
             'Lesotho': (-29.6039267, 28.3350193),
             'Botswana': (-23.1681782, 24.5928742),
             'Rwanda': (-1.9646631, 30.0644358),
             'Zimbabwe': (-19.01688, 29.35365015971339),
             'Afghanistan': (33.7680065, 66.2385139)}

with st.echo(code_location='below'):
    st.title("2021 World Happiness Report Dashboard")

    st.header("World review")

    data = pd.read_csv("dataset.csv")

    st.write('В своем проекте я рассматриваю влияние различных критериев на уровень счастья.')

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)

    # FIRST CHART (PT1)

    st.write('Распространено мнение, что там, где люди богаче, там они счастливее. '
             'На графике Вы можете видеть (если нажмете show regression) зависимость между ВВП на душу населения '
             'и уровнем счастья государства. Также с помощью слайдера вы можете выбирать количество стран, '
             'которе необходимо отобразить, где справа расположены самые бедные, а слева самые богатые государства '
             '(с самым большим ВВП на душу населения)')

    values = st.slider('Select a range of values', min_value=1,
                       max_value=data.shape[0],
                       value=(int(data.shape[0] / 4), int(3 * data.shape[0] / 4)),
                       step=1,
                       key="slider1")
    df = data[["Ladder score", "Logged GDP per capita", "Country name"]].copy()
    df.rename(columns={"Logged GDP per capita": "GDP per capita", "Ladder score": "Happiness level"}, inplace=True)
    df.sort_values("GDP per capita", inplace=True)
    cf = df.copy()
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
    if st.checkbox("Show regression", key="checkbox3"):
        sns.regplot(x='GDP per capita', y='Happiness level', data=df, ci=None, order=2, scatter_kws={'color': 'white'},
                    line_kws={'color': 'red'})
    st.pyplot(fig)

    # FIRST CHART (PT2)
    st.write('Также можно посмотреть, как соответствуют разные регионы общему тренду. '
             'Вы можете выбрать один или несколько регионов из списка и '
             'посмотреть как их расположения соотносится с общий для всех стран регрессией')

    regions = st.multiselect('Выберите регион:', data["Regional indicator"].unique())
    df = data[data["Regional indicator"].isin(regions)].copy()
    df.rename(columns={"Logged GDP per capita": "GDP per capita", "Ladder score": "Happiness level"}, inplace=True)
    df.sort_values("GDP per capita", inplace=True)
    df.set_index("Country name", inplace=True)

    fig = plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')

    for country, info in df.iterrows():
        x = info['GDP per capita']
        y = info['Happiness level']
        plt.scatter(x, y, s=100, color=region_color[info["Regional indicator"]])
        plt.text(x, y, country, fontsize=8)

    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.title("GDP per capita / Happiness level", fontsize=22)
    plt.xlabel("GDP per capita", fontsize=22)
    plt.ylabel("Happiness level", fontsize=22)
    if st.checkbox("Show regression", key="checkbox1"):
        sns.regplot(x='GDP per capita', y='Happiness level', data=cf, ci=None, order=2, scatter_kws={'color': 'white'},
                    line_kws={'color': 'red'})
    st.pyplot(fig)

    # GIF
    st.write('Важным я считаю показать необходимость большой выборки. '
             'Ниже Вы можете посмотреть как выборка влияет на вид регрессии. ')
    st.image('celluloid_subplots.gif')

    # SECOND CHART
    st.write('Далее посмотрим на влияние других факторов на уровень счастья. '
             'Вы можете выбрать критерий и выборку стран, '
             'чтобы посмотреть зависимость уровня счастья от выбранного фактора')
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
    st.write('Теперь рассмотрим данные на одной стране. '
             'Ниже вы можете выбрать страну и посмотреть как соотносятся данные это страны со средним мировым уровнем.')

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

    # FOURTH CHART
    st.write('На последнем графике рассмотрен другой датасет о терроризме. '
             'На карте ниже Вы можете видеть географическое расположение террористических атак(красный) '
             'и уровень счастья в этом государстве(синий). Более того, чем больше уровень счастья, '
             'тем больше синий круг, а чем больше количество террористических атак в этой стране, '
             'тем больше красный круг')
    st.subheader("Number of terroristic attacks (1970 - 2017) / Happiness level")
    df = data[['Country name', 'Ladder score']].copy()
    years = pd.read_csv('num_of_attacks.csv')
    years.set_index('Country name', inplace=True)
    df.set_index('Country name', inplace=True)
    df = df.merge(years, left_index=True, right_index=True)
    df.rename(columns={"Ladder score": "Happiness level"}, inplace=True)
    lat = [lan_lon[country][0] for country in df.index.tolist()]
    lon = [lan_lon[country][1] for country in df.index.tolist()]
    df['lat'] = lat
    df['lon'] = lon
    df.reset_index(inplace=True)

    fig1 = px.scatter_geo(df, lat='lat', lon='lon',
                          size="# of attacks", hover_name="Country name")
    fig2 = px.scatter_geo(df, lat='lat', lon='lon',
                          size="Happiness level", hover_name="Country name")

    fig = px.scatter_geo()
    fig.add_traces(fig1._data)
    fig.add_traces(fig2._data)
    fig.data[0].marker.color = 'rgba(255,0,0,0.4)'
    fig.data[1].marker.color = 'rgba(0,0,255,0.3)'
    st.plotly_chart(fig)

    opinion = st.radio("Вам понравилось?", ['ДА', 'НЕТ'])
    submit = st.button('Submit')
    if submit:
        with open('stats.json', 'r') as file:
            data = json.load(file)
            if opinion == 'ДА':
                data['yes'] += 1
            else:
                data['no'] += 1
        with open('stats.json', 'w') as file:
            json.dump(data, file)
        st.balloons()
        submit = False
