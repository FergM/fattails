import fattails

# Quick access to selected methods in other modules
from fattails.metrics import mad


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
