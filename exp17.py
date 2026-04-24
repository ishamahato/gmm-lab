import matplotlib.pyplot as plt

# Input
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# DDA Algorithm
dx = x2 - x1
dy = y2 - y1

steps = int(max(abs(dx), abs(dy)))

x_inc = dx / steps
y_inc = dy / steps

x = x1
y = y1

x_points = []
y_points = []

for i in range(steps + 1):
    x_points.append(round(x))
    y_points.append(round(y))
    x += x_inc
    y += y_inc

# Plot
plt.figure()

# Draw axes (4 quadrants)
plt.axhline(0)
plt.axvline(0)

# Plot points
plt.plot(x_points, y_points)

plt.title("DDA Line Drawing")
plt.grid()

plt.show()

# Print points
print("Points:")
for i in range(len(x_points)):
    print(f"({x_points[i]}, {y_points[i]})")
