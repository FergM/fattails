import unittest

import numpy as np

from fattails.metrics import mad

class TestMad(unittest.TestCase):
    """Test the mean absolute deviation method"""

    def test_mad_zero(self):

        x = [1,1,1,1,1]
        x = np.array(x)

        mad_ = mad(x)

        self.assertEqual(mad_, 0)

    def test_mad_example(self):

        x = [0,5,-5,0,0]

        mad_ = mad(x)
        
        expected_mad = 2
        self.assertEqual(mad_, expected_mad)

if __name__ == '__main__':
    unittest.main()