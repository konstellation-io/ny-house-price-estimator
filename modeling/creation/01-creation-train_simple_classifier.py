import joblib
import os
from pathlib import Path

import mlflow
from mlflow.exceptions import MlflowException
from mlflow.tracking import MlflowClient
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
MLFLOW_EXPERIMENT = "airbnb-price-estimator" # os.getenv("BUCKET_NAME")    # "airbnb-price-estimation"  #airbnb-specify-s3-mlflow-artifacts
MLFLOW_RUN_NAME = "test-mlflow-exp-creation"

RF_PARAMS = dict(
    n_estimators = [100], 
    max_depth = [8],  #4, 6, 8, 12, 16
    max_features = [0.4, 0.6, 0.8],
    min_samples_split = [2, 4],
    class_weight=["balanced"], 
    random_state=[0]
)

INCLUDE_AMENITIES = False
        

def main():
    """
    The main function of the script for training a simple classifier.
    """
    
    
    # Temporary code 
    client = mlflow.tracking.MlflowClient(tracking_uri=MLFLOW_URL)
    if not MLFLOW_EXPERIMENT in [exp.name for exp in client.list_experiments()]:
        client.create_experiment(MLFLOW_EXPERIMENT, artifact_location="s3://ny-price-estimator/mlflow-artifacts")

    mlflow.set_tracking_uri(MLFLOW_URL)
    mlflow.set_experiment(MLFLOW_EXPERIMENT)
    
    with mlflow.start_run(run_name=MLFLOW_RUN_NAME):
        
        # Read input data
        df = pd.read_csv(FILEPATH_DATA, index_col=0).dropna(axis=0)

        # Set up training and testing data
        feature_names = ['neighbourhood', 'room_type', 'accommodates', 'bathrooms', 'bedrooms']
        amenities = ['TV', 'Internet', 'Air_conditioning', 'Kitchen', 'Heating', 'Wifi', 'Elevator', 'Breakfast']

        if INCLUDE_AMENITIES:
            cols = feature_names + amenities
        else:
            cols = feature_names

        X = df[cols]
        y = df['category']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=1)
        
        # Iterate through hyperparameter space:
        for params in ParameterGrid(RF_PARAMS):        
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
                mlflow.log_param("amenities", INCLUDE_AMENITIES)

                mlflow.log_metrics(metrics)
                mlflow.log_artifact(str(FILEPATH_MODEL))


if __name__ == "__main__":
    main()    