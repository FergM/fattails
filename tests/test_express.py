from fattails import express
from matplotlib.axes._subplots import SubplotBase
import pandas as pd
import pytest


class TestImports:
    """ Check that no imports are missing.
    """

    def test_mad_method_exists(self):
        """Check mad exists as expected in this namespace"""

        # Check that the attribute exists
        try:
            _ = express.mad
        except AttributeError:
            # Fail test if `express` doesn't have a `mad` attribute
            msg = 'The method called `mad` is missing from the express module.'
            pytest.fail(msg)


class TestPlotMSMoments:

    @pytest.mark.parametrize("description, input_data", [
                            ("list_data",  [1, 2, 3]),
                            ("series_data",  pd.Series([1, 2, 3])),
                            ])
    def testplot_MS_moments(self, description, input_data):

        axes = express.plot_MS_moments(input_data)
        first_axis = axes[0, 0]

        assert axes.shape == (2, 2)
        assert isinstance(first_axis, SubplotBase)
