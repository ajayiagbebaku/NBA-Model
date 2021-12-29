import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 12/28/2021:")
st.text("Spread Win/Loss: (111-117).487")
st.text("Over/Under Win Loss: (123-141).466")
st.text("Spread HIGH Confidence:(43-31).581")
st.text("Spread LOW Confidence:(31-36).469")
st.text("Totals HIGH Confidence:(47-45).511")
st.text("Totals LOW Confidence:(33-43).434")
st.text("Please note projections are made around 4pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)