import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/8/2021:")
st.text("Spread Win/Loss: (18-19)")
st.text("Over/Under Win Loss: (22-17)")
st.text("Please note projections are made around 8am CST each day")
df = pd.read_excel("UpdatedResults.xlsx")
st.dataframe(df)