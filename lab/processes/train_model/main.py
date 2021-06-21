import os
from pathlib import Path

import joblib
import mlflow
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score
from sklearn.model_selection import ParameterGrid, train_test_split

MINIO_DATA_FOLDER = os.getenv("MINIO_DATA_FOLDER")

DIR_DATA_PROCESSED = Path(MINIO_DATA_FOLDER) / "processed"
FILEPATH_DATA = DIR_DATA_PROCESSED / "listings_processed.csv"

DIR_MODEL = Path(MINIO_DATA_FOLDER).parent / "models"
DIR_TEMP = Path("temp")  # Temporary location to save results before logging to MlFlow
FILEPATH_MODEL = DIR_MODEL / "simple_classifier.joblib"

MLFLOW_URL = os.getenv("MLFLOW_URL")
MLFLOW_EXPERIMENT = "ny-price-estimator"
MLFLOW_RUN_NAME = "train-simple-model"

RF_PARAMS = dict(
    n_estimators=[100, 200, 400],
    max_depth=[4, 6, 8, 12, 16],
    max_features=[0.4, 0.6, 0.8],
    min_samples_split=[2, 4],
    class_weight=["balanced"],
    random_state=[0],
)

INCLUDE_AMENITIES = True


def plot_confusion_matrix(
    y_pred: np.ndarray,
    y_true: np.ndarray,
    filepath: str,
    classes: list = [0, 1, 2, 3],
    labels: list = ["low", "mid", "high", "lux"],
) -> None:
    """
    Given arrays for predictions (y_pred) and true values (y_true) of a binary variable, plots a confusion matrix for the classes
    with their provided labels and saves it to the location specified in filepath.
    """
    c = confusion_matrix(y_true, y_pred)
    c = c / c.sum(axis=1).reshape(len(classes), 1)

    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(c, annot=True, cmap="BuGn", square=True, fmt=".2f", annot_kws={"size": 10}, cbar=False)
    plt.xlabel("Predicted", fontsize=16)
    plt.ylabel("Real", fontsize=16)
    plt.xticks(ticks=np.arange(0.5, len(classes)), labels=labels, rotation=0, fontsize=12)
    plt.yticks(ticks=np.arange(0.5, len(classes)), labels=labels, rotation=0, fontsize=12)

    plt.savefig(filepath)
    plt.close()


def main():
    """
    The main function of the script for training a simple classifier.
    - Loads processed data
    - Trains a simple Random Forest classifier
    - Evaluates the model on the test set
    - Logs the training hyperparameters, the trained model and metrics to MLflow
    """
    os.mkdir(DIR_TEMP)

    mlflow.set_tracking_uri(MLFLOW_URL)
    mlflow.set_experiment(MLFLOW_EXPERIMENT)

    with mlflow.start_run(run_name=MLFLOW_RUN_NAME):

        # Read input data
        df = pd.read_csv(FILEPATH_DATA, index_col=0).dropna(axis=0)

        # Set up training and testing data
        feature_names = ["neighbourhood", "room_type", "accommodates", "bathrooms", "bedrooms"]
        amenities = ["TV", "Internet", "Air_conditioning", "Kitchen", "Heating", "Wifi", "Elevator", "Breakfast"]

        if INCLUDE_AMENITIES:
            cols = feature_names + amenities
        else:
            cols = feature_names

        X = df[cols]
        y = df["category"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=1)

        # Iterate through hyperparameter space:
        for params in ParameterGrid(RF_PARAMS):
            with mlflow.start_run(run_name=MLFLOW_RUN_NAME, nested=True):

                # Train model
                clf = RandomForestClassifier(**params, n_jobs=4)
                clf.fit(X_train, y_train)

                # Save model
                joblib.dump(clf, FILEPATH_MODEL)

                # Evaluate the model
                y_pred = clf.predict(X_test)
                y_proba = clf.predict_proba(X_test)

                metrics = dict()
                metrics["accuracy"] = accuracy_score(y_test, y_pred)
                metrics["roc_auc"] = roc_auc_score(y_test, y_proba, multi_class="ovr")

                plot_confusion_matrix(y_pred=y_pred, y_true=y_test, filepath=str(DIR_TEMP / "confusion_matrix.png"))

                # Log to MLflow
                mlflow.log_params(params)
                mlflow.log_param("amenities", INCLUDE_AMENITIES)
                mlflow.log_metrics(metrics)
                mlflow.log_artifact(str(FILEPATH_MODEL))
                mlflow.log_artifacts(str(DIR_TEMP))


if __name__ == "__main__":

    main()
