"""
The logic for the data preprocessing node
"""

from configparser import ConfigParser
from pathlib import Path

import pandas as pd
from lib.data_processing import preprocess_amenities_column, preprocess_target_variable
from processes.preprocess_data.mappings import MAP_NEIGHB, MAP_ROOM_TYPE


def process_house_data(config: ConfigParser) -> None:
    """
    Loads raw house price data as input (from path defined in config)
    and saves processed house price data (to path defined in config)

    Arguments:
        config {ConfigParser} -- Required section:
            "data": contains keys "dir_raw", "dir_processed", "fname_raw" and "fname_processed"
    """

    # Unpack config
    dir_raw = Path(config["data"]["dir_raw"])
    dir_processed = Path(config["data"]["dir_processed"])
    fpath_raw_data = dir_raw / config["data"]["fname_raw"]
    fpath_processed_data = dir_processed / config["data"]["fname_processed"]

    # Read data from Minio
    df_raw = pd.read_csv(fpath_raw_data)

    # Subset on columns of choice  IMPROVE: Import from a config file
    columns = [
        "neighbourhood_group_cleansed",
        "room_type",
        "latitude",
        "longitude",
        "accommodates",
        "bathrooms",
        "bedrooms",
        "beds",
        "amenities",
        "price",
    ]
    df = df_raw[columns].copy()
    df.rename(columns={"neighbourhood_group_cleansed": "neighbourhood"},
              inplace=True)

    # Preprocess the target variable
    df = preprocess_target_variable(df)

    # Create amenities features
    df = preprocess_amenities_column(df)

    # Map categorical features
    df["neighbourhood"] = df["neighbourhood"].map(MAP_NEIGHB)
    df["room_type"] = df["room_type"].map(MAP_ROOM_TYPE)

    # Save to Minio
    df.to_csv(fpath_processed_data)
