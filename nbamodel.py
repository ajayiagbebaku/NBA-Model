import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 12/7/2021:")
st.text("Spread Win/Loss: (86-102).457")
st.text("Over/Under Win Loss: (94-115).450")
st.text("Spread HIGH Confidence:(24-24).500")
st.text("Spread LOW Confidence:(25-27).481")
st.text("Totals HIGH Confidence:(31-32).492")
st.text("Totals LOW Confidence:(21-33).389")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)