from configparser import ConfigParser

import mlflow
from mlflow.tracking import MlflowClient


def download_best_model(config: ConfigParser, mlflow_url: str, metric: str) -> None:
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
        max_results=log_top,
        order_by=["metrics.test_rmse ASC"]
    )[0]

    # register the best model
    mlflow.download_artifact(f"runs:/{best_run.info.run_id}/model.joblib",)
