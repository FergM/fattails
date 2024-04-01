## Finds the most likely p, by maximising the entropy given k heads out of n tosses subject to that constraint of k being heads out of n tosses

from scipy.optimize import minimize
from scipy.special import comb
import numpy as np

# Define Shannon entropy for Binomial distribution
def shannon_entropy(p, n):
    p = p[0]  # Extract p from the array
    terms = [comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(n + 1)]
    entropy = -np.sum(term * np.log2(term) for term in terms if term > 0)  # Exclude zero terms
    return -entropy  # Minimize the negative entropy to maximize entropy

# Define constraint for the mean (x/n)
def constraint_mean(p, n, x):
    return n * p[0] - x

# Number of trials (n) and observed successes (x)
n = 10
x = 3

# Initial guess for p
initial_p = [0.5]

# Constraint for mean
con = {'type': 'eq', 'fun': constraint_mean, 'args': (n, x)}

# Perform optimization to maximize entropy
result = minimize(shannon_entropy, initial_p, args=(n,), constraints=[con], bounds=[(0, 1)])

# Extract optimized p value
optimized_p = result.x[0]

print(f"Optimized p to maximize entropy: {optimized_p}")
