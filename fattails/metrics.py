from copy import copy

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def max_to_sum_plot(sample):
    """
    Parameters: 1D numpy array
   
    ----------------
    
    Output: Matplotlib object
    2x2 Maximum to Sum plot of the 4 moments: Mean, Variance, Skewness and Kurtosis
    
    -----------------
    """
    #error handling
    if len(sample)<10:
        raise Exception("Not enough data")
        
    if np.array(sample).shape != (len(sample),):
        raise Exception("Sample not 1D")
    
    R = np.zeros((4,len(sample)))
    for p in range(0,4):
        #1-4 moments
        for n in range(2,len(sample)):
            #loop through the sample for each p
            M = np.max(sample[:n]**(p+1)) # index starts from 0
            S = np.sum(sample[:n]**(p+1))
            R[p,n] = M/S
    #make plots
    fig,ax = plt.subplots(2,2)
    ax[0,0].plot(R[0,:])
    ax[0,0].set_title("1st Moment")
    ax[0,1].plot(R[1,:])
    ax[0,1].set_title("2nd Moment")
    ax[1,0].plot(R[2,:])
    ax[1,0].set_title("3rd Moment")
    ax[1,1].plot(R[3,:])
    ax[1,1].set_title("4th Moment")
    for ax in ax.flat:
        ax.set(xlabel='n', ylabel='max-to-sum')
        ax.label_outer()
    return ax


def mad(x):
    """Calculate Mean Absolute Deviation

    The average deviation from sample mean.
    Not to be confused with 'Median' Absolute Deviation.

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
    # ---------------------------------------------------
    # PREPARE
    # Sort values from low to high. Keep track of original
    # index and order.

    arr = copy(arr)      # Copy to avoid accidental mutation
    sr = pd.Series(arr)  # Ensure we have a pandas series

    # Keep a copy of the original index
    input_index = sr.index.copy()

    # Create index of input order
    df = sr.reset_index(name='input_values')  # Keeps the input index as a column
    df.index.name = 'input_order'  # Name the new index

    # Sort from low to high and reindex
    df = df.sort_values(by='input_values')  # sort from low to high
    df = df.reset_index()
    df.index.name = 'sorted_order'  # Name the new index

    # ---------------------------------------------------
    # CALCULATE

    # Label relative positions
    gap_count = len(sr) + 1           # Think of the Posts and Fences analogy
    df['left_gap_count'] = df.index + 1                    # Count values <= x
    df['right_gap_count'] = gap_count - df.left_gap_count  # Count values >= x

    # Get survival Probability
    df['survival_probability'] = df.right_gap_count / gap_count

    # ---------------------------------------------------
    # FORMAT THE OUTPUT

    # Reset Input Order and Index
    df = df.sort_values(by='input_order')  # sort from low to high
    df.index = input_index

    # Extract the output series
    survival_probability_sr = df.survival_probability

    return survival_probability_sr


def calculate_moments(data, moments=[1, 2, 3, 4], absolute_values=True):
    """Create dataframe with a column for each moment.

    Parameters
    ----------
    data : array-like
        Numeric values whose moments you want to calculate.
        Must be 1-dimensional

    moments : list-like of numbers
        Each moment has its own column in the output.

    absolute_values : , default True


    Returns
    -------
    moments_df : DataFrame
        Elementwise evaluation of x**p for each x in data and p in moments
        Number of rows = len(data)
        Number of columns = len(moments)
    """

    # FORMAT THE INPUT
    sr = pd.Series(data)
    if absolute_values:
        # Take absolute values (this matters for odd moments)
        sr = sr.abs()

    # CALCULATE MOMENTS
    df = pd.DataFrame()
    # Add columns with the moments for each datapoint
    for moment in moments:
        df[f'moment_{moment}'] = sr**moment

    return df


def max_over_sum(data, reset_index=False):
    """Calculate cumulative max over sum

    Parameters
    ----------
    data : array-like
        Numeric values whose moments you want to calculate.
        Must be 1-dimensional
    reset_index : bool
        Reset the index so it matches the cumulative count of your dataset size
        Selecting True will give you an output index starting at 1

    Returns
    -------
    max_over_sum : Series
        Series with cumulative maximum divided by cumulative sum.
        Cumulative sample size is assigned as the series' index.
    """
    sr = pd.Series(data)

    if reset_index:
        # Replace index with Cumulative Sample Size
        sr.reset_index(drop=True, inplace=True)
        sr.index += 1
        sr.index.rename('cumulative_sample_size', inplace=True)

    # Calculate
    max_over_sum = sr.cummax()/sr.cumsum()

    return max_over_sum
