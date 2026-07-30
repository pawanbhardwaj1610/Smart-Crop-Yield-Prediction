from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = ROOT_DIR / "data" / "processed" / "feature_engineered_dataset.csv"

MODEL_PATH = (
    ROOT_DIR
    / "notebooks"
    / "models"
    / "tuned_random_forest_model.pkl"
)

LOG_DIR = ROOT_DIR / "logs"
ARTIFACT_DIR = ROOT_DIR / "artifacts"

N_ESTIMATORS = 100
RANDOM_STATE = 42
TEST_SIZE = 0.2
