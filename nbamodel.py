import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/24/2021:")
st.text("Spread Win/Loss: (64-85).430")
st.text("Over/Under Win Loss: (71-80).470")
st.text("Spread HIGH Confidence:(12-15).462")
st.text("Spread LOW Confidence:(15-18).469")
st.text("Totals HIGH Confidence:(14-9).609")
st.text("Totals LOW Confidence:(14-22).389")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)