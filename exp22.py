import numpy as np
import matplotlib.pyplot as plt

# Original polygon (A, B, C, D)
polygon = np.array([
    [2,2],
    [5,4],
    [4,7],
    [1,5]
])

# -------- Transformations --------

# Scaling (2,2)
scaled = polygon * [2,2]

# Translation (+3, +5)
translated = polygon + [3,5]

# Reflection about Y-axis
reflected = polygon * [-1,1]

# Shearing (X=1, Y=2)
sheared = []
for x,y in polygon:
    x_new = x + 1*y
    y_new = y + 2*x
    sheared.append([x_new, y_new])
sheared = np.array(sheared)

# Rotation 90° clockwise
theta = np.radians(-90)
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
rotated = polygon @ R.T

# -------- Plot --------

plt.figure(figsize=(8,8))

def draw(shape, label):
    s = np.vstack([shape, shape[0]])
    plt.plot(s[:,0], s[:,1], label=label)

draw(polygon, "Original")
draw(scaled, "Scaled")
draw(translated, "Translated")
draw(reflected, "Reflected (Y-axis)")
draw(sheared, "Sheared")
draw(rotated, "Rotated")

plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.legend()
plt.title("Polygon Transformations")

plt.show()
