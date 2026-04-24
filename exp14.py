import matplotlib.pyplot as plt
import numpy as np

# Square points
square = np.array([[0,3],[3,3],[3,0],[0,0]])

# Triangle points
triangle = np.array([[0,0],[4,0],[2,3]])

def plot_shape(original, transformed, title):
    plt.figure()

    # Original
    o = np.vstack([original, original[0]])
    plt.plot(o[:,0], o[:,1], label="Original")

    # Transformed
    t = np.vstack([transformed, transformed[0]])
    plt.plot(t[:,0], t[:,1], label="Transformed")

    plt.axhline(0)
    plt.axvline(0)
    plt.grid()
    plt.legend()
    plt.title(title)
    plt.show()

# Transformations
def translate(shape, tx, ty):
    return shape + [tx, ty]

def scale(shape, sx, sy):
    return shape * [sx, sy]

def reflect_x(shape):
    return shape * [1, -1]

def shear(shape, shx, shy):
    new = []
    for x,y in shape:
        new.append([x + shx*y, y + shy*x])
    return np.array(new)

def rotate(shape, angle):
    theta = np.radians(angle)
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    return shape @ R.T

# Menu
while True:
    print("\n--- MENU ---")
    print("1. Square Scaling")
    print("2. Square Translation")
    print("3. Square Reflection (X-axis)")
    print("4. Square Shearing")
    print("5. Square Rotation")
    print("6. Triangle Transformations")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        result = scale(square, 2, 3)
        plot_shape(square, result, "Scaling")

    elif choice == 2:
        result = translate(square, 1, 5)
        plot_shape(square, result, "Translation")

    elif choice == 3:
        result = reflect_x(square)
        plot_shape(square, result, "Reflection X-axis")

    elif choice == 4:
        result = shear(square, 3, 4)
        plot_shape(square, result, "Shearing")

    elif choice == 5:
        result = rotate(square, 90)
        plot_shape(square, result, "Rotation 90°")

    elif choice == 6:
        print("\nTriangle Transformations")
        print("1. Translation")
        print("2. Scaling")
        print("3. Shearing")
        print("4. Reflection")
        print("5. Rotation")

        ch = int(input("Enter choice: "))

        if ch == 1:
            result = translate(triangle, 2, 2)
        elif ch == 2:
            result = scale(triangle, 2, 2)
        elif ch == 3:
            result = shear(triangle, 1, 1)
        elif ch == 4:
            result = reflect_x(triangle)
        elif ch == 5:
            result = rotate(triangle, 45)

        plot_shape(triangle, result, "Triangle Transformation")

    elif choice == 7:
        break

    else:
        print("Invalid choice")
