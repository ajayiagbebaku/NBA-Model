import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 12/15/2021:")
st.text("Spread Win/Loss: (105-114).479")
st.text("Over/Under Win Loss: (115-132).466")
st.text("Spread HIGH Confidence:(38-30).559")
st.text("Spread LOW Confidence:(30-34).469")
st.text("Totals HIGH Confidence:(43-40).518")
st.text("Totals LOW Confidence:(30-40).429")
st.text("Please note projections are made around 4pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)