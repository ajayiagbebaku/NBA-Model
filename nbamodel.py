import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/28/2021:")
st.text("Spread Win/Loss: (75-90).455")
st.text("Over/Under Win Loss: (81-92).470")
st.text("Spread HIGH Confidence:(17-18).486")
st.text("Spread LOW Confidence:(21-20).512")
st.text("Totals HIGH Confidence:(21-16).568")
st.text("Totals LOW Confidence:(18-26).409")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)