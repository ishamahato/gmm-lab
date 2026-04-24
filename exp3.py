import matplotlib.pyplot as plt
from shapely.geometry import Polygon

# Original polygon
poly_points = [(20,20), (80,20), (100,60), (60,100), (20,80)]

# Clipping window
xmin, ymin = 30, 30
xmax, ymax = 90, 90

clip_window = [(xmin,ymin), (xmax,ymin), (xmax,ymax), (xmin,ymax)]

# Create polygons
subject = Polygon(poly_points)
clipper = Polygon(clip_window)

# Perform clipping
clipped = subject.intersection(clipper)

# Extract coordinates
clipped_coords = list(clipped.exterior.coords)

# Plotting
plt.figure()

# Original polygon
x, y = zip(*(poly_points + [poly_points[0]]))
plt.plot(x, y, linestyle='dashed', label="Original Polygon")

# Clipping window
xw, yw = zip(*(clip_window + [clip_window[0]]))
plt.plot(xw, yw, label="Clipping Window")

# Clipped polygon
xc, yc = zip(*clipped_coords)
plt.plot(xc, yc, linewidth=2, label="Clipped Polygon")

plt.legend()
plt.title("Weiler-Atherton Polygon Clipping")
plt.grid()

plt.show()

# Print result
print("Clipped Polygon Coordinates:")
for pt in clipped_coords:
    print(f"({pt[0]:.2f}, {pt[1]:.2f})")
