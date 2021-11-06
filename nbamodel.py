import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 11/6/2021:")
st.text("Spread Win/Loss: (9-14)")
st.text("Over/Under Win Loss: (16-9)")
df = pd.read_excel("UpdatedResults.xlsx")
st.dataframe(df)