import numpy as np

# Two small 2×2 arrays used to demonstrate different stacking operations.
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Print the original arrays for reference
print("arr1:\n", arr1)
print("arr2:\n", arr2)

# Print dimensionality (ndim) and shape for each input array
# - ndim = number of axes (dimensions)
# - shape = size along each axis (rows, columns, ...)
print("arr1 ndim:", arr1.ndim, "shape:", arr1.shape)
print("arr2 ndim:", arr2.ndim, "shape:", arr2.shape)

# Horizontal stacking (concatenate columns)
# For two (2,2) arrays, hstack produces a (2,4) array
h = np.hstack((arr1, arr2))
print("\nHorizontal stacking (np.hstack):\n", h)
print("h shape:", h.shape, "ndim:", h.ndim)

# Vertical stacking (concatenate rows)
# For two (2,2) arrays, vstack produces a (4,2) array
v = np.vstack((arr1, arr2))
print("\nVertical stacking (np.vstack):\n", v)
print("v shape:", v.shape, "ndim:", v.ndim)

# Depth stacking (stack arrays along a new third axis)
# For two (2,2) arrays, dstack produces a (2,2,2) array where the last axis is depth
d = np.dstack((arr1, arr2))
print("\nDepth stacking (np.dstack) - adds a new depth axis:\n", d)
print("d shape:", d.shape, "ndim:", d.ndim)

# np.stack can also be used to create a new axis at a chosen position.
# Example: stack along axis=0 -> shape (2, 2, 2) (first axis selects which array)
s0 = np.stack((arr1, arr2), axis=0)
print("\nnp.stack axis=0 ->\n", s0)
print("s0 shape:", s0.shape, "ndim:", s0.ndim)
