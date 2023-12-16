"""HIDDEN MOMENTS

2023-12-16 Workings About Hidden Moments. 
For more context see my notebook `2023-12 Hidden Moments.ipynb`
"""

import numpy as np
from scipy import integrate
from scipy.stats import norm

def gaussian_samples(n, mean=0, std_dev=1):
    """
    Generate a Gaussian random sample of size n.

    Parameters:
    - n (int): Size of the random sample.
    - mean (float): Mean of the Gaussian distribution (default is 0).
    - std_dev (float): Standard deviation of the Gaussian distribution (default is 1).

    Returns:
    - numpy.ndarray: Array containing the generated random sample.
    """
    sample = np.random.normal(loc=mean, scale=std_dev, size=n)

    return sample

def gaussian_hidden_moment(threshold, moment, mean=0, std_dev=1):
    """Calculate the hidden moment for a gaussian distribution.

    The hidden pth moment above a threshold k.

    Defined as the integral of (x^p)*pdf
    With integration limits of k to infinity.
    And a gaussian pdf.

    Parameters
    ----------
    threshold : float
        Threshold above which we define things to be hidden.
    moment : int >=0
        The moment of interest
        * 0th moment is hidden probability
        * 1st is hidden mean, 2nd is hidden variance ...
    
    Returns
    -------
    hidden_moment : float
        The hidden moment. 
        For p=0:
            This represents the amount of probability which lies above k,
            i.e. this is equivalent to the survival function.
    estimated_error
        Estimated error from the numerical integration.
        Determined by `numpy.integrate.quad`
    """

    # Create a normal distribution object
    normal_distribution = norm(loc=mean, scale=std_dev)

    # Define the function to be integrated: x^p * phi(x)
    def integrand(x, moment):
        return x**moment * normal_distribution.pdf(x)

    # Integrate the function from k to infinity
    hidden_moment, estimated_error = integrate.quad(integrand, threshold, np.inf, args=(moment,))

    return hidden_moment, estimated_error

def sample_gaussian_hidden_moment(n, moment):
    """Sample the gaussian and calculate the hidden moment.
    
    Parameters
    ----------
    n : int
        Size of the random sample
    moment : int >=0
        The moment of interest
        * 0th moment is hidden probability
        * 1st is hidden mean, 2nd is hidden variance ...
    """
    sample = gaussian_samples(n)
    sample_max = np.max(sample)

    hidden_moment, _ = gaussian_hidden_moment(threshold=sample_max, moment=0)

    return hidden_moment


def hidden_moment_samples(meta_n, hidden_moment_func, n, moment):
    """Make samples of the hidden moment

    Parameters
    ----------
    meta_n
        Hidden moment sample size.
        The number of times we sample the hidden moment (of size n)
    hidden_moment_func
        A function of
        * n - sample size
        * moment - the moment of interest
    n
        Sample size from the raw distribution.
        Used to calculate each individual hidden moment.
    moment : int >=0
        The moment of interest
        * 0th moment is hidden probability
        * 1st is hidden mean, 2nd is hidden variance ...
    """

    meta_sample = [hidden_moment_func(n, moment)
                             for _ in range(meta_n)]

    hidden_moment_samples = np.array(meta_sample)

    return hidden_moment_samples


if __name__ == "__main__":

    # Generate a sample of hidden moments
    hidden_moment_samples = hidden_moment_samples(
                                    meta_n=10, 
                                    hidden_moment_func=sample_gaussian_hidden_moment,
                                    n=10,
                                    moment=0)

    print(hidden_moment_samples)
