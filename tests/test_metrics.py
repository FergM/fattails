import numpy as np
import pandas as pd
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

    def test_returns_expected_results(self, description, input_data, expected_output):

        output = get_survival_probability(input_data)

        assert output.name == 'survival_probability'
        assert output.to_list() ==  expected_output