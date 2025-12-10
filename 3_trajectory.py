import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # registers the 3D projection with matplotlib

# Create a time array with 100 samples evenly spaced between 0 and 10.
# This parameter t drives the parametric equations for x, y, z.
t = np.linspace(0, 10, 100)

# Parametric definitions:
# - x and y use cosine and sine of t to form a circle in the XY plane.
# - z increases linearly with t (t / 2), so the circle moves upward as t increases,
#   producing a helix (spiral) in 3D space.
x = np.cos(t)
y = np.sin(t)
z = t / 2

# Build an explicit (N, 3) trajectory array where each row is a point [x, y, z].
# Using a single array makes it easy to do per-axis selection and slicing.
traj = np.zeros((t.size, 3), dtype=np.float64)
traj[:, 0] = x  # column 0 = x coordinates
traj[:, 1] = y  # column 1 = y coordinates
traj[:, 2] = z  # column 2 = z coordinates

# Select points where the z coordinate is below a threshold.
# np.where returns indices satisfying the condition; we take the first element
# because np.where returns a tuple (one array per dimension).
z_threshold = 1.0
indexes = np.where(traj[:, 2] < z_threshold)[0]  # indices with z < threshold
low_altitude_points = traj[indexes, :]           # subset of trajectory under threshold

# Plot the full trajectory and highlight the low-altitude points.
# - ax.plot draws a continuous blue line for the full helix.
# - ax.scatter marks the selected points in red.
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Continuous trajectory line
ax.plot(x, y, z, 'b-', linewidth=2)

# Highlighted subset (low altitude)
ax.scatter(
    low_altitude_points[:, 0],  # x coords of selected points
    low_altitude_points[:, 1],  # y coords of selected points
    low_altitude_points[:, 2],  # z coords of selected points
    c='red',
    s=50,
    label='low altitude'
)

# Label axes for clarity (units here are arbitrary; the code uses 'km').
ax.set_xlabel('km')
ax.set_ylabel('km')
ax.set_zlabel('km')

# Show the plot window.
plt.show()