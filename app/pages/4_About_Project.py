import streamlit as st

st.set_page_config(page_title="About Project", layout="wide")
st.title("ℹ️ About the Project")

st.markdown("""
## Project Overview
This project predicts crop yield using historical agricultural data and environmental attributes.

## Problem Statement
Farmers and agricultural decision-makers need data-driven insights to estimate yield and plan resource allocation.

## Technologies Used
- Python
- FastAPI
- Streamlit
- SQLite
- scikit-learn
- pandas
- plotly

## Folder Structure
- app/: Streamlit frontend
- api/: FastAPI backend
- database/: SQLite storage
- src/: Machine learning components
- reports/: project reports and figures

## Links
- GitHub: https://github.com/pawanbhardwaj1610
- LinkedIn: https://www.linkedin.com/in/pawanbhardwaj1610/

## Future Scope
- Add user authentication
- Deploy on cloud infrastructure
- Support PostgreSQL and dashboards
- Add more crop models and forecasting features
""")
