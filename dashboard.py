# dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Heart Health Dashboard")

df = pd.DataFrame({
    "Age": [45, 60, 35],
    "Risk Score": [0.2, 0.8, 0.5],
    "Gender": ["Male", "Female", "Male"]
})

fig = px.scatter(df, x="Age", y="Risk Score", color="Gender")
st.plotly_chart(fig)
