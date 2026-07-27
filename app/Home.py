from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Smart Crop Yield Prediction",
    page_icon="🌾",
    layout="wide",
)

with open(Path(__file__).parent / "assets" / "style.css", "r", encoding="utf-8") as handle:
    st.markdown(f"<style>{handle.read()}</style>", unsafe_allow_html=True)

st.title("🌾 Smart Crop Yield Prediction & Agricultural Decision Support System")
st.markdown("""
Welcome to the crop yield prediction application.

This app lets users:
- predict crop yield from environmental and agronomic inputs
- inspect past predictions stored in the database
- explore model insights and performance metrics
- learn about the project and future scope
""")

st.info("Use the sidebar to navigate between prediction, history, insights, and project information pages.")

st.subheader("System Architecture")
st.markdown("""
- User input is collected in the Streamlit frontend
- Requests are sent to the FastAPI backend
- The backend runs the trained model and stores the result in SQLite
- Prediction results and history are displayed back in the UI
""")

st.subheader("Project Authors")
st.markdown("- Author: Pawan Bhardwaj")
st.markdown("- Project: Smart Crop Yield Prediction & Agricultural Decision Support System")
