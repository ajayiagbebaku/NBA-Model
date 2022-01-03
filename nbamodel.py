import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 1/3/2022:")
st.text("Spread Win/Loss: (118-131).474")
st.text("Over/Under Win Loss: (131-156).456")
st.text("Spread HIGH Confidence:(45-37).549")
st.text("Spread LOW Confidence:(36-44).450")
st.text("Totals HIGH Confidence:(55-58).487")
st.text("Totals LOW Confidence:(34-49).410")
st.text("Please note projections are made around 4pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)