import os
from pathlib import Path

import numpy as np
import pandas as pd
from pandas import DataFrame


MINIO_DATA_FOLDER = os.getenv("MINIO_DATA_FOLDER")
DIR_DATA_RAW = Path(MINIO_DATA_FOLDER) / "base"
DIR_DATA_PROCESSED = Path(MINIO_DATA_FOLDER) / "created"

FILEPATH_INPUT = DIR_DATA_RAW / "listings.csv"
FILEPATH_OUTPUT = DIR_DATA_PROCESSED / "listings_processed.csv"


def preprocess_target_variable(df: DataFrame) -> DataFrame:
    """
    Converts the target variable column from string to numeric ('$100.00' -> 100)
    and creates price categories.
    """
    df['price'] = df['price'].str.extract(r"(\d+).")
    df['price'] = df['price'].astype(int)
    df['category'] = pd.cut(df['price'], bins=[10, 90, 180, 400, np.inf], labels=[0, 1, 2, 3])
    return df


def preprocess_amenities_column(df: DataFrame) -> DataFrame:
    """
    Given a text column 'amenities' containing amenity-specific substrings
    ('Heating', 'TV', 'Internet', 'Wifi' etc.), extracts the individual amenities
    as one-hot encoded features.
    """
    df['TV'] = df['amenities'].str.contains('TV')
    df['TV'] = df['TV'].astype(int)
    df['Internet'] = df['amenities'].str.contains('Internet')
    df['Internet'] = df['Internet'].astype(int)
    df['Air_conditioning'] = df['amenities'].str.contains('Air conditioning')
    df['Air_conditioning'] = df['Air_conditioning'].astype(int)
    df['Kitchen'] = df['amenities'].str.contains('Kitchen')
    df['Kitchen'] = df['Kitchen'].astype(int)
    df['Heating'] = df['amenities'].str.contains('Heating')
    df['Heating'] = df['Heating'].astype(int)
    df['Wifi'] = df['amenities'].str.contains('Wifi')
    df['Wifi'] = df['Wifi'].astype(int)
    df['Elevator'] = df['amenities'].str.contains('Elevator')
    df['Elevator'] = df['Elevator'].astype(int)
    df['Breakfast'] = df['amenities'].str.contains('Breakfast')
    df['Breakfast'] = df['Breakfast'].astype(int)

    df.drop('amenities', axis=1, inplace=True)
    
    return df


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

    # Save to Minio
    df.to_csv(FILEPATH_OUTPUT)


if __name__ == "__main__":
    
    main()