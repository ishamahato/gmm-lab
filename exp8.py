import matplotlib.pyplot as plt

# Window
wxmin, wymin = 0, 0
wxmax, wymax = 100, 100

# Viewport
vxmin, vymin = 200, 200
vxmax, vymax = 400, 400

# Points
points = [(20,30), (60,70)]

# Scale factors
sx = (vxmax - vxmin) / (wxmax - wxmin)
sy = (vymax - vymin) / (wymax - wymin)

mapped_points = []

for (xw, yw) in points:
    xv = vxmin + (xw - wxmin) * sx
    yv = vymin + (yw - wymin) * sy
    mapped_points.append((xv, yv))

# Plot
plt.figure()

# Window
plt.plot([wxmin, wxmax, wxmax, wxmin, wxmin],
         [wymin, wymin, wymax, wymax, wymin], label="Window")

# Viewport
plt.plot([vxmin, vxmax, vxmax, vxmin, vxmin],
         [vymin, vymin, vymax, vymax, vymin], label="Viewport")

# Points
for (xw, yw), (xv, yv) in zip(points, mapped_points):
    plt.scatter(xw, yw)
    plt.scatter(xv, yv)
    print(f"({xw},{yw}) -> ({xv},{yv})")

plt.legend()
plt.title("Window to Viewport Mapping")
plt.grid()

plt.show()
