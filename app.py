# Main app page (sets up navigation and routing)

import streamlit as st
from multiapp import MultiApp
from components import forecast, analyze

# Set up MultiApp feature (allows for multiple pages)
app = MultiApp()

st.set_page_config(page_title="Diplomatica Forecasting App", page_icon="📊", layout='centered', initial_sidebar_state="collapsed")

st.title('Forecast and Analyze Data')


st.markdown("""
Visualize geo-political data and extrapolate new information
""")

st.markdown('<button style="border-color: black; border-radius: 10;" ><a style="-webkit-appearance: button; -moz-appearance: button; appearance: button; text-decoration: none; color: initial;" href="https://diplomatica.vercel.app/dashboard" target="_blank">Return to Dashboard</a></button>', unsafe_allow_html=True)

# Other pages
app.add_app("Analyze", analyze.app)
app.add_app("Forecast", forecast.app)

# The main app
app.run()