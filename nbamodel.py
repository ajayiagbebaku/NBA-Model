import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/19/2021:")
st.text("Spread Win/Loss: (50-69).420")
st.text("Over/Under Win Loss: (59-63).484")
st.text("Spread HIGH Confidence:(6-7).462")
st.text("Spread LOW Confidence:(7-11).389")
st.text("Totals HIGH Confidence:(9-4).692")
st.text("Totals LOW Confidence:(7-11).389")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)