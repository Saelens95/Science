# 9.4 Diffusion of Earth's Crust

import numpy as np
from numpy import empty, sin, pi
import matplotlib.pyplot as plt
from matplotlib import *

depth = 20  # meters
L = 10  # years
D = 0.01  # thermal diffusivity of Earth's crust as const.
N = 100  # number of divisions in grid
a = L / N  # grid spacing
h = 0.0001  # time-step
epsilon = h / 1000
tau = 3.154e7  # 1 year in seconds
A = 10
B = 12

# temp info + arrays
temp_low = 0.0
temp_mid = 10.0
temp_high = 11.0

T = empty(N + 1, float)
T[0] = temp_low
T[N] = temp_high
T[1:N] = temp_mid

Tp = empty(N + 1, float)
Tp[0] = temp_low
Tp[N] = temp_high

# couldn't simulate using actual values in seconds i.e. 3.15e8 for 10 years
# so I opted to use the following:
t1 = 9.0       # 9 years
t2 = 9.25      # 9.25 years
t3 = 9.50      # 9.50 years
t4 = 9.75      # 9.75 years
t_end = 10.0   # 10 years

# temp function
def Temp(t):
    return A + (B * sin(2 * pi * t) / tau)


t = 0.0

# loop to get temps and store initial time points
for i in range(N + 1):
    k = Temp(t)
    T[i] = k
    t += h

t = 0.0
c = h * D / (a * a)
depths = np.linspace(0, depth, N + 1)

# test statement
print("Init. Time: ", t, " End Time: ", t_end)
# 10 years of data
while t < t_end:

    Tp[1:N] = T[1:N] + c * (T[2:N + 1] + T[0:N - 1] - 2 * T[1:N])
    T, Tp = Tp, T
    t += h

    # checking for all four times
    if abs(t - t1) < epsilon:
        plt.plot(depths, T, label="t1")

    if abs(t - t2) < epsilon:
        plt.plot(depths, T, label="t2")

    if abs(t - t3) < epsilon:
        plt.plot(depths, T, label="t3")

    if abs(t - t4) < epsilon:
        plt.plot(depths, T, label="t4")

plt.title("Temp. of Earth's Crust v Depth")
plt.xlabel("Depth (m)")
plt.ylabel("Teperature (C)")
plt.legend()
plt.show()

# if I'm viewing things correctly, it seems that the temperature is 10 C everywhere but the start and end points
# which is what the text asked for
# though I can barely see all four time/temp profiles -- so something must be wrong