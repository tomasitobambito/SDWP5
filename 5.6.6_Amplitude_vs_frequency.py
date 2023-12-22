import matplotlib.pyplot as plt
import numpy as np

# Constants
m = 302.224
k = 290888835
forcing = 0.9*9.80665/m

# Data Range
time_step = 200000
duration = 1
max_frequency = 225

# Plot Data
max_displacement = []
frequencies = []

for frequency in range(1, max_frequency+1):
    frequencies.append(frequency)
    omega_n = np.sqrt(k/m)
    omega_f = 2*np.pi*frequency

    # Maximum displacement computation for current frequency
    displacement = []
    times = []
    for time in range(time_step):
        times.append(time / time_step)
        displacement.append(
            (forcing/(omega_n**2-omega_f**2))*np.sin(omega_f*time*duration/time_step))
    max_displacement.append(max(displacement))

# comment out ylim for a maximum frequency of 100 Hz
plt.ylim(0, 0.6*10**(-6))
plt.grid(True)
plt.title("Amplitude vs Frequency")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude [m]")

plt.plot(frequencies, max_displacement, color="navy")

plt.show()
