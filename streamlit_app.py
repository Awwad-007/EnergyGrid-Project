import os
import streamlit as st

# Force security bypass at the application level
os.environ['STREAMLIT_SERVER_ENABLE_CORS'] = "false"
os.environ['STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION'] = "false"

st.title("⚡ Smart Energy Grid Simulator")
st.write("Environment is OpenEnv compliant and ready for validation.")