#import openaq
import pandas as pd
#api = openaq.OpenAQ()
#cdf = api.cities(country='CL', df=True)

df = pd.read_csv('azufre.csv')

import streamlit as st

st.dataframe(df)
