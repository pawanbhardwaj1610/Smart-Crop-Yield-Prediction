# Phase 13 - FastAPI Backend Report

## Objective
Expose the trained crop yield model through a REST API using FastAPI.

## What was implemented
- Added a FastAPI application in `api/main.py`
- Added request validation schema in `api/schemas.py`
- Added a prediction service wrapper in `api/predict.py`
- Added health and prediction endpoints

## Endpoints
- `GET /`
- `GET /health`
- `POST /predict`

## Run locally
```bash
uvicorn api.main:app --reload
```

## Swagger docs
Open `http://localhost:8000/docs`
