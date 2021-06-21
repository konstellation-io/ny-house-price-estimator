import configparser
import os

from processes.preprocess_data.process_house_data import process_house_data

PATH_CONFIG = os.getenv("PATH_CONFIG")
config = configparser.ConfigParser()
config.read(str(PATH_CONFIG))

MLFLOW_URL = os.getenv("MLFLOW_URL")


if __name__ == "__main__":

    process_house_data(config=config)
