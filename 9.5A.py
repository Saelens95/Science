# 9.5 Part A -- FTCS solution of the wave equation (piano string)

import numpy as np
from numpy import empty, exp
import matplotlib.pyplot as plt
from matplotlib import *

v = 100.0
L = 1.0
d = 0.1
C = 1.0
sigma = 0.3
h = 1e-5
N = 100

# arrays -- position and velocity
psi_x = empty(N+1, float)
psi_x[0] = 0
psi_x[N] = 0
psi_x[1:N] = 0

phi_x = empty(N+1, float)

# profile function
def velocity(x):
    return C * (x*(L-x)/L**2) * exp(-((x-d)**2)/(2*sigma**2))

# init. condition -- position
x = 0.0

# init. and end times
t = 0.0
t_end = 0.1

# loop to get velocities
for i in range(N+1):
    k = velocity(x)
    phi_x[i] = k
    x += L/N

# starting new array by copying old array
psi_x_new = psi_x.copy()

# main-loop
while t <= t_end:
    # updating psi_x_new indices
    psi_x_new[0] = 0.0 # first
    psi_x_new[-1] = 0.0 # last
    psi_x_new[1:-1] = psi_x[1:-1] + h * phi_x[1:-1] # everywhere in between
    psi_x = psi_x_new.copy() # psi_x array will now have psi_x_new array values
    t += h

# plotting
plt.plot(np.linspace(0, L, N+1), phi_x)
plt.xlabel('Displacement (m)')
plt.ylabel('Velocity (m/s)')
plt.show()