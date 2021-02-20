from fattails import express
import pytest


class TestImports:
    """ Check that no imports are missing.
    """

    def test_mad_method(self):

        # Check that the attribute exists
        try:
            _ = express.mad
        except AttributeError:
            # Fail test if `express` doesn't have a `mad` attribute
            msg = 'The method called `mad` is missing from the express module.'
            pytest.fail(msg)
