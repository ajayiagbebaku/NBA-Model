import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 12/9/2021:")
st.text("Spread Win/Loss: (91-105).464")
st.text("Over/Under Win Loss: (100-119).457")
st.text("Spread HIGH Confidence:(28-27).509")
st.text("Spread LOW Confidence:(26-27).491")
st.text("Totals HIGH Confidence:(35-33).515")
st.text("Totals LOW Confidence:(23-36).390")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)