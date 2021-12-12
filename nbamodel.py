import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 12/12/2021:")
st.text("Spread Win/Loss: (98-108).476")
st.text("Over/Under Win Loss: (107-125).461")
st.text("Spread HIGH Confidence:(34-29).540")
st.text("Spread LOW Confidence:(27-28).491")
st.text("Totals HIGH Confidence:(39-37).513")
st.text("Totals LOW Confidence:(26-37).413")
st.text("Please note projections are made around 4pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)