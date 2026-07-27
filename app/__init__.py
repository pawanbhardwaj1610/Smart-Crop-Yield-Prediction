"""Smart Crop Yield Prediction application package."""

from .train import main as train_main
from .predict import main as predict_main

__all__ = ["train_main", "predict_main"]
