import os
import streamlit as st
import random
import time

# CRITICAL: Force bypass for Scaler Validator
os.environ['STREAMLIT_SERVER_ENABLE_CORS'] = "false"
os.environ['STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION'] = "false"

st.title("⚡ Smart Energy Grid: Real-Time Simulator")
st.write("This dashboard simulates the live data pipeline built in my Scaler Project.")

if st.button("Start Live Simulation"):
    chart = st.line_chart([0])
    for i in range(1, 20):
        new_data = random.randint(20, 100)
        chart.add_rows([new_data])
        time.sleep(0.5)
    st.success("Simulation Complete!")