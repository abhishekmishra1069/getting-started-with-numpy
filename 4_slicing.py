import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7])

# data[::] uses the full slice form start:stop:step with defaults.
# - start omitted -> 0
# - stop omitted -> len(data)
# - step omitted -> 1
# So data[::] returns all elements (a view of the original array).
print(data[::])  # output: [1 2 3 4 5 6 7]

# 2D example
arr = np.array([[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]])

# arr[1:3, 1] means:
# - For rows: 1:3 -> start at row index 1 up to (but not including) row index 3 -> rows 1 and 2
# - For columns: 1 -> take column index 1
# Result is a 1D array with elements from rows 1 and 2 at column 1 -> [4, 7]
print(arr[1:3, 1])  # output: [4 7]

# Examples (not executed here) to illustrate variations:
# data[::2] -> every 2nd element -> [1,3,5,7]
# data[::-1] -> reversed -> [7,6,5,4,3,2,1]
# arr[:, 0] -> all rows, column 0 -> [0,3,6]
# arr[0:2, 0:2] -> top-left 2x2 subarray -> [[0,1],[3,4]]