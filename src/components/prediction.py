import os
import sys
from typing import Any

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

from src.config import MODEL_PATH, ROOT_DIR
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object


class PredictionPipeline:
    EXPECTED_COLUMNS = [
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

    def __init__(self, model_path: str = MODEL_PATH):
        self.model_path = model_path
        self.model = self._load_model()
        self.reference_data = self._load_reference_data()
        self.categorical_encoders = self._fit_label_encoders()
        self.default_values = self._build_default_values()

    def _load_model(self) -> Any:
        try:
            if not os.path.exists(self.model_path):
                raise FileNotFoundError(f"Model file not found: {self.model_path}")

            model = load_object(self.model_path)
            logging.info(f"Loaded model from {self.model_path}")
            return model
        except Exception as e:
            raise CustomException(e, sys) from e

    def _load_reference_data(self) -> pd.DataFrame | None:
        try:
            reference_paths = [
                ROOT_DIR / "data" / "processed" / "final_df.csv",
                ROOT_DIR / "data" / "processed" / "feature_engineered_dataset.csv",
            ]
            for path in reference_paths:
                if os.path.exists(path):
                    data = pd.read_csv(path)
                    logging.info(f"Loaded reference training data from {path}")
                    return data
            return None
        except Exception as e:
            logging.warning(f"Unable to load reference data: {e}")
            return None

    def _fit_label_encoders(self) -> dict[str, LabelEncoder]:
        encoders: dict[str, LabelEncoder] = {}
        if self.reference_data is None:
            return encoders

        for column in ["Crop", "Season", "State"]:
            if column in self.reference_data.columns:
                encoder = LabelEncoder()
                encoder.fit(self.reference_data[column].astype(str))
                encoders[column] = encoder
        return encoders

    def _build_default_values(self) -> dict[str, float]:
        defaults: dict[str, float] = {
            "Year": 2020.0,
            "Area": 1000.0,
            "Production": 1000.0,
            "Annual_Rainfall": 1000.0,
            "Fertilizer": 1000.0,
            "Pesticide": 1000.0,
            "avg_temp_c": 25.0,
            "total_rainfall_mm": 1000.0,
            "avg_humidity_percent": 60.0,
            "N": 100.0,
            "P": 40.0,
            "K": 20.0,
            "pH": 6.5,
            "Production_per_area": 1.0,
            "Rainfall_per_temperature": 40.0,
        }

        if self.reference_data is not None:
            for column in ["Annual_Rainfall", "Fertilizer", "Pesticide", "avg_temp_c", "total_rainfall_mm", "avg_humidity_percent"]:
                if column in self.reference_data.columns:
                    defaults[column] = float(self.reference_data[column].median())

        return defaults

    def _coerce_numeric(self, series: pd.Series, default: float) -> pd.Series:
        converted = pd.to_numeric(series, errors="coerce")
        return converted.fillna(default)

    def _encode_categorical(self, series: pd.Series, column: str) -> pd.Series:
        if column not in self.categorical_encoders:
            return series

        if pd.api.types.is_numeric_dtype(series):
            return series.astype(float)

        encoder = self.categorical_encoders[column]
        values = series.astype(str)
        known_values = values.isin(encoder.classes_)
        if not known_values.all():
            fallback_value = encoder.classes_[0]
            values = values.where(known_values, fallback_value)
        return pd.Series(encoder.transform(values), dtype=float)

    def _prepare_features(self, data: pd.DataFrame) -> pd.DataFrame:
        prepared = pd.DataFrame(index=data.index)
        prepared["Crop"] = data.get("Crop", pd.Series(["Unknown"] * len(data), index=data.index))
        prepared["Year"] = self._coerce_numeric(data.get("Year", pd.Series([self.default_values["Year"]] * len(data), index=data.index)), self.default_values["Year"])
        prepared["Season"] = data.get("Season", pd.Series(["Kharif"] * len(data), index=data.index))
        prepared["State"] = data.get("State", pd.Series(["Unknown"] * len(data), index=data.index))
        prepared["Area"] = self._coerce_numeric(data.get("Area", pd.Series([self.default_values["Area"]] * len(data), index=data.index)), self.default_values["Area"])
        prepared["Production"] = self._coerce_numeric(data.get("Production", pd.Series([self.default_values["Production"]] * len(data), index=data.index)), self.default_values["Production"])
        prepared["Annual_Rainfall"] = self._coerce_numeric(data.get("Annual_Rainfall", data.get("Rainfall", pd.Series([self.default_values["Annual_Rainfall"]] * len(data), index=data.index))), self.default_values["Annual_Rainfall"])
        prepared["Fertilizer"] = self._coerce_numeric(data.get("Fertilizer", pd.Series([self.default_values["Fertilizer"]] * len(data), index=data.index)), self.default_values["Fertilizer"])
        prepared["Pesticide"] = self._coerce_numeric(data.get("Pesticide", pd.Series([self.default_values["Pesticide"]] * len(data), index=data.index)), self.default_values["Pesticide"])
        prepared["avg_temp_c"] = self._coerce_numeric(data.get("avg_temp_c", data.get("Temperature", pd.Series([self.default_values["avg_temp_c"]] * len(data), index=data.index))), self.default_values["avg_temp_c"])
        prepared["total_rainfall_mm"] = self._coerce_numeric(data.get("total_rainfall_mm", data.get("Rainfall", pd.Series([self.default_values["total_rainfall_mm"]] * len(data), index=data.index))), self.default_values["total_rainfall_mm"])
        prepared["avg_humidity_percent"] = self._coerce_numeric(data.get("avg_humidity_percent", data.get("Humidity", pd.Series([self.default_values["avg_humidity_percent"]] * len(data), index=data.index))), self.default_values["avg_humidity_percent"])
        prepared["N"] = self._coerce_numeric(data.get("N", pd.Series([self.default_values["N"]] * len(data), index=data.index)), self.default_values["N"])
        prepared["P"] = self._coerce_numeric(data.get("P", pd.Series([self.default_values["P"]] * len(data), index=data.index)), self.default_values["P"])
        prepared["K"] = self._coerce_numeric(data.get("K", pd.Series([self.default_values["K"]] * len(data), index=data.index)), self.default_values["K"])
        prepared["pH"] = self._coerce_numeric(data.get("pH", pd.Series([self.default_values["pH"]] * len(data), index=data.index)), self.default_values["pH"])

        prepared["Crop"] = self._encode_categorical(prepared["Crop"], "Crop")
        prepared["Season"] = self._encode_categorical(prepared["Season"], "Season")
        prepared["State"] = self._encode_categorical(prepared["State"], "State")

        area = prepared["Area"].replace(0, np.nan)
        production = prepared["Production"]
        prepared["Production_per_area"] = (production / area).replace([np.inf, -np.inf], np.nan).fillna(self.default_values["Production_per_area"])

        rainfall = prepared["Annual_Rainfall"]
        temperature = prepared["avg_temp_c"].replace(0, np.nan)
        prepared["Rainfall_per_temperature"] = (rainfall / temperature).replace([np.inf, -np.inf], np.nan).fillna(self.default_values["Rainfall_per_temperature"])

        return prepared[self.EXPECTED_COLUMNS]

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

            if all(column in data.columns for column in self.EXPECTED_COLUMNS):
                feature_frame = data[self.EXPECTED_COLUMNS].copy()
            else:
                feature_frame = self._prepare_features(data)

            feature_frame = feature_frame.astype(float)
            prediction = self.model.predict(feature_frame)
            logging.info(f"Made predictions for {len(feature_frame)} samples")
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
    