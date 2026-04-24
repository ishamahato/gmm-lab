import matplotlib.pyplot as plt

# Window
xmin, ymin = 10, 10
xmax, ymax = 100, 100

def liang_barsky(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    t1, t2 = 0.0, 1.0

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return False, None
        else:
            t = q[i] / p[i]

            if p[i] < 0:
                t1 = max(t1, t)
            else:
                t2 = min(t2, t)

    if t1 > t2:
        return False, None

    x_start = x1 + t1 * dx
    y_start = y1 + t1 * dy
    x_end = x1 + t2 * dx
    y_end = y1 + t2 * dy

    return True, (x_start, y_start, x_end, y_end)

# Input line
x1, y1 = 0, 50
x2, y2 = 120, 80

result, clipped = liang_barsky(x1, y1, x2, y2)

plt.figure()

# Draw window
plt.plot([xmin,xmax,xmax,xmin,xmin],
         [ymin,ymin,ymax,ymax,ymin], label="Window")

# Original line
plt.plot([x1,x2],[y1,y2], linestyle='dashed', label="Original Line")

if result:
    x_start, y_start, x_end, y_end = clipped
    plt.plot([x_start,x_end],[y_start,y_end], linewidth=2, label="Clipped Line")
    print(f"Clipped Line: ({x_start:.2f},{y_start:.2f}) to ({x_end:.2f},{y_end:.2f})")
else:
    print("Line Rejected")

plt.legend()
plt.title("Liang-Barsky Line Clipping")
plt.grid()
plt.xlim(0,150)
plt.ylim(0,150)

plt.show()
