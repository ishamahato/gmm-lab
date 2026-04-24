import matplotlib.pyplot as plt

# Input
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# Bresenham Algorithm
x, y = x1, y1
dx = abs(x2 - x1)
dy = abs(y2 - y1)

sx = 1 if x2 > x1 else -1
sy = 1 if y2 > y1 else -1

points_x = []
points_y = []

if dx > dy:
    p = 2*dy - dx
    for i in range(dx + 1):
        points_x.append(x)
        points_y.append(y)

        x += sx
        if p < 0:
            p += 2*dy
        else:
            y += sy
            p += 2*(dy - dx)
else:
    p = 2*dx - dy
    for i in range(dy + 1):
        points_x.append(x)
        points_y.append(y)

        y += sy
        if p < 0:
            p += 2*dx
        else:
            x += sx
            p += 2*(dx - dy)

# Plot
plt.figure()

# Draw axes
plt.axhline(0)
plt.axvline(0)

# Plot line
plt.plot(points_x, points_y)

plt.title("Bresenham Line Drawing")
plt.grid()

plt.show()

# Output points
print("Points:")
for i in range(len(points_x)):
    print(f"({points_x[i]}, {points_y[i]})")
