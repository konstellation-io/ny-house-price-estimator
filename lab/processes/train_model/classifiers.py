"""
The logic for the model training node
"""

from configparser import ConfigParser
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import ParameterGrid, train_test_split

from lib.viz import plot_confusion_matrix


def classifiers_hyperparam_search(
    mlflow, config: ConfigParser, mlflow_url: str, train_params: dict, mlflow_tags: dict
) -> None:
    """
    Trains a series of RandomForest models iterating through all combinations of training parameters as defined in
    train_params, logging the hyperparams and the resulting model and metrics and model to mlflow.
    Uses processed data from location specified in config.

    Arguments:
        mlflow {module} -- the mlflow module (injected as dependency for mocking in integration tests)
        config {ConfigParser} -- required sections:
            "data": containing "dir_processed" and "fname_processed" (together defining the processed data path);
            "artifacts": containing "temporal_folder";
            "outputs": containing filenames for the outputs ("fname_model" and "fname_conf_matrix");
            "training": containing a boolean field "include_amenities";
            "mlflow": containg "mlflow_experiment";
        mlflow_url {str} -- the URL of the mlflow instance
        train_params {dict} -- A dictionary specifying the grid search hyperparameter values
            (all keys must be kwargs for for sklearn RandomForestClassifier)
        mlflow_tags {dict} -- A dictionary containing tags for the mlflow run (e.g. "git_tag")
    """
    # Unpack config
    dir_processed = Path(config["data"]["dir_processed"])
    fpath_processed_data = dir_processed / config["data"]["fname_processed"]
    dir_artifacts = Path(config["artifacts"]["temporal_folder"])
    fpath_model = str(dir_artifacts / config["outputs"]["fname_model"])
    fpath_conf_matrix = str(dir_artifacts / config["outputs"]["fname_conf_matrix"])
    include_amenities = bool(config["training"]["include_amenities"])
    mlflow_experiment = config["mlflow"]["mlflow_experiment"]

    # Set up
    dir_artifacts.mkdir(exist_ok=True)
    mlflow.set_tracking_uri(mlflow_url)
    mlflow.set_experiment(mlflow_experiment)

    with mlflow.start_run(run_name="hyperparam_search"):
        mlflow.set_tags(mlflow_tags)

        # Read input data
        df = pd.read_csv(fpath_processed_data, index_col=0).dropna(axis=0)

        # Set up training and testing data
        feature_names = [
            "neighbourhood",
            "room_type",
            "accommodates",
            "bathrooms",
            "bedrooms",
        ]
        amenities = [
            "TV",
            "Internet",
            "Elevator",
        ]

        if include_amenities:
            cols = feature_names + amenities
        else:
            cols = feature_names

        X = df[cols]
        y = df["category"]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.15, random_state=1
        )

        # Iterate through hyperparameter space:
        for params in ParameterGrid(train_params):
            with mlflow.start_run(run_name="train-simple-model", nested=True):
                mlflow.set_tags(mlflow_tags)
                # Train model
                clf = RandomForestClassifier(**params, n_jobs=4)
                clf.fit(X_train, y_train)

                # Save model
                joblib.dump(clf, fpath_model)

                # Evaluate the model
                y_pred = clf.predict(X_test)
                y_proba = clf.predict_proba(X_test)

                metrics = dict()
                metrics["accuracy"] = accuracy_score(y_test, y_pred)
                metrics["roc_auc"] = roc_auc_score(y_test, y_proba, multi_class="ovr")

                plot_confusion_matrix(
                    y_pred=y_pred, y_true=y_test, filepath=fpath_conf_matrix
                )

                # Log to MLflow
                mlflow.log_params(params)
                mlflow.log_param("amenities", include_amenities)
                mlflow.log_metrics(metrics)
                mlflow.log_artifact(str(fpath_model))
                mlflow.log_artifacts(str(dir_artifacts))
