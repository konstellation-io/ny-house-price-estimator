import joblib
import os
from pathlib import Path

import mlflow
import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix


MINIO_DATA_FOLDER = os.getenv("MINIO_DATA_FOLDER")

DIR_DATA_PROCESSED = Path(MINIO_DATA_FOLDER) / "created"
FILEPATH_DATA = DIR_DATA_PROCESSED / "listings_processed.csv"

DIR_MODEL = Path(MINIO_DATA_FOLDER).parent / "models"
FILEPATH_MODEL = DIR_MODEL / "simple_classifier.joblib"

MLFLOW_URL = "http://mlflow-server:5000"
MLFLOW_EXPERIMENT = "ny-price-estimation"
MLFLOW_RUN_NAME = "test-track-params"


def main():
    
    mlflow.set_tracking_uri(MLFLOW_URL)
    mlflow.set_experiment(MLFLOW_EXPERIMENT)
    
    with mlflow.start_run(run_name=MLFLOW_RUN_NAME):
        
        # Read input data
        df = pd.read_csv(FILEPATH_DATA, index_col=0).dropna(axis=0)

        # Set up training and testing data
        FEATURE_NAMES = ['neighbourhood', 'room_type', 'accommodates', 'bathrooms', 'bedrooms']
        X = df[FEATURE_NAMES]
        y = df['category']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=1)

        # Train model
        CLF_PARAMS = dict(n_estimators=120, random_state=0)

        clf = RandomForestClassifier(**CLF_PARAMS)
        clf.fit(X_train, y_train)

        # Save model
        joblib.dump(clf, FILEPATH_MODEL)
        
        # Log to MLflow
        mlflow.log_params(CLF_PARAMS)
        mlflow.log_artifact(FILEPATH_MODEL)


if __name__ == "__main__":
    main()    