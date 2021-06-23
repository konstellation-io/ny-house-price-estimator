"""
Unit tests for lib/data_processing.py
"""

import unittest

import numpy as np
import pandas as pd
import pytest

from lib.data_processing import preprocess_target_variable


@pytest.mark.unittest
class TestDataCreation(unittest.TestCase):
    """
    Unit tests for data processing
    """

    def test_preprocess_target_variable(self):
        """
        Happy-path tests that the target variable (price category) is generated as expected
        """
        prices_as_string = ["$100.00", "$82.00", "$420.00"]
        prices_as_int = [100, 82, 420]
        categories = [1, 0, 3]

        df_input = pd.DataFrame(prices_as_string, columns=["price"])
        df_output = preprocess_target_variable(df_input)

        self.assertTrue(np.allclose(df_output["price"], prices_as_int))
        self.assertTrue(all(df_output["category"] == categories))


if __name__ == "__main__":

    unittest.main()
