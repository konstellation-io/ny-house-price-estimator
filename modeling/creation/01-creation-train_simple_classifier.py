import joblib
import os
from pathlib import Path

from matplotlib import pyplot as plt
import mlflow
from mlflow.exceptions import MlflowException
from mlflow.tracking import MlflowClient
import numpy as np
import pandas as pd
from pandas import DataFrame
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split, ParameterGrid


MINIO_DATA_FOLDER = os.getenv("MINIO_DATA_FOLDER")

DIR_DATA_PROCESSED = Path(MINIO_DATA_FOLDER) / "created"
FILEPATH_DATA = DIR_DATA_PROCESSED / "listings_processed.csv"

DIR_MODEL = Path(MINIO_DATA_FOLDER).parent / "models"
DIR_TEMP = Path("temp")  # Temporary location to save results before logging to MlFlow
FILEPATH_MODEL = DIR_MODEL / "simple_classifier.joblib"

MLFLOW_URL = os.getenv("MLFLOW_URL")
MLFLOW_EXPERIMENT = "price-estimator"  # os.getenv("BUCKET_NAME")    # "airbnb-price-estimation"  #airbnb-specify-s3-mlflow-artifacts
MLFLOW_RUN_NAME = "test-mlflow-exp-creation"

RF_PARAMS = dict(
    n_estimators = [100], #, 200, 400], 
    max_depth = [4], #, 6, 8, 12, 16],
    max_features = [0.4, 0.6, 0.8],
    min_samples_split = [2, 4],
    class_weight=["balanced"], 
    random_state=[0]
)

INCLUDE_AMENITIES = False
        

def plot_confusion_matrix(y_pred: np.ndarray, y_true: np.ndarray, filepath: str, classes: list = [0, 1, 2, 3], labels: list = ['low', 'mid', 'high', 'lux']) -> None:
    """ 
    Given arrays for predictions (y_pred) and true values (y_true) of a binary variable, plots a confusion matrix for the classes 
    with their provided labels and saves it to the location specified in filepath.
    """
    c = confusion_matrix(y_true, y_pred)
    c = c / c.sum(axis=1).reshape(len(classes), 1)

    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(c, annot=True, cmap='BuGn', square=True, fmt='.2f', annot_kws={'size': 10}, cbar=False)
    plt.xlabel('Predicted', fontsize=16)
    plt.ylabel('Real', fontsize=16)
    plt.xticks(ticks=np.arange(.5, len(classes)), labels=labels, rotation=0, fontsize=12)
    plt.yticks(ticks=np.arange(.5, len(classes)), labels=labels, rotation=0, fontsize=12)
    
    plt.savefig(filepath)


def main():
    """
    The main function of the script for training a simple classifier.
    """    
    os.mkdir(DIR_TEMP)
    
    # Temporary solution for an issue with mlflow artifacts buckets creation:
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
                
                plot_confusion_matrix(y_pred=y_pred, y_test=y_test, filepath=str(DIR_PATH / "confusion_matrix.png"))

                # Log to MLflow
                mlflow.log_params(params)
                mlflow.log_param("amenities", INCLUDE_AMENITIES)

                mlflow.log_metrics(metrics)
                mlflow.log_artifact(str(FILEPATH_MODEL))
                mlflow.log_artifacts(str(DIR_PATH))


if __name__ == "__main__":
    main()    