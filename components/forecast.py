import streamlit as st
import pandas as pd
import plotly.express as px

def predict(country, metric):
    canada = {'GDP': 1.5, 'Imports': 30, 'Population': 39}
    australia = {'GDP': 1.2, 'Imports': 18, 'Population': 27}

def app():
    st.write("## 2022 Forecasted Metrics")
    st.write("""
    **Linear Regression**
    - GDP (Canada): `$1.5` Trillion
    - GDP (Australia): `$1.2` Trillion
    - Imported Goods (Canada): `30%` of GDP
    - Imported Good (Australia): `18%` of GDP
    - Population (Canada): `39` Million
    - Population (Australia): `27` Million
    """)