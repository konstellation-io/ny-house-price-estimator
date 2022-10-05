import os
from configparser import ConfigParser

import mlflow
from mlflow.entities import ViewType
from mlflow.tracking import MlflowClient


def save_best_model_in_runtimes_folder(
    config: ConfigParser,
    mlflow_url: str,
) -> None:
    """
    Download the best model based on a metric

    Args:
        config (ConfigParser): Configuration
        mlflow_url (str): MLFlow URI
        metric (str): Best metric to choice
    """
    mlflow.set_tracking_uri(mlflow_url)
    client = MlflowClient()
    experiment = client.get_experiment_by_name(config["mlflow"]["mlflow_experiment"])

    best_run = client.search_runs(
        experiment_ids=experiment.experiment_id,
        run_view_type=ViewType.ACTIVE_ONLY,
        filter_string=config["mlflow"]["query"],
        max_results=int(config["mlflow"]["log_top"]),
        order_by=["metric.roc_auc ASC"],
    )[0]

    # register the best model
    return mlflow.artifacts.download_artifacts(
        f'runs:/{best_run.info.run_id}/{config["outputs"]["fname_model"]}',
        dst_path=config["outputs"]["model_destination_path"],
    )
