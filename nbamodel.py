import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/18/2021:")
st.text("Spread Win/Loss: (45-62).421")
st.text("Over/Under Win Loss: (50-60).455")
st.text("Spread HIGH Confidence:(5-6)")
st.text("Spread LOW Confidence:(4-10)")
st.text("Totals HIGH Confidence:(8-4")
st.text("Totals LOW Confidence:(4-9)")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)