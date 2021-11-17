import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/17/2021:")
st.text("Spread Win/Loss: (43-59).422")
st.text("Over/Under Win Loss: (48-57).457")
st.text("Spread HIGH Confidence:(3-4)")
st.text("Spread LOW Confidence:(3-4)")
st.text("Totals HIGH Confidence:(4-4")
st.text("Totals LOW Confidence:(1-5)")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)