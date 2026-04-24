import matplotlib.pyplot as plt

# Input
r = 5
xc, yc = 0, 0

# Initial values
x = 0
y = r
p = 1 - r

points_x = []
points_y = []

print("Iteration | x | y | p")
print("------------------------")

# Function to plot all 8 symmetric points
def plot_circle(xc, yc, x, y):
    pts = [
        (xc+x, yc+y), (xc-x, yc+y),
        (xc+x, yc-y), (xc-x, yc-y),
        (xc+y, yc+x), (xc-y, yc+x),
        (xc+y, yc-x), (xc-y, yc-x)
    ]
    return pts

# Loop
i = 0
while x <= y:
    print(f"{i:9} | {x} | {y} | {p}")

    pts = plot_circle(xc, yc, x, y)
    for px, py in pts:
        points_x.append(px)
        points_y.append(py)

    x += 1

    if p < 0:
        p = p + 2*x + 1
    else:
        y -= 1
        p = p + 2*(x - y) + 1

    i += 1

# Plot
plt.figure()
plt.scatter(points_x, points_y)

# Axes
plt.axhline(0)
plt.axvline(0)

plt.gca().set_aspect('equal')
plt.title("Midpoint Circle (r=5)")
plt.grid()

plt.show()
