# Phase 15 - Streamlit Web Application Report

## Project Information
- Project Name: Smart Crop Yield Prediction & Agricultural Decision Support System
- Phase: Phase 15 – Streamlit Web Application (Frontend)
- Author: Pawan Bhardwaj
- Date: 2026-07-27

## Objective
Build a professional Streamlit-based web application that allows users to interact with the trained crop yield model through a visual interface.

## Background
The project previously had a FastAPI backend and a machine learning pipeline. To improve user accessibility, a frontend interface was added so users could:
- enter crop and environmental information
- obtain predictions from the API
- inspect prediction history
- explore insights and project details

## Implementation
### Frontend structure
Created the required Streamlit app structure under app/:
- app/Home.py
- app/pages/1_Predict_Crop_Yield.py
- app/pages/2_Prediction_History.py
- app/pages/3_Model_Insights.py
- app/pages/4_About_Project.py
- app/utils.py
- app/assets/style.css

### Features implemented
- Home page with project description and architecture overview
- Prediction page with input form and API integration
- Prediction history page with filtering and CSV download
- Model insights page for metrics and visual outputs
- About page with project information and future scope

## Validation
The following checks were performed:
- Installed required packages: streamlit, requests, plotly, pandas
- Verified that the Streamlit app entrypoint files were created successfully
- Verified the API integration utility points to the FastAPI backend URL

## Challenges
- Ensuring the Streamlit app can communicate reliably with the FastAPI backend
- Handling cases where the backend is unavailable or the history endpoint is empty
- Making the interface readable while keeping the app lightweight

## Deliverables
- Streamlit frontend application files under app/
- CSS styling and page assets under app/assets/
- Report file saved at reports/15_Streamlit_Application_Report.md

## Conclusion
Phase 15 completes the frontend layer of the project by delivering a clean, interactive Streamlit web application that connects to the machine learning backend and presents prediction, history, insights, and project information in a user-friendly format.

## Next Phase
The next phase can focus on deployment, Dockerization, or cloud hosting of the full application.
