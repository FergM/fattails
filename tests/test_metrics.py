import numpy as np
import pandas as pd
from pandas.testing import assert_series_equal
import pytest


from fattails.metrics import mad, get_survival_probability

class TestMad:
    """Test the mean absolute deviation method"""

    def test_example(self):

        x = [0,5,-5,0,0]

        mad_ = mad(x)

        expected_mad = 2
        assert mad_ == expected_mad

    def test_handles_mad_of_zero(self):

        x = [1,1,1,1,1]
        x = np.array(x)

        mad_ = mad(x)

        assert mad_ == 0

@pytest.mark.parametrize("description, input_data, expected_output", [
    ("duplicate_values",  [ 2,   2, 3], [0.75, 0.5,  0.25]),
    ("negative_values",   [-1,-0.3, 7], [0.75, 0.5,  0.25]),
    ("not_sorted_values", [ 2,   3, 2], [0.75, 0.25,  0.5]),
])
class TestGetSurvivalProbability:

    def test_accepts_list_input(self, description, input_data, expected_output):
        """List input data should be accepted even though output is always a pandas series."""

        output = get_survival_probability(input_data)

        assert output.name == 'survival_probability'
        assert output.to_list() ==  expected_output

    def test_accepts_series_input(self, description, input_data, expected_output):

        # Setup
        index = pd.date_range('2000-01-01', periods=len(input_data))
        # Input series
        input_name = 'name_placeholder'
        input_data = pd.Series(input_data, index, name=input_name)
        # Expected output
        expected_name = 'survival_probability'
        expected = pd.Series(expected_output, index, name=expected_name)

        output = get_survival_probability(input_data)

        assert_series_equal(output, expected)