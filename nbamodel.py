import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/14/2021:")
st.text("Spread Win/Loss: (37-51).42")
st.text("Over/Under Win Loss: (39-45).473")
st.text("Spread HIGH Confidence:")
st.text("Spread LOW Confidence:")
st.text("Totals HIGH Confidence:")
st.text("Totals LOW Confidence:")
st.text("Please note projections are made around 9am CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)