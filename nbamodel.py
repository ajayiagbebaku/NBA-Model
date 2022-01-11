import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 1/10/2022:")
st.text("Spread Win/Loss: (128-138).481")
st.text("Over/Under Win Loss: (156-183).460")
st.text("Spread HIGH Confidence:(52-41).559")
st.text("Spread LOW Confidence:(40-48).455")
st.text("Totals HIGH Confidence:(72-72).500")
st.text("Totals LOW Confidence:(40-56).417")
st.text("Please note projections are made around 4pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)