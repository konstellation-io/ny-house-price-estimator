"""
Main code for the download_model node
"""

import os

from download_model import save_best_model_in_runtimes_folder
from lib.config import load_config

PATH_CONFIG = os.getenv("PATH_CONFIG")
MLFLOW_URL = os.getenv("MLFLOW_URL")
# MLFLOW_TAGS = {"git_tag": os.getenv("DRONE_TAG")}

if __name__ == "__main__":

    config = load_config(PATH_CONFIG)
    model = save_best_model_in_runtimes_folder(config, MLFLOW_URL)
    print("Model: ", model)
    os.rename(model,
              f'{config["outputs"]["model_destination_path"]}/model.joblib')
