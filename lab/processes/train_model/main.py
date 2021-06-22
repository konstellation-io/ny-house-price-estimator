import os

import mlflow

from lib.config import load_config
from processes.train_model.classifiers import classifiers_hyperparam_search

PATH_CONFIG = os.getenv("PATH_CONFIG")
MLFLOW_URL = os.getenv("MLFLOW_URL")
RF_PARAMS = dict(
    n_estimators=[100, 200, 400],
    max_depth=[4, 6, 8, 12, 16],
    max_features=[0.4, 0.6, 0.8],
    min_samples_split=[2, 4],
    class_weight=["balanced"],
    random_state=[0],
)


if __name__ == "__main__":

    config = load_config(PATH_CONFIG)
    classifiers_hyperparam_search(mlflow=mlflow, config=config, mlflow_url=MLFLOW_URL, train_params=RF_PARAMS)
