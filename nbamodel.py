import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/21/2021:")
st.text("Spread Win/Loss: (59-78).431")
st.text("Over/Under Win Loss: (66-74).481")
st.text("Spread HIGH Confidence:(9-11).450")
st.text("Spread LOW Confidence:(13-16).448")
st.text("Totals HIGH Confidence:(11-8).579")
st.text("Totals LOW Confidence:(12-17).414")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)