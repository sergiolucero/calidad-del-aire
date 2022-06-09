#import openaq
import pandas as pd
import altair as alt
import streamlit as st

#api = openaq.OpenAQ()
#cdf = api.cities(country='CL', df=True)

df = pd.read_csv('azufre.csv')

c = alt.Chart(df).mark_line().encode(
    x='fecha',
    y='value',
    color='city'
    #strokeDash='symbol',
)

st.altair_chart(c)
st.dataframe(df)
