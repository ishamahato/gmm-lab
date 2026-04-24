import matplotlib.pyplot as plt

# Clipping window
xmin, ymin = 10, 10
xmax, ymax = 60, 60

# Points
points = [(5,5), (20,30), (70,40), (50,70)]

visible = []
invisible = []

# Check visibility
for (x, y) in points:
    if xmin <= x <= xmax and ymin <= y <= ymax:
        visible.append((x, y))
        print(f"{(x,y)} -> Visible")
    else:
        invisible.append((x, y))
        print(f"{(x,y)} -> Invisible")

# Plot
plt.figure()

# Draw clipping window
plt.plot([xmin, xmax, xmax, xmin, xmin],
         [ymin, ymin, ymax, ymax, ymin],
         label="Clipping Window")

# Plot visible points
if visible:
    x, y = zip(*visible)
    plt.scatter(x, y, label="Visible Points")

# Plot invisible points
if invisible:
    x, y = zip(*invisible)
    plt.scatter(x, y, label="Invisible Points")

# Draw a line (example shape)
line_x = [0, 80]
line_y = [0, 80]
plt.plot(line_x, line_y, linestyle='dashed', label="Original Line")

# Clipped line (manually inside window)
clipped_x = [10, 60]
clipped_y = [10, 60]
plt.plot(clipped_x, clipped_y, linewidth=2, label="Clipped Line")

plt.legend()
plt.title("Clipping of Points and Shapes")
plt.grid()

plt.xlim(0, 80)
plt.ylim(0, 80)

plt.show()
