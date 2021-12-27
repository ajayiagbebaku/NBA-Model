import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 12/27/2021:")
st.text("Spread Win/Loss: (109-115).487")
st.text("Over/Under Win Loss: (118-139).459")
st.text("Spread HIGH Confidence:(42-31).575")
st.text("Spread LOW Confidence:(30-34).469")
st.text("Totals HIGH Confidence:(45-44).506")
st.text("Totals LOW Confidence:(31-42).425")
st.text("Please note projections are made around 4pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)