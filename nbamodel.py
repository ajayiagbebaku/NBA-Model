import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/12/2021:")
st.text("Spread Win/Loss: (26-37).413")
st.text("Over/Under Win Loss: (33-33).500")
st.text("Please note projections are made around 9am CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)