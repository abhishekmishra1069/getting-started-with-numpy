import numpy as np

# english thrust units - foot-pounds (force in lbf, time in seconds)
burn_data = np.array([
    [140.0, 600],  # [force (lbf), duration (s)]
    [140.0, 300],
    [140.0, 900],
])

# Conversion factor from pound-force to newtons (1 lbf ≈ 4.44822 N)
lbf_to_newton = 4.44822

# Split columns: forces in lbf and times in seconds
forces_lbf = burn_data[:, 0]  # first column: forces (lbf)
times = burn_data[:, 1]       # second column: durations (s)

# Convert forces to newtons (element-wise multiplication)
forces_newton = forces_lbf * lbf_to_newton

# Reassemble into a 2-column array: [force (N), time (s)]
converted_burn_data = np.column_stack((forces_newton, times))

# Compute impulse = force × time
# original_impulse uses lbf × s (wrong units if treated as N·s)
original_impulse = burn_data[:, 0] * burn_data[:, 1]
# correct_impulse uses N × s (SI units)
correct_impulse = converted_burn_data[:, 0] * converted_burn_data[:, 1]

# Print summary tables and the error factor when mixing units
print("Original Burn Data [Force (lbf), Time (s)]:\n", burn_data)
print("\nConverted Burn Data [Force (N), Time (s)]:\n", converted_burn_data)
print("\nOriginal Impulse (lbf·s, wrongly treated as N·s):", original_impulse)
print("Correct Impulse (N·s):", correct_impulse)
print("\nImpulse Error Factor (Original vs. Correct):",
      original_impulse / correct_impulse)