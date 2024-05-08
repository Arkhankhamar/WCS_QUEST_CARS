import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(page_title="Exercice WCS Dataframe Voitures")

@st.cache_data
def data():
    df_car = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')
    return df_car

df = data()

st.header('Bienvenue sur la quête "voitures"')


with st.sidebar:
    st.header("Options")
    st.image('./header.png')
    choix_cols = st.multiselect("Choix des pays",list(df['continent'].unique()))
    choix_cols = st.multiselect("Choix nombre de cylindres", list(df['cylinders'].unique()))


fig_1 = sns.stripplot(df, x='continent', y='hp', hue ='cylinders' )
st.pyplot(fig_1.figure)