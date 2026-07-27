import pandas as pd

from src.components.prediction import PredictionPipeline


def test_predict_data_rejects_missing_columns():
    pipeline = PredictionPipeline.__new__(PredictionPipeline)
    pipeline.model = None

    data = pd.DataFrame({"Crop": ["Wheat"]})

    try:
        pipeline.predict_data(data)
    except Exception as exc:
        assert "Missing required columns" in str(exc)
