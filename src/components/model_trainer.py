import os
import sys
from typing import Any, Dict, Tuple

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from src.config import MODEL_PATH, N_ESTIMATORS, RANDOM_STATE, TEST_SIZE
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


class ModelTrainer:
    def __init__(self, model_path: str = MODEL_PATH):
        self.model_path = model_path

    def train(
        self,
        X: Any,
        y: Any,
        test_size: float = TEST_SIZE,
        random_state: int = RANDOM_STATE,
    ) -> Tuple[Any, Dict[str, float]]:
        try:
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )

            model = RandomForestRegressor(
                n_estimators=N_ESTIMATORS,
                random_state=random_state,
                n_jobs=-1,
            )
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            rmse = mean_squared_error(y_test, y_pred) ** 0.5
            metrics = {
                "mae": mean_absolute_error(y_test, y_pred),
                "rmse": rmse,
                "r2": r2_score(y_test, y_pred),
            }

            self._save_model(model)
            logging.info(
                f"Trained RandomForestRegressor; MAE={metrics['mae']:.4f}, RMSE={metrics['rmse']:.4f}, R2={metrics['r2']:.4f}"
            )
            return model, metrics
        except Exception as e:
            raise CustomException(e, sys) from e

    def _save_model(self, model: Any) -> None:
        try:
            directory = os.path.dirname(self.model_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)

            save_object(self.model_path, model)
            logging.info(f"Saved trained model to {self.model_path}")
        except Exception as e:
            raise CustomException(e, sys) from e
