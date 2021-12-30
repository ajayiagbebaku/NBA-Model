import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 12/29/2021:")
st.text("Spread Win/Loss: (113-121).483")
st.text("Over/Under Win Loss: (125-144).465")
st.text("Spread HIGH Confidence:(44-33).571")
st.text("Spread LOW Confidence:(32-38).457")
st.text("Totals HIGH Confidence:(49-47).510")
st.text("Totals LOW Confidence:(33-44).429")
st.text("Please note projections are made around 4pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)