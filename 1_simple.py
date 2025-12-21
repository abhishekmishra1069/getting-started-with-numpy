import numpy as np
from Timer import Timer

# Create a large sequence of integers and convert to a NumPy array.
# Using a NumPy array allows fast, vectorized numerical operations.
data = np.array(range(54_000_000))

# `array` holds the same data; kept for clarity with the original example.
array = np.array(data)

# Use the Timer context manager to measure how long NumPy's mean takes.
with Timer() as t:
	# NumPy's `mean` is implemented in C and is highly optimized.
	mean = np.mean(array)

print(f"Time taken: {t.interval:.6f} seconds")
print(f"Grade: {mean:.2f}")


def compute_sum(array):
	"""Compute the mean using an explicit Python loop.

	This function demonstrates a pure-Python approach (much slower
	for large arrays) so you can compare it with NumPy's performance.
	We avoid naming the variable `sum` to not shadow the built-in.
	"""
	total = 0
	# Iterate over each index and accumulate the value.
	for i in range(len(array)):
		total += array[i]

	# Return the average (mean).
	return total / len(array)


# Measure the time taken by the custom Python summation.
with Timer() as s:
	mean_custom = compute_sum(array)

print(f"Time taken (custom sum): {s.interval:.6f} seconds")
print(f"Grade (custom): {mean_custom:.2f}")