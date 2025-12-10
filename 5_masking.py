import numpy as np

# Create a 1D NumPy array with positive and negative integers
x = np.array([-2, -1, 1, 2, 5])

# Build a boolean mask where the condition (x > 0) is True for positive elements.
# The mask is an array of booleans with the same shape as x: [False, False, True, True, True]
mask = x > 0

# Use the mask to index x. This returns a new array containing only the elements
# where mask is True (all positive numbers in x).
print(x[mask])

# You can apply the condition inline without creating a separate mask variable.
# This is equivalent to the previous print statement.
print(x[x > 0])

# Create another mask for even elements using the modulo operator.
# x % 2 == 0 produces [True, False, False, True, False] for this x.
mask = x % 2 == 0

# Use the even-mask to select even elements from x.
print(x[mask])