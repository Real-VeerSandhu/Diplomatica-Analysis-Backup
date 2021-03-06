import streamlit as st
import pandas as pd
import plotly.express as px


def app():
    st.markdown('## Analyze')

    st.markdown("""
    Examine numerical metrics and through interactive charts
    """)

    full_gdp = pd.read_csv('data/gdp.csv')
    full_gdp = full_gdp.drop(columns='Unnamed: 0')

    full_imports = pd.read_csv('data/imports.csv')
    full_imports = full_imports.drop(columns='Unnamed: 0')

    full_pop = pd.read_csv('data/population.csv')
    full_pop = full_pop.drop(columns='Unnamed: 0')

    fig1 = px.line(full_gdp, x='Year', y='GDP', color='Country', title='GDP over Time (Canada vs Australia)')
    fig2 = px.line(full_imports, x='Year', y='Imports of Goods and Services (% GDP)', color='Country', title='Imports of Goods and Services over Time (Canada vs Australia)')    
    fig3 = px.line(full_pop, x='Year', y='Population', color='Country', title='Population over Time (Canada vs Australia)')

    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    st.plotly_chart(fig3)