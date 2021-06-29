"""
Integration test for process_house_data
"""

import configparser
import os
import shutil
from pathlib import Path

import pytest

from processes.preprocess_data.process_house_data import process_house_data

test_config = configparser.ConfigParser()
test_config.read("lab/processes/config_test.ini")


@pytest.fixture(name="temp_dir")
def fixture_temporary_directory(dir_temp="temp"):
    """
    Creates a directory to hold temporary data or artifacts for the duration of test execution,
    cleaning up the created temporary directory afterwards

    Keyword Arguments:
        dir_temp {str} -- name or path of temporary directory (default: {"temp"})

    Yields:
        {Generator[str]}
    """
    # Setup: create temp directory
    Path(dir_temp).mkdir(exist_ok=True)

    # Pass to test
    yield dir_temp

    # Teardown: remove temp directory
    shutil.rmtree(dir_temp)


@pytest.mark.integration
def test_process_house_data(temp_dir):
    """
    Integration test for process_house_data

    Arguments:
        temp_dir {str} -- temporary directory to hold test artifacts until test completion
            (use with fixture_temporary_directory)
    """
    test_config["data"]["dir_processed"] = temp_dir

    process_house_data(config=test_config)

    fname_expected = test_config["data"]["fname_processed"]
    files_in_temp_dir = os.listdir(temp_dir)

    assert fname_expected in files_in_temp_dir
