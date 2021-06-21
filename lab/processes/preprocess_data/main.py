import configparser
import os
from pathlib import Path

from processes.preprocess_data.process_house_data import process_house_data

PATH_CONFIG = os.getenv("PATH_CONFIG")
config = configparser.ConfigParser()
config.read(str(PATH_CONFIG))

MLFLOW_URL = os.getenv("MLFLOW_URL")


if __name__ == "__main__":

    try:
        process_house_data(config=config)
    except KeyError as e:
        print(f"Path config: {Path(PATH_CONFIG)}")
        print(f"Contents: {os.listdir(Path(PATH_CONFIG).parent)}")
        print(f"Config sections:\n {config.sections()}")
        raise e
