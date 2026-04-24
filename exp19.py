import matplotlib.pyplot as plt
import numpy as np

a = 100   # major axis
b = 60    # minor axis

theta = np.linspace(0, 2*np.pi, 200)

x = a * np.cos(theta)
y = b * np.sin(theta)

plt.figure()

# Quadrant 1 (red)
plt.fill(x[(x>=0)&(y>=0)], y[(x>=0)&(y>=0)], color='red')

# Quadrant 3 (green)
plt.fill(x[(x<=0)&(y<=0)], y[(x<=0)&(y<=0)], color='green')

# Axes
plt.axhline(0)
plt.axvline(0)

plt.title("Ellipse Quadrants")
plt.gca().set_aspect('equal')
plt.grid()
plt.show()
