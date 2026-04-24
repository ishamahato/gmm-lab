import numpy as np
import matplotlib.pyplot as plt

# Cube vertices
vertices = np.array([
    [0,0,0],[50,0,0],[50,50,0],[0,50,0],
    [0,0,50],[50,0,50],[50,50,50],[0,50,50]
])

# Reflection transformations
xy_reflect = vertices * [1, 1, -1]
yz_reflect = vertices * [-1, 1, 1]
zx_reflect = vertices * [1, -1, 1]

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Original
ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], label="Original")

# Reflections
ax.scatter(xy_reflect[:,0], xy_reflect[:,1], xy_reflect[:,2], label="XY-plane")
ax.scatter(yz_reflect[:,0], yz_reflect[:,1], yz_reflect[:,2], label="YZ-plane")
ax.scatter(zx_reflect[:,0], zx_reflect[:,1], zx_reflect[:,2], label="ZX-plane")

ax.set_title("3D Reflection of Cube")
ax.legend()

plt.show()

# Print example
print("Original:", vertices[6])
print("XY:", xy_reflect[6])
print("YZ:", yz_reflect[6])
print("ZX:", zx_reflect[6])
