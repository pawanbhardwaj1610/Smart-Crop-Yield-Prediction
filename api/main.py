import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from api.predict import PredictionService
from api.schemas import CropInput
from database.database import get_prediction_history

app = FastAPI(title="Smart Crop Yield Prediction API")
service = PredictionService()


@app.get("/")
def root() -> JSONResponse:
    return JSONResponse(content={"message": "Smart Crop Yield Prediction API is running"})


@app.get("/health")
def health() -> JSONResponse:
    return JSONResponse(content={"status": "ok"})


@app.post("/predict")
def predict(payload: CropInput) -> JSONResponse:
    payload_dict = payload.model_dump()
    prediction = service.predict(payload_dict)
    return JSONResponse(content={"Predicted Yield": round(prediction, 4)})


@app.get("/history")
def history() -> JSONResponse:
    rows = get_prediction_history()
    return JSONResponse(content={"history": rows})
