import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/22/2021:")
st.text("Spread Win/Loss: (62-80).437")
st.text("Over/Under Win Loss: (69-76).476")
st.text("Spread HIGH Confidence:(11-12).478")
st.text("Spread LOW Confidence:(14-17).452")
st.text("Totals HIGH Confidence:(13-8).619")
st.text("Totals LOW Confidence:(13-19).414")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)