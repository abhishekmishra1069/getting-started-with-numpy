import numpy as np

# Examples of reshaping and axis operations (some lines are commented out
# in the original file; kept here as examples you can enable).
# - reshape: change the shape of an array to a compatible shape
# - transpose: swap axes of a 2D array
# - ravel / flatten: produce a 1D view/copy of the array

# Example: a 1D array reshaped to 2x2 (uncomment to use)
# arr = np.array([1, 2, 3, 4])
# print(f"Reshape to grid: {np.reshape(arr, (2, 2))}")

# Create a 3D array with shape (2, 2, 2)
arr = np.array([[[1, 2], [3, 4]],
                [[5, 6], [7, 8]]])
# Current shape: (2, 2, 2) -> 2 blocks of 2x2 matrices

# Example: reshape the 3D array to shape (2,1,4) (uncomment to use)
# print(f"Reshape #2: {np.reshape(arr, (2, 1, 4))}")

# Example: transpose a 2D array (uncomment if arr is 2D)
# arr2 = np.array([[1,2], [3,4], [5,6], [7,8]])
# print(f"Transpose: {np.transpose(arr2)}")
from Timer import Timer
with Timer() as t:
    ravelled = np.ravel(arr)
print(f"Time taken for ravel: {t.interval:.6f} seconds")
# ravel: returns a 1D view of the array when possible (no copy usually)
print(f"Ravel: {ravelled}")    # output: [1 2 3 4 5 6 7 8]

# flatten: always returns a 1D copy of the array
with Timer() as t2:
    flattened = arr.flatten()
print(f"Time taken for flatten: {t2.interval:.6f} seconds")
print(f"Flatten: {flattened}")  # output: [1 2 3 4 5 6 7 8]