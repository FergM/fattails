import matplotlib.pyplot as plt
from scipy.optimize import minimize
import numpy as np

# Define Shannon entropy for Multinomial distribution with a fixed number of samples
def shannon_entropy_multinomial_fixed_samples(p, n):
    entropy = -np.sum(p_i * np.log2(p_i) for p_i in p if p_i > 0)  # Exclude zero terms
    return -n * entropy  # Account for the number of samples

# Define constraint for the average rating with a fixed number of samples
def constraint_average_fixed_samples(p, avg, n):
    weighted_sum = np.sum(i * p_i for i, p_i in enumerate(p, start=1))
    return n * weighted_sum - n * avg  # Account for the number of samples

# Function to perform optimization for given number of reviews and average rating
def optimize_probs(num_reviews, avg_review):
    # Initial guess for p
    initial_p = [0.2, 0.2, 0.2, 0.2, 0.2]
    
    # Constraint for average review
    con_avg = {'type': 'eq', 'fun': constraint_average_fixed_samples, 'args': (avg_review, num_reviews)}
    
    # Additional constraint for probabilities to sum to 1
    con_sum = {'type': 'eq', 'fun': lambda p: np.sum(p) - 1}
    
    # Perform optimization to maximize entropy
    result = minimize(shannon_entropy_multinomial_fixed_samples, initial_p, args=(num_reviews,), constraints=[con_avg, con_sum], bounds=[(0, 1)]*5)
    
    # Extract optimized p values
    return result.x

# Known average review
avg_review = 4.0

# Different number of reviews
num_reviews_list = [4, 8, 16, float('inf')]

# Store optimized probabilities
optimized_probs = {}

# Perform optimization for each number of reviews
for num_reviews in num_reviews_list:
    optimized_p = optimize_probs(num_reviews, avg_review) if num_reviews != float('inf') else optimize_probs(10000, avg_review)  # Use a large number to approximate infinity
    optimized_probs[num_reviews] = optimized_p

# Adjusted plot to show a dot plot for each case
fig, ax = plt.subplots()

# Different markers for better visibility
markers = ['o', 's', '^', 'x']

for i, (num_reviews, optimized_p) in enumerate(optimized_probs.items()):
    ax.plot(range(1, 6), optimized_p, marker=markers[i], linestyle='-', label=f'{num_reviews} Reviews')

# Labels and title
ax.set_xlabel('Star Rating')
ax.set_ylabel('Probability')
ax.set_title('Optimized Probabilities for Different Numbers of Reviews')
ax.legend()

plt.show()
