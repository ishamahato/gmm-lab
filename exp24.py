import numpy as np
import matplotlib.pyplot as plt

# Original Square
square = np.array([
    [0,0],
    [2,0],
    [2,2],
    [0,2]
])

# -------- Transformations --------

# 1. Translation (4,3)
translated = square + [4,3]

# 2. Scaling (2,2)
scaled = square * [2,2]

# 3. Reflection about X-axis
reflected = square * [1,-1]

# 4. Shearing (shx=2, shy=1)
sheared = []
for x,y in square:
    x_new = x + 2*y
    y_new = y + 1*x
    sheared.append([x_new, y_new])
sheared = np.array(sheared)

# 5. Rotation 90° anticlockwise
theta = np.radians(90)
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
rotated = square @ R.T

# -------- Plot Function --------
def draw(shape, label):
    s = np.vstack([shape, shape[0]])
    plt.plot(s[:,0], s[:,1], label=label)

# -------- Plot --------
plt.figure(figsize=(8,8))

draw(square, "Original")
draw(translated, "Translated")
draw(scaled, "Scaled")
draw(reflected, "Reflected (X-axis)")
draw(sheared, "Sheared")
draw(rotated, "Rotated 90°")

# Axes
plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.legend()
plt.title("Square Transformations")

plt.gca().set_aspect('equal')
plt.show()
