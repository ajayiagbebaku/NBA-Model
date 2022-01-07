import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 1/7/2022:")
st.text("Spread Win/Loss: (123-136).475")
st.text("Over/Under Win Loss: (145-169).462")
st.text("Spread HIGH Confidence:(48-40).545")
st.text("Spread LOW Confidence:(38-46).452")
st.text("Totals HIGH Confidence:(65-64).504")
st.text("Totals LOW Confidence:(38-54).413")
st.text("Please note projections are made around 4pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)