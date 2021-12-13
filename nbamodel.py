import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 12/13/2021:")
st.text("Spread Win/Loss: (101-110).479")
st.text("Over/Under Win Loss: (110-128).462")
st.text("Spread HIGH Confidence:(35-29).547")
st.text("Spread LOW Confidence:(29-30).492")
st.text("Totals HIGH Confidence:(41-37).526")
st.text("Totals LOW Confidence:(27-39).409")
st.text("Please note projections are made around 4pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)