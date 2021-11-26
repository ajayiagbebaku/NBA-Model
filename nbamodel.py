import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/26/2021:")
st.text("Spread Win/Loss: (66-87).431")
st.text("Over/Under Win Loss: (73-86).459")
st.text("Spread HIGH Confidence:(13-17).433")
st.text("Spread LOW Confidence:(16-18).471")
st.text("Totals HIGH Confidence:(16-11).593")
st.text("Totals LOW Confidence:(15-25).375")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)