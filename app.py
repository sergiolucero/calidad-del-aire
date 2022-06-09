import openaq
import pandas as pd
import altair as alt

api = openaq.OpenAQ()
cdf = api.cities(country='CL', df=True)

df = pd.read_csv('azufre.csv')

import streamlit as st

# azufre tiene toda la data para generar un altair stock plot


c = alt.Chart(df).mark_line().encode(
    x='fecha',
    y='value',
    color='city'
    #strokeDash='symbol',
)

st.altair_chart(c)
st.dataframe(df)
