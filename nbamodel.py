import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/16/2021:")
st.text("Spread Win/Loss: (41-58).414")
st.text("Over/Under Win Loss: (46-56).451")
st.text("Spread HIGH Confidence:(2-4)")
st.text("Spread LOW Confidence:(2-3)")
st.text("Totals HIGH Confidence:(2-3")
st.text("Totals LOW Confidence:(1-5)")
st.text("Please note projections are made around 9am CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)