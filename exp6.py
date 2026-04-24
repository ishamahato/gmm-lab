import numpy as np
import matplotlib.pyplot as plt

# Cube vertices
vertices = np.array([
    [0,0,0],[50,0,0],[50,50,0],[0,50,0],
    [0,0,50],[50,0,50],[50,50,50],[0,50,50]
])

# Fixed point
P = np.array([10,10,10])

# Scaling factors
S = np.array([2,2,2])

# Step 1: Translate to origin
translated = vertices - P

# Step 2: Scale
scaled = translated * S

# Step 3: Translate back
final = scaled + P

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Original
ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], label="Original")

# Scaled
ax.scatter(final[:,0], final[:,1], final[:,2], label="Scaled about P")

# Mark point P
ax.scatter(P[0], P[1], P[2], label="Fixed Point P", s=100)

ax.set_title("Scaling About Arbitrary Point")
ax.legend()

plt.show()

# Print one example
print("Original:", vertices[1])
print("Scaled:", final[1])
