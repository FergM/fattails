from copy import copy
import numpy as np
import pandas as pd

def mad(x):
    """Calculate Mean Absolute Deviation
    
    Not to be confused with commonly found 'Median' Absolute Deviation.
    
    Parameters
    ----------
    x : array_like
        Input array or object that can be converted to an array.
    
    Returns
    -------
    mad : scalar
          Mean Absolute Deviation of x
    """

    mean = np.mean(x)

    deviation = x-mean

    absolute_deviation = np.abs(deviation)

    mad = np.mean(absolute_deviation)

    return mad

def get_survival_probability(arr):
    """Calculate sample probability of X >= x, for each value in `arr`.

    Duplicate values are treated as ascending values based on
    their position in `arr`.

    Parameters
    ----------
    arr : array_like
        Numeric values on the real number line

    Returns
    -------
    survival_probability_sr : Pandas Series
    """
    #---------------------------------------------------
    # PREPARE
    ## Sort values from low to high. Keep track of original
    ## index and order.

    arr = copy(arr)     # Copy to avoid accidental mutation
    sr = pd.Series(arr) # Ensure we have a pandas series

    ## Keep a copy of the original index
    input_index = sr.index.copy()

    ## Create index of input order
    df = sr.reset_index(name='input_values') # Keeps the input index as a column
    df.index.name = 'input_order' # Name the new index

    ## Sort from low to high and reindex
    df = df.sort_values(by='input_values') # sort from low to high
    df = df.reset_index()
    df.index.name = 'sorted_order' # Name the new index

    #---------------------------------------------------
    # CALCULATE

    # Label relative positions
    gap_count = len(sr) + 1           # Think of the Posts and Fences analogy
    df['left_gap_count'] = df.index + 1                   # Count values <= x
    df['right_gap_count'] = gap_count - df.left_gap_count # Count values >= x

    # Get survival Probability
    df['survival_probability'] = df.right_gap_count / gap_count

    #---------------------------------------------------
    # FORMAT THE OUTPUT

    #Reset Input Order and Index
    df = df.sort_values(by='input_order') # sort from low to high
    df.index = input_index

    #Extract the output series
    survival_probability_sr = df.survival_probability

    return survival_probability_sr