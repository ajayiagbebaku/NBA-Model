import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 12/31/2021:")
st.text("Spread Win/Loss: (115-124).481")
st.text("Over/Under Win Loss: (130-146).471")
st.text("Spread HIGH Confidence:(44-35).557")
st.text("Spread LOW Confidence:(34-39).466")
st.text("Totals HIGH Confidence:(53-47).53")
st.text("Totals LOW Confidence:(34-46).425")
st.text("Please note projections are made around 4pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)