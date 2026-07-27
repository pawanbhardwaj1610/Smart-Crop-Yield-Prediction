import json
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Model Insights", layout="wide")
st.title("📈 Model Insights")

metrics_path = Path("artifacts/training_metrics.json")
if metrics_path.exists():
    with metrics_path.open("r", encoding="utf-8") as handle:
        metrics = json.load(handle)
    st.subheader("Model Performance Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("R² Score", f"{metrics.get('r2', 0):.4f}")
    col2.metric("RMSE", f"{metrics.get('rmse', 0):.4f}")
    col3.metric("MAE", f"{metrics.get('mae', 0):.4f}")
else:
    st.warning("Training metrics file not found. Run the training workflow first.")

feature_importance_path = Path("reports/figures/feature_importance.png")
shap_path = Path("reports/figures/shap_summary.png")

if feature_importance_path.exists():
    st.subheader("Feature Importance")
    st.image(str(feature_importance_path), use_container_width=True)
else:
    st.info("Feature importance image not found. Generate the explainability reports first.")

if shap_path.exists():
    st.subheader("SHAP Summary Plot")
    st.image(str(shap_path), use_container_width=True)
else:
    st.info("SHAP summary image not found. Generate the explainability reports first.")
