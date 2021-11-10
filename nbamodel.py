import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/10/2021:")
st.text("Spread Win/Loss: (21-27).438")
st.text("Over/Under Win Loss: (25-25).500")
st.text("Please note projections are made around 8am CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)