import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 12/10/2021:")
st.text("Spread Win/Loss: (94-105).472")
st.text("Over/Under Win Loss: (101-121).457")
st.text("Spread HIGH Confidence:(31-27).534")
st.text("Spread LOW Confidence:(26-27).491")
st.text("Totals HIGH Confidence:(35-34).507")
st.text("Totals LOW Confidence:(26-37).390")
st.text("Please note projections are made around 4pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)