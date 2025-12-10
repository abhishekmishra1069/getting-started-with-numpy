import numpy as np
from Timer import Timer

data = np.array(range(1000))

array = np.array(data)

with Timer() as t:
    mean = np.mean(array)
    
print (f"Time taken: {t.interval:.6f} seconds")
print(f"Grade: {mean:.2f}")

def compute_sum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    
    return sum/len(array)

with Timer() as s:
    mean_custom = compute_sum(array)
    
print(f"Time taken (custom sum): {s.interval:.6f} seconds")