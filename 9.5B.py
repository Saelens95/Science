# 9.5 Part B -- Animation of piano string

from vpython import *
import numpy as np

# most of code is same as Part A
v = 100.0
L = 1.0
d = 0.1
C = 1.0
sigma = 0.3
h = 1e-6
N = 100

# conditions
x = 0.0
t = 0.0
t_end = 0.1

# animation -- using sphere function from text
spheres = []
for i in range(N + 1):
    x = i * (L / N) # piano string length / steps
    position = vector(x,0,0)
    spheres.append(sphere(pos=position, radius=0.01, color=color.green)) # reminds me of the matrix

# main-loop
t = 0.0
while t <= t_end:   # it seems that the animation speed stays the same even though I increase value of t_end

    for i in range(N + 1):
        x = i * (L / N)
        displacement = C * (x * (L - x) / L ** 2) * np.exp(-((x - d) ** 2) / (2 * sigma ** 2)) # psi func.
        spheres[i].pos.y = displacement * 5 # update y-pos of sphere with psi func --> multiply by 5 to see better
        x += L / N  # update position

    rate(1000)
    t += h