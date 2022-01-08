import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 1/8/2022:")
st.text("Spread Win/Loss: (125-137).477")
st.text("Over/Under Win Loss: (148-175).458")
st.text("Spread HIGH Confidence:(49-40).551")
st.text("Spread LOW Confidence:(39-48).448")
st.text("Totals HIGH Confidence:(66-68).493")
st.text("Totals LOW Confidence:(39-55).413")
st.text("Please note projections are made around 4pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)