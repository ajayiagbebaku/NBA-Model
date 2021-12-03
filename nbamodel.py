import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 12/2/2021:")
st.text("Spread Win/Loss: (82-98).456")
st.text("Over/Under Win Loss: (88-104).458")
st.text("Spread HIGH Confidence:(20-22).476")
st.text("Spread LOW Confidence:(25-25).500")
st.text("Totals HIGH Confidence:(27-24).529")
st.text("Totals LOW Confidence:(19-30).388")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)