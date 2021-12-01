import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 12/1/2021:")
st.text("Spread Win/Loss: (80-95).457")
st.text("Over/Under Win Loss: (88-99).471")
st.text("Spread HIGH Confidence:(20-21).488")
st.text("Spread LOW Confidence:(23-23).500")
st.text("Totals HIGH Confidence:(27-21).563")
st.text("Totals LOW Confidence:(19-28).404")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)