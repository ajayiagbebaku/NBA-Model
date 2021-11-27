import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/27/2021:")
st.text("Spread Win/Loss: (72-89).447")
st.text("Over/Under Win Loss: (79-89).470")
st.text("Spread HIGH Confidence:(14-18).438")
st.text("Spread LOW Confidence:(21-19).525")
st.text("Totals HIGH Confidence:(20-13).606")
st.text("Totals LOW Confidence:(17-26).395")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)