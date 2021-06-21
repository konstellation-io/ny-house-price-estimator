import os
from pathlib import Path
import sys

import numpy as np
import pandas as pd
from pandas import DataFrame

DIR_REPO = Path(__file__).parent.parent.parent.parent
DIR_EXP = DIR_REPO / "experiments"
sys.path.append(str(DIR_EXP))

from src.data_processing import preprocess_target_variable, preprocess_amenities_column


MINIO_DATA_FOLDER = os.getenv("MINIO_DATA_FOLDER")
DIR_DATA_RAW = Path(MINIO_DATA_FOLDER) / "raw"
DIR_DATA_PROCESSED = Path(MINIO_DATA_FOLDER) / "processed"

FILEPATH_INPUT = DIR_DATA_RAW / "listings.csv"
FILEPATH_OUTPUT = DIR_DATA_PROCESSED / "listings_processed.csv"


# Categorical variable mapping dictionaries
MAP_ROOM_TYPE = {
    'Shared room': 1,
    'Private room': 2,
    'Entire home/apt': 3,
    'Hotel room': 4}

MAP_NEIGHB = {
    'Bronx': 1,
    'Queens': 2,
    'Staten Island': 3,
    'Brooklyn': 4,
    'Manhattan': 5}


def main():

    # Read data from Minio
    print(os.listdir(MINIO_DATA_FOLDER))
    df_raw = pd.read_csv(FILEPATH_INPUT)    
    
    # Subset on columns of choice
    COLUMNS = ['id', 'neighbourhood_group_cleansed', 'property_type', 'room_type', 'zipcode', 'latitude', 'longitude', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'bed_type', 'amenities', 'price']
    df = df_raw[COLUMNS].copy()
    df.rename(columns={'neighbourhood_group_cleansed': 'neighbourhood'}, inplace=True)

    # Preprocess the target variable
    df = preprocess_target_variable(df)

    # Create amenities features
    df = preprocess_amenities_column(df)

    # Map categorical features
    df['neighbourhood'] = df['neighbourhood'].map(MAP_NEIGHB)
    df['room_type'] = df['room_type'].map(MAP_ROOM_TYPE)

    # Save to Minio
    df.to_csv(FILEPATH_OUTPUT)


if __name__ == "__main__":
    
    main()