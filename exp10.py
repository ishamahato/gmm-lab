import matplotlib.pyplot as plt

# Clipping window
xmin, ymin = 10, 10
xmax, ymax = 80, 80

# Points
points = [(20,30), (90,40), (50,50), (5,60)]

inside = []
outside = []

# Check points
for (x, y) in points:
    if xmin <= x <= xmax and ymin <= y <= ymax:
        inside.append((x, y))
        print(f"{(x,y)} -> Inside")
    else:
        outside.append((x, y))
        print(f"{(x,y)} -> Outside")

# Plot
plt.figure()

# Draw clipping window
plt.plot([xmin, xmax, xmax, xmin, xmin],
         [ymin, ymin, ymax, ymax, ymin],
         label="Clipping Window")

# Plot inside points
if inside:
    x, y = zip(*inside)
    plt.scatter(x, y, label="Inside Points")

# Plot outside points
if outside:
    x, y = zip(*outside)
    plt.scatter(x, y, label="Outside Points")

plt.legend()
plt.title("Point Clipping")
plt.grid()

plt.xlim(0, 100)
plt.ylim(0, 100)

plt.show()
