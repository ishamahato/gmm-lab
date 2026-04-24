import matplotlib.pyplot as plt

# Clipping window
xmin, ymin = 10, 10
xmax, ymax = 100, 100

# Compute region code
def compute_code(x, y):
    code = 0

    if x < xmin: code |= 1      # LEFT
    if x > xmax: code |= 2      # RIGHT
    if y < ymin: code |= 4      # BOTTOM
    if y > ymax: code |= 8      # TOP

    return code

def cohen_sutherland(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)

    accept = False

    while True:
        if (code1 | code2) == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break
        else:
            x, y = 0, 0
            code_out = code1 if code1 != 0 else code2

            if code_out & 8:  # TOP
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & 4:  # BOTTOM
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & 2:  # RIGHT
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & 1:  # LEFT
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    return accept, x1, y1, x2, y2


# Input line
x1, y1 = 5, 20
x2, y2 = 120, 80

accept, cx1, cy1, cx2, cy2 = cohen_sutherland(x1, y1, x2, y2)

# Plotting
plt.figure()

# Original line (dashed)
plt.plot([x1, x2], [y1, y2], 'b--', label="Original Line")

# Clipping window
plt.plot([xmin, xmax, xmax, xmin, xmin],
         [ymin, ymin, ymax, ymax, ymin], 'r', label="Clipping Window")

# Clipped line
if accept:
    plt.plot([cx1, cx2], [cy1, cy2], 'g', linewidth=2, label="Clipped Line")
    print("Line Accepted (Partially Clipped)")
    print(f"Clipped Line: ({cx1:.2f}, {cy1:.2f}) to ({cx2:.2f}, {cy2:.2f})")
else:
    print("Line Rejected")

plt.xlim(0, 150)
plt.ylim(0, 150)
plt.legend()
plt.title("Cohen-Sutherland Line Clipping")

plt.grid()
plt.show()
