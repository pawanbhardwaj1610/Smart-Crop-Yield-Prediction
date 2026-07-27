import os
import sys
import pandas as pd

from src.config import DATA_PATH
from src.exception import CustomException
from src.logger import logging


class DataIngestion:
    def __init__(self, data_path: str = DATA_PATH):
        self.data_path = data_path

    def fetch_data(self) -> pd.DataFrame:
        try:
            if not os.path.exists(self.data_path):
                raise FileNotFoundError(f"Data file not found: {self.data_path}")

            df = pd.read_csv(self.data_path)
            logging.info(f"Loaded dataset from {self.data_path} with shape {df.shape}")
            return df
        except Exception as e:
            raise CustomException(e, sys) from e
