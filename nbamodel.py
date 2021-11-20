import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/20/2021:")
st.text("Spread Win/Loss: (55-73).430")
st.text("Over/Under Win Loss: (63-68).481")
st.text("Spread HIGH Confidence:(8-10).444")
st.text("Spread LOW Confidence:(10-12).455")
st.text("Totals HIGH Confidence:(10-7).588")
st.text("Totals LOW Confidence:(10-12).455")
st.text("Please note projections are made around 12pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)