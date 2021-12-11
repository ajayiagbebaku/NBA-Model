import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 12/11/2021:")
st.text("Spread Win/Loss: (97-106).478")
st.text("Over/Under Win Loss: (103-124).454")
st.text("Spread HIGH Confidence:(34-27).557")
st.text("Spread LOW Confidence:(26-28).481")
st.text("Totals HIGH Confidence:(37-36).507")
st.text("Totals LOW Confidence:(24-37).393")
st.text("Please note projections are made around 4pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)