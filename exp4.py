import numpy as np
import matplotlib.pyplot as plt

# Cube vertices
vertices = np.array([
    [0,0,0],[50,0,0],[50,50,0],[0,50,0],
    [0,0,50],[50,0,50],[50,50,50],[0,50,50]
])

theta = np.radians(45)

# Rotation matrices
Rx = np.array([
    [1,0,0],
    [0,np.cos(theta),-np.sin(theta)],
    [0,np.sin(theta),np.cos(theta)]
])

Ry = np.array([
    [np.cos(theta),0,np.sin(theta)],
    [0,1,0],
    [-np.sin(theta),0,np.cos(theta)]
])

Rz = np.array([
    [np.cos(theta),-np.sin(theta),0],
    [np.sin(theta),np.cos(theta),0],
    [0,0,1]
])

# Apply rotations
rot_x = vertices @ Rx.T
rot_y = vertices @ Ry.T
rot_z = vertices @ Rz.T

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Original cube
ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], label='Original')

# Rotated cubes
ax.scatter(rot_x[:,0], rot_x[:,1], rot_x[:,2], label='X-rotated')
ax.scatter(rot_y[:,0], rot_y[:,1], rot_y[:,2], label='Y-rotated')
ax.scatter(rot_z[:,0], rot_z[:,1], rot_z[:,2], label='Z-rotated')

ax.set_title("3D Rotation of Cube")
ax.legend()

plt.show()
