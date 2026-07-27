from src.config import DATA_PATH
from src.components.prediction import PredictionPipeline
from src.logger import logging


def run_prediction(csv_path: str = DATA_PATH):
    pipeline = PredictionPipeline()
    predictions = pipeline.predict_from_csv(csv_path)
    logging.info(f"Prediction pipeline returned {len(predictions)} records")
    return predictions


if __name__ == "__main__":
    predictions = run_prediction()
    print(predictions)
