import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 12/6/2021:")
st.text("Spread Win/Loss: (83-102).449")
st.text("Over/Under Win Loss: (93-110).458")
st.text("Spread HIGH Confidence:(21-24).467")
st.text("Spread LOW Confidence:(25-27).481")
st.text("Totals HIGH Confidence:(30-29).508")
st.text("Totals LOW Confidence:(21-31).404")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)