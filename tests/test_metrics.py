import numpy as np
import pandas as pd
import pytest


from fattails.metrics import mad, get_survival_probability

@pytest.fixture
def survival_data_examples():
    """Example input and output to test get_survival_probability"""
    two_equal_values = {}
    two_equal_values['input'] = [2,2,3]
    two_equal_values['output'] = [0.75, 0.5, 0.25]

    negative_and_positive = {}
    negative_and_positive['input'] = [-1,-0.3,7]
    negative_and_positive['output'] = [0.75, 0.5, 0.25]

    not_monotonic = {}
    not_monotonic['input'] = [2,3,2]
    not_monotonic['output'] = [0.75, 0.25, 0.5]

    examples = [two_equal_values, not_monotonic, negative_and_positive]

    return examples

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

class TestGetSurvivalProbability:

    def test_returns_expected_results(self, survival_data_examples):

        for example in survival_data_examples:
            data = example['input']
            expected = example['output']

            output = get_survival_probability(data)

            assert output.name == 'survival_probability'
            assert output.to_list() ==  example['output']