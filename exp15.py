import numpy as np
import matplotlib.pyplot as plt

# ---------- Shapes ----------
square = np.array([[0,0],[3,0],[3,3],[0,3]])
triangle = np.array([[0,0],[4,0],[2,3]])
rectangle = np.array([[0,0],[6,0],[6,3],[0,3]])

# ---------- Transformations ----------
def translate(shape, tx, ty):
    return shape + [tx, ty]

def scale(shape, sx, sy):
    return shape * [sx, sy]

def rotate(shape, angle):
    theta = np.radians(angle)
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    return shape @ R.T

# ---------- Apply Transformations ----------
square_t = rotate(scale(translate(square,2,2),2,2),45)
triangle_t = rotate(scale(translate(triangle,2,2),2,2),45)
rectangle_t = rotate(scale(translate(rectangle,2,2),2,2),45)

# ---------- Plot ALL ----------
fig, axs = plt.subplots(1,3, figsize=(15,5))

def draw(ax, original, transformed, title):
    o = np.vstack([original, original[0]])
    t = np.vstack([transformed, transformed[0]])

    ax.plot(o[:,0], o[:,1], label="Original")
    ax.plot(t[:,0], t[:,1], label="Transformed")
    ax.set_title(title)
    ax.grid()
    ax.legend()
    ax.axhline(0)
    ax.axvline(0)

draw(axs[0], square, square_t, "Square")
draw(axs[1], triangle, triangle_t, "Triangle")
draw(axs[2], rectangle, rectangle_t, "Rectangle")

plt.tight_layout()
plt.show()
