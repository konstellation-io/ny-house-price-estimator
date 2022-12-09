"""
Main code for the preprocess_data node
"""

import os

from lib.config import load_config
from processes.preprocess_data.process_house_data import process_house_data

PATH_CONFIG = os.getenv("PATH_CONFIG", "")

if __name__ == "__main__":

    config = load_config(PATH_CONFIG)
    process_house_data(config=config)
