import matplotlib.pyplot as plt
import numpy as np

# Constants
m = 500
k = 290888835
frequency = 100
forcing = 0.9*9.80665/m
omega_n = np.sqrt(k/m)
omega_f = 2*frequency*np.pi

# Data range
time_steps = 1000
duration = 0.2

# Plot Data
displacement = []
times = []

for time in range(time_steps):
    times.append(time * duration / time_steps)
    displacement.append(
        (-forcing * omega_f) / (omega_n * (omega_n ** 2 - omega_f ** 2)) * np.sin(omega_n * time * duration / time_steps) +
        ((forcing * omega_f) / (omega_n * (omega_n ** 2 - omega_f ** 2))) * np.cos(omega_f * time * duration / time_steps))

plt.title("Displacement vs Time")
plt.xlabel("Time [s]")
plt.ylabel("Displacement [m]")
plt.grid(True)

plt.plot(times, displacement, color="navy")
plt.axhline(linestyle="--", color="black")

plt.show()