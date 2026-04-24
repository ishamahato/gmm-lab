import matplotlib.pyplot as plt
import numpy as np

xc, yc = 10, 10
r = 30

theta = np.linspace(0, 2*np.pi, 200)

x = xc + r * np.cos(theta)
y = yc + r * np.sin(theta)

plt.plot(x, y)
plt.scatter(xc, yc)

plt.title("Circle (10,10), r=30")
plt.gca().set_aspect('equal')
plt.grid()
plt.show()
