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

    sr = pd.Series(arr, name='input_data') # Convert input to pandas series
    sr = sr.sort_values()                  # Sort from low to high

    # Reset index
    df = sr.reset_index()   # Keeps the old index
    df = df.rename(columns={'index':'input_index'})

    # Label relative positions
    gap_count = len(sr) + 1           # Think of the Posts and Fences analogy
    df['left_gap_count'] = df.index+1                     # Count values <= x
    df['right_gap_count'] = gap_count - df.left_gap_count # Count values >= x

    # Get survival Probability
    df['survival_probability'] = df.right_gap_count / gap_count

    #===================================================
    #Format the Output

    #Reset original Order
    df = df.sort_values(by='input_index')

    #Extract the output series
    survival_probability_sr = df.survival_probability
    survival_probability_sr.reindex(df.input_index)

    return survival_probability_sr