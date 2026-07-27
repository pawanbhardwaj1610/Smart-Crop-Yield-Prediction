# Phase 14 - Database Integration Report

## Objective
Add persistent storage for prediction requests so the crop yield API can retain a history of predictions for later analysis.

## Database choice
- SQLite was implemented first for simplicity and local development.
- The design is compatible with a future migration to PostgreSQL.

## What was implemented
- Created a database layer in database/database.py
- Added a SQLite database file at database/database.db
- Implemented a prediction_history table with the following columns:
  - id
  - date
  - state
  - crop
  - prediction
- Wired the prediction API to insert a record whenever a prediction is made.
- Added a GET /history endpoint to retrieve stored prediction history.

## Files added or updated
- database/database.py
- database/database.db
- api/predict.py
- api/main.py
- tests/test_database.py

## Verification
The following checks were run successfully:
- Unit test: python -m unittest -q tests.test_database
- Prediction request to the API completed successfully.
- GET /history returned stored rows from the database.

## Summary
Phase 14 completes the persistence layer for the Smart Crop Yield Prediction API by storing prediction history in SQLite and exposing it through a dedicated endpoint.
