import fattails

# Quick access to selected methods in other modules
from fattails.metrics import mad


def plot_tail(data, percent=33):
    """Plot the right tail
    
    Plotting is on a loglog scale.
    
    Parameters
        
    
    Returns
        None
        
    Returns
    -------
    ax : `matplotlib.axes.Axes`
        Returns the output from a pandas dataframe plot method.
    """
    
    df = data.to_frame('daily_return')
    
    # Calculate survival probability for each datapoint
    df['survival_probability'] = fattails.get_survival_probability(df.daily_return)
    df = df.sort_values(by='daily_return') # show sorted values

    # Plot the Right Tail
    selection = df.survival_probability < 0.33 # select top 33% of datapoints

    right_tail = df.loc[selection]

    ax = right_tail.plot(x='daily_return', y='survival_probability',
                    kind='scatter', loglog=True,
                    title='Gamestop Daily Returns',
                    xlabel='Daily Return', ylabel='Probability of >= X'
                    ); # xlabel argument requires pandas >= 1.2.0
    
    return ax


def plot_MS_moments(data):
    """Plot cumulative max/sum ratio of 1st to 4th moments

    Parameters
    ----------
    data : array-like
        Numeric values whose moments you want to calculate.
        Must be:
            * a valid input to `fattails.metrics.calculate_moments`.
            * 1-dimensional


    Returns
    -------
    subplots : np.array
        2*2 array of matplotlib subplots
    """

    # Calculate Moments
    moments_df = fattails.metrics.calculate_moments(data)

    # Calculate Max/Sum Ratio
    max_over_sum_df = moments_df.apply(fattails.metrics.max_over_sum)

    # Plot Max over Sum
    subplots = max_over_sum_df.plot(subplots=True, layout=[2, 2],
                                    figsize=[12.0, 8.0])

    return subplots
