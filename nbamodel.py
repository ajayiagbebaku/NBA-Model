import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 1/4/2022:")
st.text("Spread Win/Loss: (119-132).474")
st.text("Over/Under Win Loss: (136-159).461")
st.text("Spread HIGH Confidence:(45-37).549")
st.text("Spread LOW Confidence:(37-45).451")
st.text("Totals HIGH Confidence:(57-60).487")
st.text("Totals LOW Confidence:(37-50).425")
st.text("Please note projections are made around 4pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)