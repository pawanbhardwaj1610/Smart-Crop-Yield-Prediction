# Phase 12 - Model Deployment and Artifacts Report

## Objective
Create a deployable and reproducible workflow for training, prediction, and artifact management so the machine learning project can be executed from scripts rather than notebooks alone.

## What was implemented
- Added reusable training and prediction entrypoints in the app package:
  - app/train.py
  - app/predict.py
- Built artifact management utilities in artifacts/manager.py to save:
  - training metrics as JSON
  - prediction outputs as CSV
- Structured the training and prediction flows into modular components under src/components and src/pipeline.
- Ensured the package can be executed from the project root with consistent imports and artifact paths.

## Key components
### Training workflow
- The training pipeline loads the processed dataset.
- It splits the dataset into features and target.
- It trains a RandomForestRegressor model.
- It saves model metrics to artifacts/training_metrics.json.

### Prediction workflow
- The prediction workflow loads the trained model from the configured model path.
- It accepts a CSV file or a DataFrame-like input.
- It writes predictions to artifacts/predictions.csv.

## Files involved
- app/train.py
- app/predict.py
- artifacts/manager.py
- src/components/model_trainer.py
- src/components/prediction.py
- src/pipeline/training_pipeline.py
- src/pipeline/prediction_pipeline.py

## Verification performed
The following commands were executed successfully:

```bash
python app/train.py
python app/predict.py --input-csv data/processed/feature_engineered_dataset.csv --output-csv artifacts/predictions.csv
```

Observed results:
- Training completed. Metrics saved to: artifacts/training_metrics.json
- Predictions completed. Output saved to: artifacts/predictions.csv

## Outputs generated
- artifacts/training_metrics.json
- artifacts/predictions.csv

## Business value
This phase makes the project production-ready from a workflow perspective by enabling:
- repeatable model training
- easy batch prediction execution
- straightforward artifact persistence for reporting and monitoring
- a cleaner handoff from experimentation to deployment

## Summary
Phase 12 establishes the operational layer of the crop yield prediction system by turning the notebook-based workflow into a script-driven, reusable ML application workflow.
