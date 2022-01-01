import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NBA",layout="wide")
st.header("Today's Predictions 1/1/2022:")
st.text("Spread Win/Loss: (115-127).475")
st.text("Over/Under Win Loss: (131-148).471")
st.text("Spread HIGH Confidence:(44-37).543")
st.text("Spread LOW Confidence:(34-40).459")
st.text("Totals HIGH Confidence:(54-49).524")
st.text("Totals LOW Confidence:(34-46).425")
st.text("Please note projections are made around 4pm CST each day")
df_results = pd.read_excel("UpdatedResults.xlsx")

st.dataframe(df_results)