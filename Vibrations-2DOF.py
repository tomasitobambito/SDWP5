import numpy as np
from scipy.linalg import eigvals

# Masses and spring constants
m1, m2 = 819.52, 302.244
k1, k2 = 692234506, 290888835

# Mass matrix
M = np.array([[m1, 0],
              [0, m2]])

# Stiffness matrix
K = np.array([[k1 + k2, -k2],
              [-k2, k2]])

# Eigenvalues represent squared natural frequencies
eigenvalues = eigvals(K, M)

# Take the square root to obtain the natural frequencies
natural_frequencies = np.sqrt(eigenvalues) * (1/(2*np.pi))

print("Natural Frequencies:", natural_frequencies)