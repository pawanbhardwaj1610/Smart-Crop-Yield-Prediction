import json
from pathlib import Path
from typing import Any

import pandas as pd
import requests
import streamlit as st

API_URL = "http://127.0.0.1:8001"


def _request_json(method: str, path: str, **kwargs: Any) -> Any:
    try:
        response = requests.request(method, f"{API_URL}{path}", timeout=10, **kwargs)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError as exc:
        raise RuntimeError("The FastAPI backend is not reachable. Start it with 'python -m uvicorn api.main:app --host 127.0.0.1 --port 8001'.") from exc
    except requests.exceptions.Timeout as exc:
        raise RuntimeError("The request to the FastAPI backend timed out.") from exc
    except requests.exceptions.RequestException as exc:
        raise RuntimeError(f"The FastAPI backend returned an error: {exc}") from exc


def load_metrics() -> dict[str, Any]:
    metrics_path = Path("artifacts/training_metrics.json")
    if not metrics_path.exists():
        return {}
    with metrics_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def get_history() -> pd.DataFrame:
    try:
        payload = _request_json("GET", "/history")
        history = payload.get("history", [])
        if not history:
            return pd.DataFrame(columns=["id", "date", "state", "crop", "prediction"])
        return pd.DataFrame(history)
    except Exception as exc:
        st.error(f"Unable to load prediction history: {exc}")
        return pd.DataFrame(columns=["id", "date", "state", "crop", "prediction"])


def make_prediction(payload: dict[str, Any]) -> dict[str, Any]:
    try:
        return _request_json("POST", "/predict", json=payload)
    except Exception as exc:
        raise RuntimeError(str(exc)) from exc
