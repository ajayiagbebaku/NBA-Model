import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/29/2021:")
st.text("Spread Win/Loss: (76-92).452")
st.text("Over/Under Win Loss: (83-94).469")
st.text("Spread HIGH Confidence:(17-19).472")
st.text("Spread LOW Confidence:(22-21).512")
st.text("Totals HIGH Confidence:(23-17).575")
st.text("Totals LOW Confidence:(18-27).400")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)