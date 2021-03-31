import joblib
import os
from pathlib import Path

import mlflow
import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split, ParameterGrid


MINIO_DATA_FOLDER = os.getenv("MINIO_DATA_FOLDER")

DIR_DATA_PROCESSED = Path(MINIO_DATA_FOLDER) / "created"
FILEPATH_DATA = DIR_DATA_PROCESSED / "listings_processed.csv"

DIR_MODEL = Path(MINIO_DATA_FOLDER).parent / "models"
FILEPATH_MODEL = DIR_MODEL / "simple_classifier.joblib"

MLFLOW_URL = os.getenv("MLFLOW_URL")
MLFLOW_EXPERIMENT = "airbnb-specify-s3-mlflow-artifacts"
MLFLOW_RUN_NAME = "test-artifact-tracking"

PARAM_GRID = dict(
    n_estimators = [100, 200, 400], 
    max_depth = [4, 6, None],
    min_samples_split = [2, 4],
    class_weight=["balanced"], 
    random_state=[0]
)

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

        
        for params in ParameterGrid(PARAM_GRID):        
            with mlflow.start_run(run_name=MLFLOW_RUN_NAME, nested=True):
                
                # Train model
                clf = RandomForestClassifier(**params, n_jobs=4)
                clf.fit(X_train, y_train)

                # Save model
                joblib.dump(clf, FILEPATH_MODEL)

                # Evaluate
                y_pred = clf.predict(X_test)
                y_proba = clf.predict_proba(X_test)

                metrics = dict()
                metrics['accuracy'] = accuracy_score(y_test, y_pred)
                metrics['roc_auc'] = roc_auc_score(y_test, y_proba, multi_class='ovr')
                
                # Log to MLflow
                mlflow.log_params(params)
                mlflow.log_metrics(metrics)
                # mlflow.log_artifact(str(FILEPATH_MODEL))


if __name__ == "__main__":
    main()    