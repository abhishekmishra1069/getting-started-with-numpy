import numpy as np

# Sample dataset (integers). Note: np.bincount requires non-negative integers.
data = np.array([30, 30, 30, 30, 30, 20, 25, 35, 40, 60, 70, 80, 90, 100])

# Arithmetic mean (average) of the data
arithmetic_mean = np.mean(data)

# bincount returns counts for each integer value from 0 to max(data).
# The index with the largest count is the mode (most frequent value).
bincount = np.bincount(data)
mode = bincount.argmax()  # integer value that appears most often

# Standard deviation measures spread around the mean
std_dev = np.std(data)

# Median is the middle value (or average of two middle values) when sorted
median = np.median(data)

# Use variable names that do not shadow Python built-ins
total = np.sum(data)
min_val = np.min(data)
max_val = np.max(data)

# Print a concise summary
print("Dataset:", data)
print(f"Arithmetic Mean (Average): {arithmetic_mean:.2f}")
print(f"Bin counts (index = value): {bincount}")
print(f"Mode (most frequent value): {mode}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"Median: {median:.2f}")
print(f"Sum: {total:.2f}")
print(f"Min: {min_val:.2f}")
print(f"Max: {max_val:.2f}")