import sys
import pandas as pd
from typing import Tuple

from src.exception import CustomException
from src.logger import logging


class DataTransformation:
    def __init__(self, target_column: str = "Yield"):
        self.target_column = target_column

    def split_features_and_target(self, df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
        try:
            if self.target_column not in df.columns:
                raise KeyError(f"Target column '{self.target_column}' not found in dataset")

            X = df.drop(columns=[self.target_column])
            y = df[self.target_column]
            logging.info(f"Transformed dataset into X shape {X.shape} and y shape {y.shape}")
            return X, y
        except Exception as e:
            raise CustomException(e, sys) from e
