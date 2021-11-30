import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/30/2021:")
st.text("Spread Win/Loss: (80-93).462")
st.text("Over/Under Win Loss: (86-98).467")
st.text("Spread HIGH Confidence:(20-20).500")
st.text("Spread LOW Confidence:(25-21).543")
st.text("Totals HIGH Confidence:(23-21).523")
st.text("Totals LOW Confidence:(19-27).413")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)