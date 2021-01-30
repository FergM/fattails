import numpy as np

from fattails.metrics import mad

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