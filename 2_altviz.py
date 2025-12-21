"""Simple altitude vs time visualization.

This script demonstrates a basic use of NumPy for numerical data and
Matplotlib for plotting. The spacecraft altitude is modeled as a simple
quadratic function of time: altitude = 0.01 * t^2.
"""

import numpy as np
import matplotlib.pyplot as plt

# Create an array of time values from 0 to 100 (inclusive) with 101 points.
# `np.linspace(start, stop, num)` returns `num` equally spaced samples.
time = np.linspace(0, 100, 101)
print(f"time (0..100) length: {time.size}")

# Pre-allocate an array for altitude values for performance and clarity.
# np.zeros(n) creates an array of zeros of length n.
altitude = np.zeros(time.size)
print(f"Initial altitude array (zeros): shape={altitude.shape}")

# Populate the altitude array using a simple kinematic model:
# altitude(t) = 0.01 * t^2 (units: kilometers if t is seconds here)
# Using vectorized operations is preferred (fast), but this loop mirrors
# the original pedagogical approach and is clear for beginners.
for i in range(len(time)):
    altitude[i] = 0.01 * time[i] ** 2

# --- Optional: user code area ---
# You can add more processing here, for example:
# - add noise: altitude += np.random.normal(0, 0.5, size=altitude.shape)
# - compute velocity: velocity = np.gradient(altitude, time)
# - find max altitude/time: idx = np.argmax(altitude)
# The original marker left a place for additional code.


# Plot the altitude vs time
plt.figure(figsize=(8, 6))
plt.plot(time, altitude, 'b-', label='Spacecraft Altitude')
plt.title('Spacecraft Ascent: Altitude vs. Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Altitude (kilometers)')
plt.grid(True)
plt.legend()
plt.show()