# 🌾 Smart Crop Yield Prediction & Agricultural Decision Support System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?style=for-the-badge&logo=fastapi)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge&logo=docker)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?style=for-the-badge)
![Render](https://img.shields.io/badge/Render-Deployed-success?style=for-the-badge)

</p>

---

# 📌 Project Overview

The **Smart Crop Yield Prediction & Agricultural Decision Support System** is a complete end-to-end Machine Learning project designed to predict agricultural crop yield using historical crop production, weather, and soil data.

This project follows the complete industry-standard Machine Learning lifecycle—from business understanding and data preprocessing to model deployment, API development, database integration, Docker containerization, Power BI dashboard creation, and cloud deployment.

The system helps farmers, researchers, and policymakers make data-driven decisions to improve agricultural productivity and resource planning.

---

# 🎯 Business Problem

Agriculture is heavily influenced by environmental and climatic factors. Farmers often struggle to estimate crop yield before harvesting, leading to inefficient planning and financial uncertainty.

This project aims to:

- Predict crop yield before harvest
- Support crop selection
- Improve fertilizer planning
- Analyze weather and soil impact
- Assist agricultural decision-making
- Reduce farming risks using data-driven insights

---

# 🚀 Key Features

### 📊 Data Analytics

- Data Cleaning
- Data Validation
- Data Integration
- Exploratory Data Analysis (EDA)
- Feature Engineering

### 🤖 Machine Learning

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor
- Hyperparameter Tuning
- Model Comparison
- Model Explainability

### 📈 Business Intelligence

Interactive Power BI Dashboard including:

- Executive Dashboard
- Crop Analysis
- Weather Analysis
- Soil Analysis
- Prediction Analysis

### 🌐 Backend Development

- FastAPI REST API
- Swagger Documentation
- Prediction API
- History API

### 💾 Database

- SQLite Integration
- Prediction History
- Automatic Record Storage

### 🐳 DevOps

- Docker Containerization
- Docker Compose
- Cloud Deployment (Render)

---

# 🏗️ Project Architecture

```text
                    User
                       │
                       ▼
             Streamlit Frontend
                       │
                       ▼
                FastAPI Backend
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
 Machine Learning Model       SQLite Database
          │                         │
          ▼                         ▼
 Random Forest Model       Prediction History
```

---

# 📂 Project Structure

```text
Smart-Crop-Yield-Prediction/
│
├── api/
├── app/
├── artifacts/
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── database/
├── deployment/
├── docs/
├── logs/
├── models/
├── notebooks/
├── powerbi/
├── reports/
├── src/
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🧠 Machine Learning Workflow

✅ Business Understanding

✅ Data Collection

✅ Data Understanding

✅ Data Cleaning

✅ Data Validation

✅ Dataset Merging

✅ Exploratory Data Analysis

✅ Feature Engineering

✅ Model Building

✅ Hyperparameter Tuning

✅ Model Explainability

✅ API Development

✅ Database Integration

✅ Dashboard Development

✅ Docker Containerization

✅ Cloud Deployment

---

# 📊 Power BI Dashboard

## Executive Dashboard

- Total Production
- Average Yield
- Total Crops
- Average Rainfall
- Yield by State

## Crop Analysis

- Top 10 Crops by Yield
- Crop Production
- Area vs Yield
- Seasonal Distribution

## Weather Analysis

- Rainfall vs Yield
- Temperature vs Yield
- Humidity vs Yield

## Soil Analysis

- Nitrogen Distribution
- Phosphorus Distribution
- Potassium Distribution
- Soil pH Analysis

---

# 🤖 Machine Learning Models

| Model | Status |
|--------|--------|
| Linear Regression | ✅ |
| Decision Tree | ✅ |
| Random Forest | ✅ Best Model |
| XGBoost | ✅ |

Evaluation Metrics

- R² Score
- RMSE
- MAE

---

# 🛠️ Technologies Used

### Programming

- Python

### Data Analysis

- Pandas
- NumPy
- Matplotlib

### Machine Learning

- Scikit-Learn
- XGBoost

### API

- FastAPI
- Uvicorn

### Database

- SQLite

### Dashboard

- Power BI

### Deployment

- Docker
- Render

---

# ⚙️ Installation

Clone Repository

```bash
git clone https://github.com/pawanbhardwaj1610/Smart-Crop-Yield-Prediction.git
```

Move into Project

```bash
cd Smart-Crop-Yield-Prediction
```

Install Requirements

```bash
pip install -r requirements.txt
```

Run API

```bash
uvicorn api.main:app --reload
```

Run Streamlit

```bash
streamlit run app/Home.py
```

---

# 🐳 Docker

Build

```bash
docker build -t smart-crop .
```

Run

```bash
docker run -p 8000:8000 smart-crop
```

---

# 🌐 Deployment

The application is deployed on Render.

API Documentation

```
https://YOUR_RENDER_URL/docs
```

---

# 📸 Project Screenshots

Add screenshots here:

```
images/

home.png

dashboard.png

api.png

prediction.png

soil.png

weather.png

crop.png
```

---

# 📈 Future Improvements

- Deep Learning Models
- Satellite Image Integration
- Real-time Weather API
- PostgreSQL Database
- AWS Deployment
- Mobile Application
- Multi-language Support

---

# 👨‍💻 Author

## Pawan Bhardwaj

B.Tech Computer Science Engineering (Data Science)

💼 LinkedIn:
https://linkedin.com/in/pawan-bhardwaj5

💻 GitHub:
https://github.com/pawanbhardwaj1610

---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.

It motivates me to build more industry-level Machine Learning and Data Science projects.

---
