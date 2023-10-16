# Define Shannon entropy for Multinomial distribution with a fixed number of samples
def shannon_entropy_multinomial_fixed_samples(p, n):
    entropy = -np.sum(p_i * np.log2(p_i) for p_i in p if p_i > 0)  # Exclude zero terms
    return -n * entropy  # Account for the number of samples

# Define constraint for the average rating with a fixed number of samples
def constraint_average_fixed_samples(p, avg, n):
    weighted_sum = np.sum(i * p_i for i, p_i in enumerate(p, start=1))
    return n * weighted_sum - n * avg  # Account for the number of samples

# Known average review and number of reviews
# Takes in the average rating and number of stars and outputs the p distribution given max entropy

avg_review = 3.5
num_reviews = 10

# Initial guess for p
initial_p = [0.2, 0.2, 0.2, 0.2, 0.2]

# Constraint for average review
con_avg = {'type': 'eq', 'fun': constraint_average_fixed_samples, 'args': (avg_review, num_reviews)}

# Additional constraint for probabilities to sum to 1
con_sum = {'type': 'eq', 'fun': lambda p: np.sum(p) - 1}

# Perform optimization to maximize entropy
result_fixed_samples = minimize(shannon_entropy_multinomial_fixed_samples, initial_p, args=(num_reviews,), constraints=[con_avg, con_sum], bounds=[(0, 1)]*5)

# Extract optimized p values
optimized_p_multinomial_fixed_samples = result_fixed_samples.x

optimized_p_multinomial_fixed_samples
