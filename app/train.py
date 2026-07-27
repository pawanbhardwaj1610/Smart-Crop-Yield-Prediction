import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src import train_pipeline
from src.logger import logging
from artifacts.manager import save_metrics


def parse_args():
    parser = argparse.ArgumentParser(
        description="Train the Smart Crop Yield Prediction model and save training artifacts."
    )
    parser.add_argument(
        "--artifacts-dir",
        default="artifacts",
        help="Directory where training artifacts such as metrics will be saved.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    artifacts_dir = Path(args.artifacts_dir)
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    metrics = train_pipeline()
    metrics_path = save_metrics(metrics, artifacts_dir / "training_metrics.json")

    logging.info(f"Training metrics written to {metrics_path}")
    print(f"Training completed. Metrics saved to: {metrics_path}")


if __name__ == "__main__":
    main()
