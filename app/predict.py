import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import pandas as pd
from src import PredictionPipeline
from src.logger import logging
from artifacts.manager import save_predictions


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run prediction using the trained Smart Crop Yield model."
    )
    parser.add_argument(
        "--input-csv",
        default="data/processed/feature_engineered_dataset.csv",
        help="Input CSV file containing features for prediction.",
    )
    parser.add_argument(
        "--output-csv",
        default="artifacts/predictions.csv",
        help="Output CSV file to write predictions.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input_csv)
    output_path = Path(args.output_csv)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pipeline = PredictionPipeline()
    input_df = pd.read_csv(input_path)
    predictions = pipeline.predict(input_df)

    results_path = save_predictions(predictions, output_path, input_df)
    logging.info(f"Predictions saved to {results_path}")
    print(f"Predictions completed. Output saved to: {results_path}")


if __name__ == "__main__":
    main()
