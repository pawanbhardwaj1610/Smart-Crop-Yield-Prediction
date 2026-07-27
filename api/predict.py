from typing import Any

import pandas as pd

from database.database import insert_prediction
from src import PredictionPipeline


class PredictionService:
    def __init__(self) -> None:
        self.pipeline = PredictionPipeline()

    def predict(self, payload: dict[str, Any]) -> float:
        df = pd.DataFrame([payload])
        prediction = self.pipeline.predict(df)
        predicted_value = float(prediction[0])
        insert_prediction(
            state=str(payload.get("State", "Unknown")),
            crop=str(payload.get("Crop", "Unknown")),
            prediction=predicted_value,
        )
        return predicted_value
