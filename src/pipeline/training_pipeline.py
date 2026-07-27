from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging


def train_pipeline():
    ingestion = DataIngestion()
    df = ingestion.fetch_data()

    transformation = DataTransformation()
    X, y = transformation.split_features_and_target(df)

    trainer = ModelTrainer()
    _, metrics = trainer.train(X, y)

    logging.info(f"Training pipeline completed with metrics: {metrics}")
    return metrics


if __name__ == "__main__":
    metrics = train_pipeline()
    print(f"Training completed: {metrics}")
