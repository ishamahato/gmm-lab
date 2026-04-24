import numpy as np
import matplotlib.pyplot as plt

# Cube vertices
vertices = np.array([
    [0,0,0],[50,0,0],[50,50,0],[0,50,0],
    [0,0,50],[50,0,50],[50,50,50],[0,50,50]
])

theta = np.radians(30)

# Scaling matrix
S = np.array([
    [2,0,0],
    [0,1.5,0],
    [0,0,1]
])

# Rotation Z matrix
Rz = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0,0,1]
])

# Translation vector
T = np.array([20,30,10])

# -------- Order 1: Scale → Rotate → Translate --------
SRT = vertices @ S.T
SRT = SRT @ Rz.T
SRT = SRT + T

# -------- Order 2: Translate → Rotate → Scale --------
TRS = vertices + T
TRS = TRS @ Rz.T
TRS = TRS @ S.T

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Original
ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], label="Original")

# SRT
ax.scatter(SRT[:,0], SRT[:,1], SRT[:,2], label="Scale→Rotate→Translate")

# TRS
ax.scatter(TRS[:,0], TRS[:,1], TRS[:,2], label="Translate→Rotate→Scale")

ax.set_title("Composite 3D Transformations")
ax.legend()

plt.show()

# Print few points
print("SRT (first point):", SRT[0])
print("TRS (first point):", TRS[0])
