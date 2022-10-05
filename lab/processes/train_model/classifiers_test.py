"""
Integration test for classifiers
"""

import configparser
import os
import shutil
from pathlib import Path

import pytest

from lib.testing import get_mlflow_double
from processes.preprocess_data.process_house_data import process_house_data
from processes.train_model.classifiers import classifiers_hyperparam_search

test_config = configparser.ConfigParser()
test_config.read("lab/processes/config_test.ini")


@pytest.fixture(name="temp_data_dir")
def fixture_temporary_data(dir_temp="temp"):
    """
    Creates a directory containing temporary data for the duration of test execution,
    cleaning up the created temporary directory afterwards

    Keyword Arguments:
        dir_temp {str} -- name or path of temporary data directory (default: {"temp"})

    Yields:
        {Generator[str]}
    """
    # Setup:
    # Create temp directory
    Path(dir_temp).mkdir(exist_ok=True)
    # Create the dataset for testing
    # IMPROVE: Load a small subset for testing instead of full dataset
    test_config["data"]["dir_processed"] = dir_temp
    process_house_data(config=test_config)

    # Pass to test
    yield dir_temp

    # Teardown: remove temp directory
    shutil.rmtree(dir_temp)


@pytest.mark.integration
def test_classifiers_hyperparam_search(temp_data_dir):
    """
    Happy-path integration test for the classifiers_hyperparams_search using a single combination of Random Forest
    hyperparameters for simplicity and speed

    Arguments:
        temp_data_dir {str} -- Path of temporary data directory required by the test,
            provided by a test fixture that also creates and destroys said directory
    """
    # Arrange
    test_config["data"]["dir_processed"] = temp_data_dir
    test_config["artifacts"]["temporal_folder"] = str(Path(temp_data_dir) / test_config["artifacts"]["temporal_folder"])
    mlflow_mock = get_mlflow_double()
    rf_params = dict(
        n_estimators=[20],
        max_depth=[4],
        max_features=[0.4],
        min_samples_split=[2],
        class_weight=["balanced"],
        random_state=[0],
    )

    # Call function under test
    classifiers_hyperparam_search(
        mlflow=mlflow_mock, config=test_config, mlflow_url="", train_params=rf_params, mlflow_tags={}
    )

    # Assert
    artifacts_created = os.listdir(test_config["artifacts"]["temporal_folder"])
    filenames_expected = [test_config["outputs"]["fname_model"], test_config["outputs"]["fname_conf_matrix"]]
    for fname in filenames_expected:
        assert fname in artifacts_created
