from fattails import metrics
import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal, assert_series_equal
import pytest


class TestMad:
    """Test the mean absolute deviation method"""

    def test_example(self):

        x = [0, 5, -5, 0, 0]

        mad_ = metrics.mad(x)

        expected_mad = 2
        assert mad_ == expected_mad

    def test_handles_mad_of_zero(self):

        x = [1, 1, 1, 1, 1]
        x = np.array(x)

        mad_ = metrics.mad(x)

        assert mad_ == 0


@pytest.mark.parametrize("description, input_data, expected_output", [
    ("duplicate_values",    [2,   2, 3], [0.75, 0.5,  0.25]),
    ("negative_values",   [-1, -0.3, 7], [0.75, 0.5,  0.25]),
    ("not_sorted_values",   [2,   3, 2], [0.75, 0.25,  0.5]),
])
class TestGetSurvivalProbability:

    def test_accepts_list_input(self, description,
                                input_data, expected_output):
        """List input data should be accepted even though
        output is always a pandas series."""

        output = metrics.get_survival_probability(input_data)

        assert output.name == 'survival_probability'
        assert output.to_list() == expected_output

    def test_accepts_series_input(self, description,
                                  input_data, expected_output):

        # Setup
        index = pd.date_range('2000-01-01', periods=len(input_data))
        # Input series
        input_name = 'name_placeholder'
        input_data = pd.Series(input_data, index, name=input_name)
        # Expected output
        expected_name = 'survival_probability'
        expected = pd.Series(expected_output, index, name=expected_name)

        output = metrics.get_survival_probability(input_data)

        assert_series_equal(output, expected)


class TestCalculateMoments:

    @pytest.mark.parametrize("description, input_data, expected_output", [
        ("simple_values",  [1, 2, 3], {'moment_1': [1, 2, 3],
                                       'moment_2': [1, 4, 9],
                                       'moment_3': [1, 8, 27]}),
        ("negative_values",  [-1, 2, -3], {'moment_1': [1, 2, 3],
                                           'moment_2': [1, 4, 9],
                                           'moment_3': [1, 8, 27]}),
    ])
    def test_gives_expected_output(self, description,
                                   input_data, expected_output):

        # Set up
        index = pd.date_range('2000-01-01', periods=3)
        input_data = pd.Series(input_data, index=index)
        expected_output = pd.DataFrame(expected_output, index=index)

        # Run
        moments_df = metrics.calculate_moments(input_data, moments=[1, 2, 3])

        # Check
        assert_frame_equal(moments_df, expected_output)


class TestMaxOverSum:

    @pytest.mark.parametrize("description, input_data, \
                              expected_output, reset_index", [
        ("simple_values",  [1, 2, 3], pd.Series([1, 2/3, 3/6]), False),
        ("reset_index",  [1, 2, 3], pd.Series([1, 2/3, 3/6]), True)
    ])
    def test_gives_expected_output(self, description,
                                   input_data, expected_output, reset_index):
        expected_output = pd.Series(expected_output)
        if reset_index:
            expected_output.index += 1
            expected_output.index.rename('cumulative_sample_size',
                                         inplace=True)

        max_over_sum = metrics.max_over_sum(input_data,
                                            reset_index=reset_index)

        assert_series_equal(max_over_sum, expected_output)
