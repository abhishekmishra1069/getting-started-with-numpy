import pandas as pd
import numpy as np

# Read a whitespace/comma separated sensor file into a pandas DataFrame.
# The file must contain columns at least: time, sensor_id, temp, rad
df = pd.read_csv('sensor_data.txt')
print("Original DataFrame:")
print(df)

# Pivot to wide format:
# - index = time (rows will correspond to timestamps)
# - columns = sensor_id (each sensor becomes a column)
# - values = temp (create a table of temperatures: time × sensor)
pivot_temp = df.pivot(index='time', columns='sensor_id', values='temp')
# Same for radiation values
pivot_rad = df.pivot(index='time', columns='sensor_id', values='rad')

# Convert pivoted DataFrames to NumPy arrays.
# After pivoting, pivot_temp.to_numpy() has shape (n_times, n_sensors)
temp_array = pivot_temp.to_numpy()
rad_array = pivot_rad.to_numpy()

# Stack the two measurement arrays along a new last axis (measurements).
# Resulting shape: (n_times, n_sensors, 2) where the last axis = [temp, rad]
sensor_array = np.dstack((temp_array, rad_array))

print("\nReshaped 3D NumPy array (time, sensors, measurements):")
print(sensor_array.round(2))
print("Shape:", sensor_array.shape)  # (n_times, n_sensors, 2)

# Flatten the 3D array to 1D (row-major / C-order by default)
flattened = np.ravel(sensor_array)
print(flattened)

# Reshape flattened array into pairs [temp, rad] per row.
# The -1 infers the correct first dimension so each row holds two measurements.
flat_array = flattened.reshape(-1, 2)
print(flat_array)

# Rebuild a DataFrame from the flattened array.
# NOTE: the MultiIndex below must match the ordering and counts produced by the ravel.
# ravel iterates fastest over the last axis, then the previous axes (C-order).
# Here the code assumes times = [0,1,2,3] and sensors = ['S1','S2'] — adapt to your data.
df_from_array = pd.DataFrame(
    flat_array,
    columns=['temp', 'rad'],
    index=pd.MultiIndex.from_product(
        [[0, 1, 2, 3], ['S1', 'S2']],
        names=['time', 'sensor_id']
    )
)

# Reset index to get 'time' and 'sensor_id' as columns and print.
df_from_array = df_from_array.reset_index()
print("\nDataFrame from 3D NumPy array (using ravel):")
print(df_from_array)