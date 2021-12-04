import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 12/4/2021:")
st.text("Spread Win/Loss: (82-101).448")
st.text("Over/Under Win Loss: (90-108).465")
st.text("Spread HIGH Confidence:(20-23).465")
st.text("Spread LOW Confidence:(25-27).481")
st.text("Totals HIGH Confidence:(28-27).529")
st.text("Totals LOW Confidence:(20-31).392")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)