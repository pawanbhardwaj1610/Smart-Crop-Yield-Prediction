import os
import sys
from typing import Any

import pandas as pd

from src.config import MODEL_PATH
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object


class PredictionPipeline:
    def __init__(self, model_path: str = MODEL_PATH):
        self.model_path = model_path
        self.model = self._load_model()

    def _load_model(self) -> Any:
        try:
            if not os.path.exists(self.model_path):
                raise FileNotFoundError(f"Model file not found: {self.model_path}")

            model = load_object(self.model_path)
            logging.info(f"Loaded model from {self.model_path}")
            return model
        except Exception as e:
            raise CustomException(e, sys) from e

    def predict_data(self, data: Any) -> Any:
        try:
            if isinstance(data, dict):
                data = pd.DataFrame([data])
            elif isinstance(data, list):
                data = pd.DataFrame(data)

            if not isinstance(data, pd.DataFrame):
                raise TypeError("Input data must be a pandas DataFrame, dict, or list")

            if "Yield" in data.columns:
                data = data.drop(columns=["Yield"])

            expected_columns = [
                "Crop",
                "Year",
                "Season",
                "State",
                "Area",
                "Production",
                "Annual_Rainfall",
                "Fertilizer",
                "Pesticide",
                "avg_temp_c",
                "total_rainfall_mm",
                "avg_humidity_percent",
                "N",
                "P",
                "K",
                "pH",
                "Production_per_area",
                "Rainfall_per_temperature",
            ]

            missing = [col for col in expected_columns if col not in data.columns]
            if missing:
                raise ValueError(f"Missing required columns for prediction: {missing}")

            extra = [col for col in data.columns if col not in expected_columns]
            if extra:
                logging.warning(f"Ignoring extra columns for prediction: {extra}")

            data = data[expected_columns]
            prediction = self.model.predict(data)
            logging.info(f"Made predictions for {len(data)} samples")
            return prediction
        except Exception as e:
            raise CustomException(e, sys) from e

    def predict(self, data: Any) -> Any:
        return self.predict_data(data)

    def predict_from_csv(self, csv_path: str) -> Any:
        try:
            if not os.path.exists(csv_path):
                raise FileNotFoundError(f"Prediction file not found: {csv_path}")

            data = pd.read_csv(csv_path)
            return self.predict_data(data)
        except Exception as e:
            raise CustomException(e, sys) from e
    
    
    
    
    
    