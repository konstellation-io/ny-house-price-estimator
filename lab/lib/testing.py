"""
Reusable functions for testing
"""

from unittest.mock import MagicMock


def get_mlflow_double() -> MagicMock:
    """
    Creates a double (stub or mock) object to replace mlflow in local executions and during testing.

    When injected in place of the mlflow module, it provides dummies for the following calls:
    - mlflow.set_tracking_uri
    - mlflow.set_experiment
    - mlflow.start_run (as context manager)
    - mlflow.log_param
    - mlflow.log_params
    - mlflow.log_metric
    - mlflow.log_metrics
    - mlflow.log_artifacts

    Returns:
        [MagicMock] -- a double that can be used in place of mlflow in local and test executions
            as either stub or mock
    """
    mlflow_double = MagicMock()
    mlflow_double.set_tracking_uri.return_value = None
    mlflow_double.set_experiment.return_value = None
    mlflow_double.start_run.__enter__.return_value = None
    mlflow_double.log_artifacts.return_value = None
    mlflow_double.log_param.return_value = None
    mlflow_double.log_params.return_value = None
    mlflow_double.log_metric.return_value = None
    mlflow_double.log_metrics.return_value = None

    return mlflow_double
