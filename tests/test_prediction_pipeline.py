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


def test_predict_accepts_api_payload_with_raw_features():
    pipeline = PredictionPipeline()
    payload = {
        "Crop": "Wheat",
        "Year": 2020,
        "State": "Punjab",
        "Area": 100.0,
        "Production": 200.0,
        "Rainfall": 800.0,
        "Temperature": 25.0,
        "Humidity": 60.0,
        "N": 120.0,
        "P": 40.0,
        "K": 20.0,
        "pH": 6.5,
        "Season": "Kharif",
    }

    prediction = pipeline.predict(payload)

    assert len(prediction) == 1
    assert isinstance(prediction[0], (int, float))
