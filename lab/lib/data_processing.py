"""
Reuasable functions for data processing, used by analysis notebooks as well as process code
"""

import numpy as np
import pandas as pd
from pandas import DataFrame


def preprocess_target_variable(df: DataFrame) -> DataFrame:
    """
    Converts the target variable column from string to numeric ('$100.00' -> 100)
    and creates price categories corresponding to low/mid/high/luxury properties.
    """
    df["price"] = df["price"].str.extract(r"(\d+).")
    df["price"] = df["price"].astype(int)
    df["category"] = pd.cut(
        df["price"], bins=[10, 90, 180, 400, np.inf], labels=[0, 1, 2, 3]
    )
    return df


def preprocess_amenities_column(df: DataFrame) -> DataFrame:
    """
    Given a text column 'amenities' containing amenity-specific substrings
    ('Heating', 'TV', 'Internet', 'Wifi' etc.), extracts the individual amenities
    as one-hot encoded features.
    """
    df["TV"] = df["amenities"].str.contains("TV")
    df["TV"] = df["TV"].astype(int)
    df["Internet"] = df["amenities"].str.contains("Internet")
    df["Internet"] = df["Internet"].astype(int)
    df["Elevator"] = df["amenities"].str.contains("Elevator")
    df["Elevator"] = df["Elevator"].astype(int)

    df.drop("amenities", axis=1, inplace=True)

    return df
