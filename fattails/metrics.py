import numpy as np

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