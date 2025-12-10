import numpy as np

# 1D array and a scalar
a = np.array([1, 2, 3])
b = 2  # scalar

# Scalar is broadcast to the shape of `a`: treated as [2, 2, 2]
result = a + b
print(result)                # output: [3 4 5]
print("A shape:", a.shape)   # A shape: (3,)
print("B shape (scalar):", np.shape(b))  # scalar has shape ()

# 2D array and 1D row vector
a = np.array([[1, 2, 3],
              [4, 5, 6]])     # shape (2, 3)
b = np.array([0, 5, 10])      # shape (3,) -- treated as (1,3) for broadcasting

# Broadcasting rules:
# - Align shapes right-to-left.
# - Dimensions are compatible when equal or one of them is 1.
# Here (2,3) and (3,) -> (2,3) and (1,3) -> b is broadcast across the 1st axis.
result = a + b                # each row of `a` has `b` added elementwise
print(result)                 # output: [[1 7 13], [4 10 16]]
print("A shape:", a.shape)    # A shape: (2, 3)
print("B shape:", b.shape)    # B shape: (3,)